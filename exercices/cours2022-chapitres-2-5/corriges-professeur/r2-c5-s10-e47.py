# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S10 · 47 — Un badge quand un nom manque

def initiales_badge(prenom: str, nom: str) -> str:
    """Retournez les initiales disponibles, chacune suivie d’un point.
    """
    resultat: str = ""
    if len(prenom) > 0:
        resultat = resultat + prenom[0] + "."
    if len(nom) > 0:
        resultat = resultat + nom[0] + "."
    return resultat

# Vérifications
assert initiales_badge('Alice', 'Durand') == 'A.D.'
assert initiales_badge('', 'Lee') == 'L.'
assert initiales_badge('', '') == ''
assert initiales_badge('Éva', '') == 'É.'
assert initiales_badge('bob', 'li') == 'b.l.'
assert initiales_badge('A', 'B') == 'A.B.'
