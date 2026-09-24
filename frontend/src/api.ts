type NativeWindow = Window & { pywebview?: { api: { save_file: (filename: string, data: string) => Promise<boolean> } } };
const token = new URLSearchParams(location.hash.slice(1)).get('token') || sessionStorage.getItem('runner-token') || '';
if (token) sessionStorage.setItem('runner-token', token);
if (location.hash) history.replaceState(null, '', location.pathname);

export async function api<T = { ok: boolean }>(path: string, data: unknown = {}): Promise<T> {
  const response = await fetch(`/api/${path}`, { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-Runner-Token': token }, body: JSON.stringify(data) });
  const body = await response.json();
  if (!response.ok) throw new Error(body.error || 'Une erreur est survenue.');
  return body as T;
}

type Save = { path: string; data: unknown };
const pending = new Map<string, Save>();
let timer: ReturnType<typeof setTimeout> | undefined;
let queue: Promise<void> = Promise.resolve();
let saveError: Error | null = null;
let inFlight = false;
let onStatus = (_status: string) => {};
export function observeSaves(fn: (status: string) => void) { onStatus = fn; }

export function scheduleSave(key: string, path: string, data: unknown) {
  pending.set(key, { path, data });
  onStatus('Enregistrement…');
  clearTimeout(timer);
  timer = setTimeout(() => { void flushSaves().catch(() => {}); }, 450);
}

export async function flushSaves() {
  clearTimeout(timer);
  const operation = queue.then(async () => {
    inFlight = true;
    try {
      while (pending.size) {
        const entries = [...pending.entries()];
        pending.clear();
        for (let i = 0; i < entries.length; i++) {
          const [, save] = entries[i];
          try { await api(save.path, save.data); }
          catch (e) {
            for (const [retryKey, retry] of entries.slice(i)) if (!pending.has(retryKey)) pending.set(retryKey, retry);
            saveError = e instanceof Error ? e : new Error(String(e));
            onStatus('Échec de sauvegarde — réessayer');
            throw saveError;
          }
        }
      }
      saveError = null;
      onStatus('Enregistré sur cet appareil');
    } finally {
      inFlight = false;
    }
  });
  queue = operation.catch(() => {});
  await operation;
  if (saveError) throw saveError;
}

window.addEventListener('beforeunload', event => {
  if (pending.size || inFlight || saveError) { event.preventDefault(); void flushSaves().catch(() => {}); }
});

export async function readFile(file: File) {
  if (file.size > 16 * 1024 * 1024) throw new Error('Le fichier dépasse 16 Mo.');
  const bytes = new Uint8Array(await file.arrayBuffer());
  let result = '';
  for (let i = 0; i < bytes.length; i += 8192) result += String.fromCharCode(...bytes.subarray(i, i + 8192));
  return btoa(result);
}

export async function download(file: { filename: string; data: string }) {
  const native = (window as NativeWindow).pywebview;
  if (native) return native.api.save_file(file.filename, file.data);
  const bytes = Uint8Array.from(atob(file.data), c => c.charCodeAt(0));
  const url = URL.createObjectURL(new Blob([bytes], { type: 'application/zip' }));
  const anchor = document.createElement('a');
  anchor.href = url; anchor.download = file.filename; anchor.click();
  setTimeout(() => URL.revokeObjectURL(url), 10_000);
  return true;
}
