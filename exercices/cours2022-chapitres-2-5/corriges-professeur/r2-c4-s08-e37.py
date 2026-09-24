# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S08 · 37 — Planifier hors d’une interruption

def premier_creneau(depart: int, periode: int, pause_debut: int, pause_fin: int) -> int:
    """Retournez la première minute de départ utilisable.
    Précondition : depart >= 0 and periode > 0 and 0 <= pause_debut <= pause_fin
    """
    t: int = ((depart + periode - 1) // periode) * periode
    while pause_debut <= t and t < pause_fin:
        t = t + periode
    return t

# Vérifications
assert premier_creneau(7, 5, 9, 14) == 15
assert premier_creneau(12, 3, 6, 12) == 12
assert premier_creneau(0, 4, 1, 9) == 0
assert premier_creneau(2, 2, 2, 2) == 2
assert premier_creneau(1, 4, 0, 13) == 16
assert premier_creneau(20, 3, 0, 10) == 21
