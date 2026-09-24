# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S05 · 21 — Atteindre le financement de la sortie

def jours_collecte(initial: int, objectif: int, premier_gain: int) -> int:
    """Retournez le premier nombre de jours permettant d’atteindre l’objectif.
    Précondition : initial >= 0 and objectif >= 0 and premier_gain > 0
    """
    somme: int = initial
    gain: int = premier_gain
    jours: int = 0
    while somme < objectif:
        somme = somme + gain
        gain = gain + 1
        jours = jours + 1
    return jours

# Vérifications
assert jours_collecte(10, 20, 3) == 3
assert jours_collecte(30, 20, 2) == 0
assert jours_collecte(0, 1, 1) == 1
assert jours_collecte(0, 6, 1) == 3
assert jours_collecte(2, 2, 5) == 0
assert jours_collecte(1, 12, 4) == 3
