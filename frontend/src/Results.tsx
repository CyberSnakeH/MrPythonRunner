import { CheckCircle, XCircle, Clock, TerminalWindow, WarningCircle, LockSimple } from '@phosphor-icons/react';
import type { Report } from './types';

const labels: Record<string, string> = { passed: 'Tous les tests sont réussis', failed: 'Encore un peu de travail', type_error: 'Vérifiez les types de votre code', syntax_error: 'Une erreur de syntaxe à corriger', error: 'L’exécution a rencontré une erreur', timeout: 'Le temps autorisé est dépassé', cancelled: 'Exécution arrêtée', no_tests: 'Aucun test de correction' };

export function Results({ report, running = false, teacher = false }: { report: Report | null; running?: boolean; teacher?: boolean }) {
  if (running) return <section className="results" aria-live="polite"><div className="result-heading"><Clock size={20} /><strong>MrPython vérifie votre code…</strong></div><div className="skeleton" /><div className="skeleton short" /></section>;
  if (!report) return <section className="results empty-results"><TerminalWindow size={22} /><div><strong>Un retour pour avancer</strong><p>Lancez les tests pour voir les résultats et les indications de MrPython.</p></div></section>;
  const good = report.status === 'passed';
  return <section className="results" aria-live="polite">
    <div className={`result-heading ${good ? 'success' : ''}`}>{good ? <CheckCircle size={22} weight="fill" /> : <WarningCircle size={22} />}<strong>{labels[report.status] || report.status}</strong><span className="mono result-score">{report.score} / {report.max_score} pts</span></div>
    {report.status === 'timeout' && <p className="hint">Vérifiez les boucles et leurs conditions d’arrêt. L’exécution a été interrompue.</p>}
    {report.diagnostics.map((d, i) => <div className={`diagnostic ${d.severity}`} key={i}><strong>{d.line ? `Ligne ${d.line} · ` : ''}{d.message}</strong>{d.details && <p>{d.details}</p>}</div>)}
    <div className="test-results">{report.tests.map(test => <div key={test.id} className="test-result"><div>{test.passed ? <CheckCircle className="success" size={18} /> : <XCircle className="failure" size={18} />}<span>{test.label}</span>{test.hidden && <LockSimple size={13} className="muted" />}<small>{test.passed ? 'Réussi' : 'À corriger'}</small></div>{test.error && (!test.hidden || teacher) && <pre>{test.error.file === 'eleve.py' && test.error.line ? `Ligne ${test.error.line} · ` : ''}{test.error.message} : {test.error.details}</pre>}</div>)}</div>
    {report.output && <details className="console-output" open><summary>Sortie du programme</summary><pre>{report.output}</pre></details>}
    <div className="results-footer"><span>{report.passed} / {report.total} tests réussis</span><span className="mono">{report.duration_ms} ms</span></div>
  </section>;
}
