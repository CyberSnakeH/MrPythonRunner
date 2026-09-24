import { useRef, useState } from 'react';
import { ArrowCounterClockwise, Code, Play, Stop, BookOpen, ArrowRight } from '@phosphor-icons/react';
import { CodeEditor } from './CodeEditor';
import { Statement } from './Statement';
import { Results } from './Results';
import { useExecution } from './useExecution';
import { kinds, type Draft, type Exercise, type Pack } from './types';

export function StudentWorkspace({ pack, exercise, draft, student, onDraft, onError }: { pack: Pack; exercise: Exercise; draft: Draft; student: string; onDraft: (draft: Draft) => void; onError: (error: unknown) => void }) {
  const current = useRef(draft);
  current.current = draft;
  const [tab, setTab] = useState<'statement' | 'tests'>('statement');
  const execution = useExecution((report, code) => {
    if (current.current.code === code) onDraft({ ...current.current, report });
  }, onError);
  function reset() { if (confirm('Remplacer votre code par le code de départ ?')) onDraft({ code: exercise.starter, report: null }); }
  return <div className="workspace-grid">
    <section className="statement-panel">
      <div className="panel-tabs"><button className={tab === 'statement' ? 'active' : ''} onClick={() => setTab('statement')}><BookOpen size={16} />Énoncé</button><button className={tab === 'tests' ? 'active' : ''} onClick={() => setTab('tests')}>Exemples de tests</button></div>
      <div className="statement-body">{tab === 'statement' ? <><span className="eyebrow">{kinds[exercise.kind]}</span><Statement text={exercise.statement} assets={pack.assets} /></> : <><h3>Comprendre ce qui est attendu</h3><p className="hint">Ces tests vous aident à vérifier votre solution. D’autres cas peuvent aussi être évalués.</p>{exercise.tests.filter(t => !t.hidden).map(t => <div className="example-test" key={t.id}><strong>{t.label}</strong><pre>{t.code}</pre></div>)}{!exercise.tests.some(t => !t.hidden) && <p className="hint">Le professeur n’a pas publié de test d’exemple.</p>}</>}</div>
      <div className="statement-note"><ArrowRight size={17} /><span>Avancez à votre rythme. Votre code est sauvegardé automatiquement.</span></div>
    </section>
    <section className="coding-panel">
      <div className="editor-toolbar"><span><Code size={17} />solution.py</span><div><span className="language-tag">Python · MrPython</span><button className="icon-button" title="Reprendre le code de départ" aria-label="Reprendre le code de départ" disabled={execution.running} onClick={reset}><ArrowCounterClockwise size={17} /></button></div></div>
      <CodeEditor value={draft.code} onChange={code => onDraft({ code, report: null })} height="clamp(240px, calc(100dvh - 490px), 390px)" />
      <div className="run-toolbar"><span className="hint">Délai maximal : {exercise.timeout} s</span>{execution.running ? <button className="button secondary" onClick={execution.stop}><Stop size={16} weight="fill" />Arrêter</button> : <button className="button primary" onClick={() => void execution.start(pack.id, exercise.id, draft.code, student)}><Play size={16} weight="fill" />Tester mon code</button>}</div>
      <Results report={draft.report} running={execution.running} />
    </section>
  </div>;
}
