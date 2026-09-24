import DOMPurify from 'dompurify';
import { spawn, Thread, type ModuleThread } from 'threads';

type TikzApi = {
  load: (root: string) => Promise<void>;
  texify: (source: string, options: Record<string, string>) => Promise<string>;
};
const ROOT = '/vendor/tikzjax';
const TIMEOUT = 20000;
let engine: ModuleThread<TikzApi> | undefined;
let nativeWorker: Worker | undefined;
let queue: Promise<unknown> = Promise.resolve();
const cache = new Map<string, string>();

/** SVG from a TeX special is untrusted, just like imported Markdown. */
export function cleanTikzSvg(raw: string): string {
  if (raw.length > 2_000_000) throw new Error('Le schéma produit est trop volumineux.');
  const safe = DOMPurify.sanitize(raw, {
    USE_PROFILES: { svg: true, svgFilters: true },
    FORBID_TAGS: ['foreignObject', 'style', 'a', 'image', 'animate', 'animateMotion', 'animateTransform', 'set'],
    FORBID_ATTR: ['tabindex'],
    RETURN_DOM_FRAGMENT: true,
  });
  const svg = safe.querySelector('svg');
  if (!svg) throw new Error('TikZJax n’a pas produit de schéma SVG.');
  // Diagrams may refer to local definitions, never to a URL/file from the pack.
  for (const element of [svg, ...svg.querySelectorAll('*')]) {
    for (const attribute of [...element.attributes]) {
      if (attribute.localName === 'href' && !/^#[\w:.-]+$/.test(attribute.value)) {
        element.removeAttributeNode(attribute);
      } else if (/url\s*\(/i.test(attribute.value) && !/^url\(\s*['"]?#[\w:.-]+['"]?\s*\)$/.test(attribute.value)) {
        element.removeAttributeNode(attribute);
      }
    }
  }
  svg.setAttribute('role', 'img');
  svg.setAttribute('aria-label', 'Schéma TikZ');
  return svg.outerHTML;
}

export function scopeTikzSvg(cleanSvg: string, prefix: string): string {
  const parsed = new DOMParser().parseFromString(cleanSvg, 'image/svg+xml');
  const svg = parsed.documentElement;
  const ids = new Map([...svg.querySelectorAll('[id]')].map(node => [node.id, `${prefix}-${node.id}`]));
  for (const node of [svg, ...svg.querySelectorAll('*')]) {
    for (const attribute of [...node.attributes]) {
      if (attribute.name === 'id' && ids.has(attribute.value)) attribute.value = ids.get(attribute.value)!;
      else if (attribute.localName === 'href' && ids.has(attribute.value.slice(1))) attribute.value = '#' + ids.get(attribute.value.slice(1));
      else attribute.value = attribute.value.replace(/url\(\s*['"]?#([\w:.-]+)['"]?\s*\)/g, (original, id: string) => ids.has(id) ? `url(#${ids.get(id)})` : original);
    }
  }
  return new XMLSerializer().serializeToString(svg);
}

async function compile(source: string): Promise<string> {
  let timer: ReturnType<typeof setTimeout> | undefined;
  try {
    return await Promise.race([
      (async () => {
        if (!engine) {
          nativeWorker = new Worker(`${ROOT}/run-tex.js`);
          engine = await spawn<TikzApi>(nativeWorker, { timeout: 10000 });
          await engine.load(new URL(ROOT, location.origin).href);
        }
        // Libraries are shipped locally and loaded before the document starts.
        const result = await engine.texify(source, {
          tikzLibraries: 'arrows.meta,positioning,calc,shapes.geometric',
          showConsole: 'false',
        });
        return cleanTikzSvg(result);
      })(),
      new Promise<never>((_, reject) => {
        timer = setTimeout(() => reject(new Error('Le dessin a dépassé le délai de 20 secondes. Simplifiez son code TikZ.')), TIMEOUT);
      }),
    ]);
  } catch (error) {
    // A malformed/infinite TeX program must not block the editor or the queue.
    nativeWorker?.terminate();
    if (engine) void Thread.terminate(engine).catch(() => undefined);
    engine = undefined;
    nativeWorker = undefined;
    throw error;
  } finally {
    clearTimeout(timer);
  }
}

export function renderTikz(source: string, signal: AbortSignal): Promise<string> {
  if (source.length > 20000) return Promise.reject(new Error('Un schéma est limité à 20 000 caractères.'));
  if (!document.getElementById('tikz-fonts')) {
    const style = document.createElement('link');
    style.id = 'tikz-fonts';
    style.rel = 'stylesheet';
    style.href = `${ROOT}/fonts.css`;
    document.head.appendChild(style);
  }
  const task = queue.then(async () => {
    if (signal.aborted) throw new DOMException('Rendu annulé', 'AbortError');
    const cached = cache.get(source);
    if (cached) return cached;
    const result = await compile(source);
    cache.set(source, result);
    if (cache.size > 32) cache.delete(cache.keys().next().value!);
    return result;
  });
  queue = task.catch(() => undefined);
  return task;
}
