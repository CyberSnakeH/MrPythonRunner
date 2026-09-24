import { useEffect, useId, useRef, useState } from 'react';
import { renderTikz, scopeTikzSvg } from './tikzRenderer';

export function TikzDiagram({ source }: { source: string }) {
  const container = useRef<HTMLElement>(null);
  const id = useId().replace(/[^a-zA-Z0-9_-]/g, '');
  const [svg, setSvg] = useState('');
  const [error, setError] = useState('');
  const title = source.match(/^\s*%\s*(.+)/)?.[1]?.slice(0, 200) || 'Schéma TikZ';

  useEffect(() => {
    setSvg('');
    setError('');
    const controller = new AbortController();
    let timer: ReturnType<typeof setTimeout>;
    const observer = new IntersectionObserver(entries => {
      if (!entries.some(entry => entry.isIntersecting)) return;
      observer.disconnect();
      // Let the teacher finish typing before compiling a changed diagram.
      timer = setTimeout(() => {
        void renderTikz(source, controller.signal).then(result => {
          if (!controller.signal.aborted) setSvg(scopeTikzSvg(result, id));
        }).catch(reason => {
          if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : 'Impossible de dessiner ce schéma.');
        });
      }, 400);
    }, { rootMargin: '300px' });
    if (container.current) observer.observe(container.current);
    return () => { controller.abort(); observer.disconnect(); clearTimeout(timer); };
  }, [source, id]);

  return <figure ref={container} className="tikz-diagram" aria-label={title}>
    <figcaption>{title}</figcaption>
    {!svg && !error && <p className="hint" role="status">Préparation du schéma…</p>}
    {error && <>
      <p className="tikz-error" role="status">Schéma indisponible. Vérifiez son code TikZ ; les autres questions restent accessibles.</p>
      <details className="tikz-source"><summary>Détails de l’erreur</summary><pre><code>{error.slice(0, 16000)}</code></pre></details>
    </>}
    {svg && <div className="tikz-output" dangerouslySetInnerHTML={{ __html: svg }} />}
    <details className="tikz-source"><summary>Voir le code TikZ</summary><pre><code>{source}</code></pre></details>
  </figure>;
}
