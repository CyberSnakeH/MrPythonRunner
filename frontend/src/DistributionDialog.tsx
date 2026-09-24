import { useEffect, useRef, useState } from 'react';
import { DownloadSimple, X } from '@phosphor-icons/react';

export function DistributionDialog({ title, busy, error, onClose, onExport, onBackup }: { title: string; busy: boolean; error: string; onClose: () => void; onExport: (student: string) => void; onBackup: () => void }) {
  const ref = useRef<HTMLDialogElement>(null);
  const [student, setStudent] = useState('');
  useEffect(() => { ref.current?.showModal(); }, []);
  return <dialog ref={ref} onCancel={onClose}><div className="dialog-content">
    <div className="section-heading"><h2>Distribuer à un élève</h2><button className="icon-button" aria-label="Fermer la distribution" disabled={busy} onClick={onClose}><X size={20} /></button></div>
    <p>Vous distribuez la série <strong>{title}</strong>.</p>
    {error && <p className="notification error" role="alert">{error}</p>}
    <form onSubmit={e => { e.preventDefault(); onExport(student.trim()); }}>
      <label htmlFor="recipient-id">Identifiant de l’élève<input id="recipient-id" value={student} maxLength={80} onChange={e => setStudent(e.target.value)} placeholder="Ex. : 01234" autoFocus required disabled={busy} /></label>
      <p className="hint">Cet identifiant sera inclus dans le fichier. L’élève devra saisir exactement le même pour accéder à tous les exercices. Les zéros initiaux et les majuscules sont conservés.</p>
      <button className="button primary" disabled={busy || !student.trim()}><DownloadSimple size={17} />Exporter le fichier élève</button>
    </form>
    <p className="hint">Exportez un fichier par élève. Votre modèle reste disponible pour préparer la série et corriger les réponses.</p>
    <button className="button secondary" disabled={busy} onClick={onBackup}><DownloadSimple size={17} />Sauvegarder le modèle professeur</button>
  </div></dialog>;
}
