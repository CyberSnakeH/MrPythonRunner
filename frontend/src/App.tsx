import { useEffect, useRef, useState } from 'react';
import { ArrowDown, ArrowUp, BookOpen, Check, CheckCircle, Code, DownloadSimple, FileArrowUp, FolderOpen, GearSix, GraduationCap, Plus, SignOut, Trash, X, Circle, PencilSimple, WarningCircle } from '@phosphor-icons/react';
import { api, download, flushSaves, observeSaves, readFile, scheduleSave } from './api';
import { StudentWorkspace } from './StudentWorkspace';
import { TeacherWorkspace } from './TeacherWorkspace';
import { ReviewWorkspace } from './ReviewWorkspace';
import { Statement } from './Statement';
import { DistributionDialog } from './DistributionDialog';
import { StudentEntry } from './StudentEntry';
import { newExercise, uid, kinds, type Draft, type Exercise, type Pack, type Work } from './types';

export default function App() {
  const [packs, setPacks] = useState<Pack[]>([]);
  const [packId, setPackId] = useState('');
  const [exerciseId, setExerciseId] = useState('');
  const [role, setRole] = useState<'student' | 'teacher'>('student');
  const [student, setStudent] = useState('');
  const [identity, setIdentity] = useState('');
  const [accessPackId, setAccessPackId] = useState('');
  const [distributing, setDistributing] = useState(false);
  const [drafts, setDrafts] = useState<Record<string, Draft>>({});
  const [draftsReady, setDraftsReady] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [notice, setNotice] = useState('');
  const [saveStatus, setSaveStatus] = useState('Enregistré sur cet appareil');
  const [settings, setSettings] = useState(false);
  const [review, setReview] = useState<{ work: Work; matching: boolean } | null>(null);
  const [busy, setBusy] = useState(false);
  const packInput = useRef<HTMLInputElement>(null);
  const workInput = useRef<HTMLInputElement>(null);
  const settingsRef = useRef<HTMLDialogElement>(null);
  const pack = packs.find(p => p.id === packId);
  const exercise = pack?.exercises.find(ex => ex.id === exerciseId);
  const unlocked = !!student && accessPackId === packId;
  const onError = (e: unknown) => { setError(e instanceof Error ? e.message : String(e)); setNotice(''); };

  useEffect(() => {
    observeSaves(setSaveStatus);
    void api<{ packs: Pack[] }>('state').then(data => { setPacks(data.packs); setPackId(data.packs[0]?.id || ''); setExerciseId(data.packs[0]?.exercises[0]?.id || ''); }).catch(onError).finally(() => setLoading(false));
  }, []);
  useEffect(() => {
    let valid = true;
    setDraftsReady(false); setDrafts({});
    if (unlocked && packId && role === 'student') {
      void flushSaves().then(() => api<{ drafts: Record<string, Draft> }>('drafts', { student, pack_id: packId })).then(data => { if (valid) { setDrafts(data.drafts); setDraftsReady(true); } }).catch(onError);
    }
    return () => { valid = false; };
  }, [student, packId, role, unlocked]);
  useEffect(() => { if (settings) settingsRef.current?.showModal(); else settingsRef.current?.close(); }, [settings]);
  useEffect(() => { if (!notice) return; const t = setTimeout(() => setNotice(''), 6500); return () => clearTimeout(t); }, [notice]);
  useEffect(() => { setIdentity(''); }, [packId, role]);

  async function action(fn: () => Promise<void> | void) {
    setError(''); setBusy(true);
    try { await flushSaves(); await fn(); } catch (e) { onError(e); } finally { setBusy(false); }
  }
  function changePack(next: Pack) {
    if (next.assignment || pack?.assignment) return;
    setPacks(prev => prev.map(p => p.id === next.id ? next : p));
    scheduleSave(`pack:${next.id}`, 'pack/save', { pack: next });
  }
  function changeExercise(next: Exercise) { if (pack) changePack({ ...pack, exercises: pack.exercises.map(ex => ex.id === next.id ? next : ex) }); }
  function selectPack(id: string) { void action(() => { setAccessPackId(''); setPackId(id); setExerciseId(packs.find(p => p.id === id)?.exercises[0]?.id || ''); setReview(null); }); }
  function changeDraft(next: Draft) {
    if (!pack || !exercise) return;
    setDrafts(prev => ({ ...prev, [exercise.id]: next }));
    scheduleSave(`draft:${student}:${pack.id}:${exercise.id}`, 'draft/save', { student, pack_id: pack.id, exercise_id: exercise.id, code: next.code });
  }
  async function login() {
    const id = identity.trim();
    if (!id) return;
    if (!pack) return;
    const result = await api<{ student: string }>('student/open', { pack_id: pack.id, student: id });
    setStudent(result.student); setAccessPackId(pack.id); setIdentity('');
  }
  async function createPack() {
    const next: Pack = { format: 'mrpython-pack', version: 1, id: uid(), title: 'Ma nouvelle série', description: '', author: '', exercises: [newExercise()], assets: {} };
    await api('pack/save', { pack: next }); setPacks(prev => [next, ...prev]); setPackId(next.id); setExerciseId(next.exercises[0].id); setReview(null); setSettings(true);
  }
  function addExercise() { if (pack) { const next = newExercise(); changePack({ ...pack, exercises: [...pack.exercises, next] }); setExerciseId(next.id); } }
  function moveExercise(delta: number) {
    if (!pack || !exercise) return;
    const list = [...pack.exercises]; const index = list.findIndex(ex => ex.id === exercise.id);
    if (index + delta < 0 || index + delta >= list.length) return;
    [list[index], list[index + delta]] = [list[index + delta], list[index]];
    changePack({ ...pack, exercises: list });
  }
  function deleteExercise() {
    if (!pack || !exercise || !confirm(`Supprimer l’exercice « ${exercise.title} » de cette série ?`)) return;
    const list = pack.exercises.filter(ex => ex.id !== exercise.id);
    changePack({ ...pack, exercises: list }); setExerciseId(list[0]?.id || '');
  }
  async function importPack(file?: File) {
    if (!file) return;
    const data = await readFile(file);
    let response = await api<{ pack?: Pack; conflict?: boolean; title?: string }>('pack/import', { data });
    if (response.conflict) {
      if (!confirm(`Une autre version de « ${response.title} » est déjà enregistrée. La remplacer par le fichier importé ? Les réponses restent sauvegardées.`)) return;
      response = await api('pack/import', { data, replace: true });
    }
    const next = response.pack!;
    setPacks(prev => [next, ...prev.filter(p => p.id !== next.id)]); setPackId(next.id); setExerciseId(next.exercises[0]?.id || ''); setReview(null);
    setAccessPackId(''); setStudent(''); setIdentity(''); setDrafts({}); setDraftsReady(false);
    if (next.assignment) setRole('student');
    setNotice(next.assignment ? 'Série chargée. Saisissez l’identifiant communiqué par votre professeur.' : 'Modèle chargé. Vous pouvez le préparer dans l’espace professeur.');
  }
  async function importWork(file?: File) {
    if (!file) return;
    const data = await readFile(file);
    if (role === 'student' && !unlocked) throw new Error('Entrez votre identifiant avant de reprendre vos réponses.');
    const loaded = await api<{ work: Work; matching: boolean; pack_id: string }>('work/import', { data, purpose: role === 'student' ? 'restore' : 'review', student });
    if (role === 'teacher') { setPackId(loaded.pack_id); setReview(loaded); }
    else {
      if (loaded.pack_id !== packId) throw new Error('Chargez d’abord la série correspondant à ce fichier de réponses et entrez votre identifiant.');
      if (!confirm(`Reprendre les réponses de « ${loaded.work.student} » ? Cela remplacera ses brouillons pour cette série sur cet appareil.`)) return;
      await api('work/restore', { data, student });
      const p = packs.find(p => p.id === loaded.work.pack_id); setExerciseId(p?.exercises[0]?.id || '');
      const response = await api<{ drafts: Record<string, Draft> }>('drafts', { student: loaded.work.student, pack_id: loaded.work.pack_id });
      setDrafts(response.drafts); setDraftsReady(true); setNotice('Réponses restaurées. Relancez les tests pour vérifier les résultats.');
    }
  }
  async function exportFile(kind: 'work/export' | 'pack/export' | 'pack/backup', recipient?: string) {
    if (!pack) return;
    const result = await api<{ filename: string; data: string }>(kind, { pack_id: pack.id, student: recipient ?? student });
    if (await download(result)) { setDistributing(false); setNotice(kind === 'pack/export' ? `Fichier exporté pour l’élève « ${recipient} ».` : kind === 'pack/backup' ? 'Modèle professeur sauvegardé.' : 'Les réponses ont été exportées. Vous pouvez les remettre à votre professeur.'); }
  }

  const passed = pack?.exercises.filter(ex => drafts[ex.id]?.report?.status === 'passed').length || 0;
  const score = Math.round((pack?.exercises.reduce((sum, ex) => sum + (drafts[ex.id]?.report?.score || 0), 0) || 0) * 100) / 100;
  return <div className="app-shell">
    <aside className="sidebar"><div className="brand"><span className="brand-mark"><Code size={23} weight="bold" /></span><div>MrPython<span>RUNNER</span></div></div>
      <div className="library-label"><span className="eyebrow">VOTRE ATELIER</span><span className="local-dot" title="Fonctionne sans connexion" /></div>
      <label className="sr-only" htmlFor="pack-select">Série d’exercices</label><select id="pack-select" className="pack-select" value={packId} onChange={e => selectPack(e.target.value)} disabled={busy || loading}>{!packs.length && <option value="">Aucune série</option>}{packs.map(p => <option key={p.id} value={p.id}>{p.title}{p.assignment ? ' · Fichier élève' : ' · Modèle professeur'}</option>)}</select>
      <div className="sidebar-actions"><button className="button secondary" disabled={busy} onClick={() => packInput.current?.click()}><FolderOpen size={17} />Charger une série</button>{role === 'teacher' && <button className="button text-button" disabled={busy} onClick={() => void action(createPack)}><Plus size={16} />Créer une série</button>}</div>
      <div className="exercise-list-heading"><span className="eyebrow">EXERCICES</span><span className="mono">{pack?.exercises.length || 0}</span></div>
      <nav className="exercise-list" aria-label="Exercices de la série">{(role === 'teacher' || unlocked) && pack?.exercises.map((ex, index) => <button key={ex.id} className={ex.id === exerciseId && !review ? 'selected' : ''} onClick={() => void action(() => { setExerciseId(ex.id); setReview(null); })}><span className="exercise-number mono">{String(index + 1).padStart(2, '0')}</span><span className="exercise-label">{ex.title}<small>{ex.points} points · {kinds[ex.kind]}</small></span>{role === 'student' && (drafts[ex.id]?.report?.status === 'passed' ? <CheckCircle size={18} weight="fill" className="success" /> : <Circle size={15} className="muted" />)}</button>)}</nav>
      {role === 'teacher' && pack && !pack.assignment && <button className="button add-exercise" onClick={addExercise}><Plus size={17} />Ajouter un exercice</button>}
      <div className="sidebar-bottom">{role === 'student' && unlocked && pack && <div className="progress-summary"><div><span>Votre progression</span><strong className="mono">{passed}/{pack.exercises.length}</strong></div><progress value={passed} max={Math.max(1, pack.exercises.length)} /><small>{score} points obtenus · continuez à votre rythme</small></div>}<div className="offline-label"><span className="local-dot" /><span>Local. Hors ligne. À votre rythme.</span></div></div>
    </aside>
    <div className="main-shell"><header className="topbar"><div className="role-switch" aria-label="Espace de travail"><button className={role === 'student' ? 'active' : ''} onClick={() => void action(() => { setRole('student'); setAccessPackId(''); setReview(null); })}><GraduationCap size={18} />Élève</button><button className={role === 'teacher' ? 'active' : ''} onClick={() => void action(() => { setRole('teacher'); setAccessPackId(''); setReview(null); })}><PencilSimple size={17} />Professeur</button></div><div className="topbar-right"><button className={`save-indicator ${saveStatus.startsWith('Échec') ? 'failure' : ''}`} onClick={() => void action(() => {})}><Check size={14} />{saveStatus}</button>{unlocked && role === 'student' && <div className="identity-chip"><span>{student.slice(0, 2).toUpperCase()}</span><strong>{student}</strong><button className="icon-button" title="Changer d’identifiant" aria-label="Changer d’identifiant" onClick={() => void action(() => { setStudent(''); setAccessPackId(''); localStorage.removeItem('runner-student'); setIdentity(''); })}><SignOut size={16} /></button></div>}</div></header>
      <main>
        {error && <div className="notification error" role="alert"><WarningCircle size={20} /><span>{error}</span><button className="icon-button" aria-label="Fermer l’erreur" onClick={() => setError('')}><X size={16} /></button></div>}
        {notice && <div className="notification" role="status"><CheckCircle size={20} /><span>{notice}</span><button className="icon-button" aria-label="Fermer la notification" onClick={() => setNotice('')}><X size={16} /></button></div>}
        {loading ? <div className="loading-page"><div className="skeleton" /><div className="skeleton short" /><p>Ouverture de votre atelier…</p></div> : !pack ? <div className="empty-state"><BookOpen size={42} /><h1>Votre prochain exercice commence ici.</h1><p>Chargez une série transmise par votre professeur, ou créez-en une dans l’espace professeur.</p><button className="button primary" onClick={() => packInput.current?.click()}><FolderOpen size={18} />Charger une série</button></div> : role === 'student' && !unlocked ? <StudentEntry pack={pack} identity={identity} busy={busy} onIdentity={setIdentity} onStart={() => void action(login)} /> : role === 'teacher' && pack.assignment ? <section className="empty-state"><BookOpen size={42} /><h1>Ce fichier est une copie élève.</h1><p>Les exercices attribués sont en lecture seule. Pour les modifier ou distribuer la série à un autre élève, ouvrez votre modèle professeur.</p><button className="button secondary" onClick={() => packInput.current?.click()}><FolderOpen size={18} />Charger le modèle professeur</button></section> : review && role === 'teacher' ? <ReviewWorkspace key={`${review.work.student}:${review.work.exported}`} pack={pack} {...review} onClose={() => setReview(null)} onError={onError} /> : <>
          <div className="breadcrumb"><span>{role === 'teacher' ? 'Espace professeur' : 'Mon parcours'}</span><span>/</span><span>{pack.title}</span></div>
          <div className="page-heading"><div><div className="eyebrow">{role === 'teacher' ? 'PRÉPARER & TRANSMETTRE' : `EXERCICE ${String(pack.exercises.findIndex(ex => ex.id === exerciseId) + 1).padStart(2, '0')}`}</div><h1>{exercise?.title || pack.title}</h1><p>{role === 'teacher' ? 'Créez le cadre. Laissez les élèves trouver le chemin.' : `${kinds[exercise?.kind || 'function']} · ${exercise?.points || 0} points`}</p></div><div className="page-actions">{role === 'teacher' ? <><button className="button secondary" title="Paramètres de la série" onClick={() => setSettings(true)}><GearSix size={17} /><span>Série</span></button><button className="button secondary" onClick={() => workInput.current?.click()}><FileArrowUp size={17} />Ouvrir une copie</button><button className="button primary" disabled={busy} onClick={() => setDistributing(true)}><DownloadSimple size={17} />Distribuer à un élève</button></> : <><button className="button secondary" onClick={() => workInput.current?.click()}><FileArrowUp size={17} /><span>Reprendre</span></button><button className="button secondary" disabled={busy} onClick={() => void action(() => exportFile('work/export'))}><DownloadSimple size={17} />Rendre mes réponses</button></>}</div></div>
          {pack.description && <details className="series-instructions"><summary>Consignes de la série{pack.author ? ` · ${pack.author}` : ''}</summary><Statement text={pack.description} assets={pack.assets} /></details>}
          {role === 'teacher' && exercise && <div className="exercise-management"><span>Position {pack.exercises.findIndex(ex => ex.id === exercise.id) + 1} sur {pack.exercises.length}</span><button className="icon-button" disabled={pack.exercises[0].id === exercise.id} aria-label="Déplacer l’exercice vers le haut" onClick={() => moveExercise(-1)}><ArrowUp size={15} /></button><button className="icon-button" disabled={pack.exercises.at(-1)?.id === exercise.id} aria-label="Déplacer l’exercice vers le bas" onClick={() => moveExercise(1)}><ArrowDown size={15} /></button><button className="button text-button" onClick={deleteExercise}><Trash size={15} />Supprimer l’exercice</button></div>}
          {!exercise ? <div className="empty-state"><BookOpen size={34} /><h2>La série attend son premier exercice.</h2>{role === 'teacher' && <button className="button primary" onClick={addExercise}><Plus size={17} />Ajouter un exercice</button>}</div> : role === 'teacher' ? <TeacherWorkspace key={exercise.id} pack={pack} exercise={exercise} onChange={changeExercise} onAssets={(assets, statement) => changePack({ ...pack, assets, exercises: pack.exercises.map(ex => ex.id === exercise.id ? { ...ex, statement } : ex) })} onError={onError} /> : draftsReady ? <StudentWorkspace key={`${student}:${pack.id}:${exercise.id}`} pack={pack} exercise={exercise} student={student} draft={drafts[exercise.id] || { code: exercise.starter, report: null }} onDraft={changeDraft} onError={onError} /> : <div className="loading-page"><div className="skeleton" /><p>Chargement de vos réponses…</p></div>}
          <footer className="page-footer"><span>MrPython Runner <span className="mono">0.1</span></span><span>Comprendre, essayer, progresser.</span></footer>
        </>}
      </main>
    </div>
    <input ref={packInput} type="file" accept=".mrpack" hidden onChange={e => { const file = e.target.files?.[0]; e.target.value = ''; void action(() => importPack(file)); }} />
    <input ref={workInput} type="file" accept=".mrwork" hidden onChange={e => { const file = e.target.files?.[0]; e.target.value = ''; void action(() => importWork(file)); }} />
    {distributing && pack && !pack.assignment && <DistributionDialog title={pack.title} busy={busy} error={error} onClose={() => setDistributing(false)} onExport={id => void action(() => exportFile('pack/export', id))} onBackup={() => void action(() => exportFile('pack/backup'))} />}
    <dialog ref={settingsRef} onCancel={() => setSettings(false)} onClick={e => { if (e.target === e.currentTarget) setSettings(false); }}><div className="dialog-content"><div className="section-heading"><h2>Votre série d’exercices</h2><button className="icon-button" aria-label="Fermer les paramètres" onClick={() => setSettings(false)}><X size={20} /></button></div>{pack && !pack.assignment && <><label>Titre de la série<input value={pack.title} maxLength={200} onChange={e => changePack({ ...pack, title: e.target.value })} /></label><label>Auteur ou établissement<input value={pack.author} maxLength={200} onChange={e => changePack({ ...pack, author: e.target.value })} /></label><label>Description et consignes générales<textarea rows={5} value={pack.description} maxLength={20000} onChange={e => changePack({ ...pack, description: e.target.value })} /></label><p className="hint">L’export contient les énoncés, les images, le code de départ et les tests. Les réponses des élèves sont enregistrées séparément.</p><button className="button primary" onClick={() => void action(() => setSettings(false))}><Check size={17} />Enregistrer et fermer</button></>}</div></dialog>
  </div>;
}
