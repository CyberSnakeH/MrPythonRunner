# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S08 · 38 — Regrouper les cycles identiques

def energie_veille(duree: int, cycle: int) -> int:
    """Calculez l’énergie totale consommée pendant la durée demandée.
    Précondition : duree >= 0 and cycle >= 1
    """
    complets: int = duree // cycle
    reste: int = duree % cycle
    total: int = complets * (8 + 2 * (cycle - 1))
    if reste > 0:
        total = total + 8 + 2 * (reste - 1)
    return total

# Vérifications
assert energie_veille(7, 3) == 32
assert energie_veille(2, 5) == 10
assert energie_veille(0, 3) == 0
assert energie_veille(4, 1) == 32
assert energie_veille(6, 3) == 24
assert energie_veille(1, 1) == 8
assert energie_veille(1000000, 10) == 2600000
