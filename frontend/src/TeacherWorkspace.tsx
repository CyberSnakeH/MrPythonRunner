import { useRef, useState } from 'react';
import { Image, Plus, Trash, Eye, Code, FileText, Flask, Play, Stop } from '@phosphor-icons/react';
import { CodeEditor } from './CodeEditor';
import { Statement } from './Statement';
import { Results } from './Results';
import { readFile } from './api';
import { useExecution } from './useExecution';
import { kinds, uid, type Exercise, type Pack, type Report } from './types';

export function TeacherWorkspace({ pack, exercise, onChange, onAssets, onError }: { pack: Pack; exercise: Exercise; onChange: (exercise: Exercise) => void; onAssets: (assets: Record<string, string>, statement: string) => void; onError: (error: unknown) => void }) {
  const [tab, setTab] = useState('statement');
  const [trialCode, setTrialCode] = useState(exercise.starter);
  const [report, setReport] = useState<Report | null>(null);
  const imageInput = useRef<HTMLInputElement>(null);
  const trialRef = useRef(trialCode);
  trialRef.current = trialCode;
  const execution = useExecution((result, code) => { if (trialRef.current === code) setReport(result); }, onError);
  const patch = (value: Partial<Exercise>) => { setReport(null); onChange({ ...exercise, ...value }); };
  const addImage = async (file?: File) => {
    if (!file) return;
    try {
      const ext = file.name.split('.').pop()?.toLowerCase();
      if (!ext || !['png', 'jpg', 'jpeg', 'webp', 'gif'].includes(ext)) throw new Error('Choisissez une image PNG, JPEG, GIF ou WebP.');
      if (file.size > 4 * 1024 * 1024) throw new Error('Une image ne doit pas dépasser 4 Mo.');
      const name = `assets/${uid()}.${ext}`;
      const data = await readFile(file);
      onAssets({ ...pack.assets, [name]: data }, `${exercise.statement}\n\n![Illustration](${name})\n`);
    } catch (e) { onError(e); }
  };
  return <section className="teacher-workspace">
    <div className="panel-tabs teacher-tabs">
      <button disabled={execution.running} className={tab === 'statement' ? 'active' : ''} onClick={() => setTab('statement')}><FileText size={17} />Énoncé</button>
      <button disabled={execution.running} className={tab === 'code' ? 'active' : ''} onClick={() => setTab('code')}><Code size={17} />Code de départ</button>
      <button disabled={execution.running} className={tab === 'tests' ? 'active' : ''} onClick={() => setTab('tests')}><Flask size={17} />Tests & barème<span className="count">{exercise.tests.length}</span></button>
      <button disabled={execution.running} className={tab === 'preview' ? 'active' : ''} onClick={() => setTab('preview')}><Eye size={17} />Essayer l’exercice</button>
    </div>
    {tab === 'statement' && <div className="author-split">
      <div className="author-form"><span className="eyebrow">CONSTRUIRE L’EXERCICE</span><label>Titre<input value={exercise.title} maxLength={200} onChange={e => patch({ title: e.target.value })} /></label>
        <label>Type d’exercice<select value={exercise.kind} onChange={e => patch({ kind: e.target.value as Exercise['kind'] })}>{Object.entries(kinds).map(([key, label]) => <option key={key} value={key}>{label}</option>)}</select></label>
        <div className="field-heading"><label htmlFor="statement-text">Énoncé en Markdown</label><button className="button text-button" onClick={() => imageInput.current?.click()}><Image size={16} />Image</button></div>
        <input ref={imageInput} hidden type="file" accept="image/png,image/jpeg,image/webp,image/gif" onChange={e => { void addImage(e.target.files?.[0]); e.target.value = ''; }} />
        <textarea id="statement-text" className="markdown-input" value={exercise.statement} maxLength={100000} onChange={e => patch({ statement: e.target.value })} spellCheck={false} />
        <p className="hint">Titres avec <code>##</code>, code entre trois accents graves. Formules : <code>$x^2$</code> ou <code>$$…$$</code>. Schémas : un bloc de code marqué <code>tikz</code>, contenant votre <code>tikzpicture</code>.</p>
      </div>
      <div className="author-preview"><span className="eyebrow">APERÇU ÉLÈVE · EN DIRECT</span><Statement text={exercise.statement} assets={pack.assets} /></div>
    </div>}
    {tab === 'code' && <div className="author-content"><h3>Le point de départ des élèves</h3><p className="hint">Définissez la signature et les indications utiles. Ce code sera proposé à l’ouverture de l’exercice.</p><div className="editor-frame"><div className="editor-toolbar"><span><Code size={17} />solution.py</span><span className="language-tag">Python</span></div><CodeEditor label="Code de départ de l’exercice" value={exercise.starter} onChange={starter => patch({ starter })} height="420px" /></div></div>}
    {tab === 'tests' && <div className="author-content"><div className="section-heading"><div><h3>Ce qui valide une solution</h3><p className="hint">Chaque test s’exécute avec un nouveau contexte. Les points sont répartis à parts égales entre les tests.</p></div><button className="button secondary" onClick={() => patch({ tests: [...exercise.tests, { id: uid(), label: `Test ${exercise.tests.length + 1}`, code: 'assert solution(0) == 0', hidden: false }] })}><Plus size={16} />Ajouter un test</button></div>
      <div className="settings-row"><label>Barème (points)<input type="number" min="0.1" max="1000" step="0.5" value={exercise.points} onChange={e => patch({ points: Math.max(0.1, Math.min(1000, Number(e.target.value) || 1)) })} /></label><label>Délai total (secondes)<input type="number" min="1" max="30" value={exercise.timeout} onChange={e => patch({ timeout: Math.max(1, Math.min(30, Number(e.target.value) || 5)) })} /></label></div>
      {!exercise.tests.length && <div className="empty-state compact"><Flask size={30} /><h3>Ajoutez votre premier test</h3><p>Un test contient au moins une instruction <code>assert</code>. Il est nécessaire pour exporter la série.</p></div>}
      {exercise.tests.map((test, index) => <div className="test-author" key={test.id}><div className="test-author-heading"><span className="test-number mono">{String(index + 1).padStart(2, '0')}</span><label className="sr-only" htmlFor={`test-${test.id}`}>Nom du test {index + 1}</label><input id={`test-${test.id}`} value={test.label} onChange={e => patch({ tests: exercise.tests.map(t => t.id === test.id ? { ...t, label: e.target.value } : t) })} /><label className="checkbox-label"><input type="checkbox" checked={test.hidden} onChange={e => patch({ tests: exercise.tests.map(t => t.id === test.id ? { ...t, hidden: e.target.checked } : t) })} />Masquer dans l’interface</label><button className="icon-button" aria-label={`Supprimer ${test.label}`} onClick={() => { if (confirm(`Supprimer le test « ${test.label} » ?`)) patch({ tests: exercise.tests.filter(t => t.id !== test.id) }); }}><Trash size={17} /></button></div><CodeEditor label={`Code du test ${index + 1}`} height="130px" value={test.code} onChange={code => patch({ tests: exercise.tests.map(t => t.id === test.id ? { ...t, code } : t) })} /></div>)}
      <p className="info-note">Les tests masqués restent présents dans le fichier distribué. Pour une évaluation, gardez une copie professeur avec des tests supplémentaires et recalculez les notes sur les réponses reçues.</p>
    </div>}
    {tab === 'preview' && <div className="author-split"><div className="author-preview"><span className="eyebrow">ÉNONCÉ</span><Statement text={exercise.statement} assets={pack.assets} /></div><div className="trial-panel"><div className="editor-toolbar"><span><Code size={17} />Solution d’essai</span><span className="language-tag">Non distribuée</span></div><CodeEditor value={trialCode} onChange={code => { setTrialCode(code); setReport(null); }} height="340px" /><div className="run-toolbar"><span className="hint">Ce code reste dans cet aperçu.</span><button className="button primary" onClick={() => execution.running ? execution.stop() : void execution.start(pack.id, exercise.id, trialCode)}>{execution.running ? <Stop size={16} /> : <Play size={16} />}{execution.running ? 'Arrêter' : 'Vérifier les tests'}</button></div><Results report={report} running={execution.running} teacher /></div></div>}
  </section>;
}
