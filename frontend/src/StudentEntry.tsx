import { ArrowRight, BookOpen } from '@phosphor-icons/react';
import type { Pack } from './types';

export function StudentEntry({ pack, identity, busy, onIdentity, onStart }: {
  pack: Pack; identity: string; busy: boolean;
  onIdentity: (value: string) => void; onStart: () => void;
}) {
  if (!pack.assignment) return <section className="welcome">
    <span className="eyebrow">FICHIER NON ATTRIBUÉ</span>
    <h1>Ce fichier est un modèle professeur.</h1>
    <p>Aucun identifiant élève n’a été attribué à cette série. Vous ne pouvez pas la commencer dans l’espace élève.</p>
    <p>Demandez votre fichier personnel à votre professeur, puis utilisez « Charger une série ». Le professeur doit ouvrir son modèle, cliquer sur « Distribuer à un élève », saisir votre identifiant et exporter le fichier.</p>
    <div className="welcome-pack"><BookOpen size={23} /><div><strong>{pack.title}</strong><span>En attente d’une attribution par le professeur</span></div></div>
  </section>;
  return <section className="welcome">
    <span className="eyebrow">AVANT DE COMMENCER LA SÉRIE</span>
    <h1>Entrez l’identifiant fourni par votre professeur.</h1>
    <p>Votre fichier est chargé. Saisissez le numéro d’identifiant que votre professeur vous a communiqué pour accéder aux exercices et tester votre code.</p>
    <form autoComplete="off" onSubmit={e => { e.preventDefault(); onStart(); }}>
      <label htmlFor="student-id">Identifiant fourni par le professeur</label>
      <div className="login-row">
        <input id="student-id" type="text" autoComplete="off" autoCapitalize="none" spellCheck={false}
          placeholder="Saisissez votre identifiant" value={identity} maxLength={80}
          onChange={e => onIdentity(e.target.value)} disabled={busy} autoFocus required />
        <button className="button primary" disabled={busy || !identity.trim()}>Commencer la série<ArrowRight size={18} /></button>
      </div>
      <small>Recopiez exactement votre identifiant, y compris les éventuels zéros au début. Un identifiant incorrect ne permet pas de commencer.</small>
    </form>
    <div className="welcome-pack"><BookOpen size={23} /><div><strong>{pack.title}</strong><span>{pack.exercises.length} exercices · {pack.exercises.reduce((sum, ex) => sum + ex.points, 0)} points</span></div></div>
  </section>;
}
