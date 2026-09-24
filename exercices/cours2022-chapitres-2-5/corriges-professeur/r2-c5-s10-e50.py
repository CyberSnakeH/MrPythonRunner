# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S10 · 50 — Remplir une cellule de largeur fixe

def ligne_tableau(texte: str, largeur: int) -> str:
    """Retournez une cellule encadrée et complétée à droite.
    Précondition : largeur >= len(texte)
    """
    resultat: str = "|" + texte
    i: int
    for i in range(len(texte), largeur):
        resultat = resultat + "_"
    return resultat + "|"

# Vérifications
assert ligne_tableau('chat', 6) == '|chat__|'
assert ligne_tableau('', 0) == '||'
assert ligne_tableau('abc', 3) == '|abc|'
assert ligne_tableau('', 3) == '|___|'
assert ligne_tableau('a b', 4) == '|a b_|'
assert ligne_tableau('é', 2) == '|é_|'
