import Editor, { loader } from '@monaco-editor/react';
import * as monaco from 'monaco-editor/esm/vs/editor/editor.api';
import 'monaco-editor/esm/vs/basic-languages/python/python.contribution';
import EditorWorker from 'monaco-editor/esm/vs/editor/editor.worker?worker';

(self as typeof self & { MonacoEnvironment: unknown }).MonacoEnvironment = { getWorker: () => new EditorWorker() };
loader.config({ monaco });

export function CodeEditor({ value, onChange, height = '360px', readOnly = false, label = 'Code Python' }: { value: string; onChange?: (value: string) => void; height?: string; readOnly?: boolean; label?: string }) {
  return <div className="code-editor" aria-label={label}>
    <Editor height={height} language="python" value={value} onChange={v => onChange?.(v || '')}
      loading={<div className="editor-loading">Chargement de l’éditeur…</div>}
      options={{ ariaLabel: label, readOnly, minimap: { enabled: false }, fontFamily: 'Geist Mono, monospace', fontSize: 13, lineHeight: 23, padding: { top: 18, bottom: 18 }, scrollBeyondLastLine: false, automaticLayout: true, tabSize: 4, insertSpaces: true, wordWrap: 'on', renderLineHighlight: 'gutter', overviewRulerLanes: 0, hideCursorInOverviewRuler: true, quickSuggestions: false, suggestOnTriggerCharacters: false, folding: true, lineNumbersMinChars: 3, contextmenu: false, scrollbar: { verticalScrollbarSize: 7, horizontalScrollbarSize: 7 } }} />
  </div>;
}
