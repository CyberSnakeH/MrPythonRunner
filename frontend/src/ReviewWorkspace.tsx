import { useEffect, useRef, useState } from 'react';
import { ArrowLeft, CheckCircle, Play, Stop, FileCode } from '@phosphor-icons/react';
import { api, flushSaves } from './api';
import { CodeEditor } from './CodeEditor';
import { Results } from './Results';
import type { Pack, Report, Work } from './types';

export function ReviewWorkspace({ pack, work, matching, onClose, onError }: { pack: Pack; work: Work; matching: boolean; onClose: () => void; onError: (error: unknown) => void }) {
  const [selected, setSelected] = useState(work.answers[0]?.exercise_id || '');
  const [reports, setReports] = useState<Record<string, Report>>({});
  const [active, setActive] = useState('');
  const cancelled = useRef(false);
  const mounted = useRef(true);
  const job = useRef('');
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; cancelled.current = true; if (job.current) void api('jobs/cancel', { id: job.current }).catch(() => {}); }; }, []);
  const stop = () => { cancelled.current = true; if (job.current) void api('jobs/cancel', { id: job.current }).catch(onError); };
  async function regrade() {
    cancelled.current = false;
    setActive('preparing');
    try {
      await flushSaves();
      for (const answer of work.answers) {
        if (cancelled.current || !mounted.current) break;
        if (!pack.exercises.some(ex => ex.id === answer.exercise_id)) continue;
        setActive(answer.exercise_id);
        const response = await api<{ id: string }>('jobs/start', { pack_id: pack.id, exercise_id: answer.exercise_id, code: answer.code });
        job.current = response.id;
        if (cancelled.current || !mounted.current) { await api('jobs/cancel', { id: response.id }); break; }
        while (mounted.current) {
          const result = await api<{ state: string; report: Report }>('jobs/get', { id: response.id });
          if (result.state === 'done') { setReports(prev => ({ ...prev, [answer.exercise_id]: result.report })); break; }
          await new Promise(resolve => setTimeout(resolve, 180));
        }
        job.current = '';
      }
    } catch (e) { if (mounted.current) onError(e); }
    finally { if (mounted.current) setActive(''); }
  }
  const answer = work.answers.find(a => a.exercise_id === selected);
  const total = Math.round(Object.values(reports).reduce((sum, r) => sum + r.score, 0) * 100) / 100;
  return <section className="review-workspace"><div className="section-heading"><div><button className="button text-button" onClick={onClose}><ArrowLeft size={16} />Retour à la série</button><h2>La copie de {work.student}</h2><p className="hint">Les résultats contenus dans une copie ne font pas foi. Relancez la correction avec vos propres tests.</p></div><button className="button primary" onClick={() => active ? stop() : void regrade()}>{active ? <Stop size={16} /> : <Play size={16} />}{active ? 'Arrêter' : 'Recalculer les notes'}</button></div>
    {!matching && <p className="info-note">La série a été modifiée depuis ce rendu. La correction utilisera les exercices et tests actuellement ouverts.</p>}
    <div className="review-grid"><div className="review-list">{work.answers.map(a => <button className={a.exercise_id === selected ? 'selected' : ''} key={a.exercise_id} onClick={() => setSelected(a.exercise_id)}><FileCode size={18} /><span>{pack.exercises.find(ex => ex.id === a.exercise_id)?.title || 'Exercice absent de cette série'}<small>{reports[a.exercise_id] ? `${reports[a.exercise_id].score} / ${reports[a.exercise_id].max_score} pts` : 'À vérifier'}</small></span>{reports[a.exercise_id]?.status === 'passed' && <CheckCircle size={16} className="success" />}</button>)}<div className="review-total"><span>Total recalculé</span><strong>{total} / {pack.exercises.reduce((sum, ex) => sum + ex.points, 0)} pts</strong><small>{Object.keys(reports).length} / {pack.exercises.length} exercices vérifiés</small></div></div><div className="review-code">{answer ? <><div className="editor-toolbar"><span>Réponse de l’élève</span><span className="language-tag">Lecture seule</span></div><CodeEditor value={answer.code} readOnly height="360px" /><Results report={reports[selected] || null} running={active === selected} teacher /></> : <div className="empty-state">Ce fichier ne contient aucune réponse.</div>}</div></div>
  </section>;
}
