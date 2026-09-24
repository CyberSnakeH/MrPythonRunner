# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S09 · 45 — Deux robots se rapprochent

def rencontre_robots(gauche: int, droite: int) -> int:
    """Retournez le nombre de tours nécessaires pour que le robot gauche rejoigne ou dépasse l’autre.
    Précondition : gauche <= droite
    """
    a: int = gauche
    b: int = droite
    tours: int = 0
    while a < b:
        a = a + 2
        b = b - 1
        tours = tours + 1
    return tours

# Vérifications
assert rencontre_robots(0, 7) == 3
assert rencontre_robots(4, 4) == 0
assert rencontre_robots(-5, 1) == 2
assert rencontre_robots(0, 1) == 1
assert rencontre_robots(0, 3) == 1
assert rencontre_robots(10, 14) == 2
