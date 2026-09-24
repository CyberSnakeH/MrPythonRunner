# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S04 · 17 — Des missions de plus en plus coûteuses

def batterie_missions(charge: int, missions: int) -> int:
    """Retournez la charge restante après toutes les missions.
    Précondition : missions >= 0 and charge >= missions * (missions + 1) // 2
    """
    reste: int = charge
    k: int = 1
    while k <= missions:
        reste = reste - k
        k = k + 1
    return reste

# Vérifications
assert batterie_missions(20, 3) == 14
assert batterie_missions(8, 0) == 8
assert batterie_missions(0, 0) == 0
assert batterie_missions(10, 4) == 0
assert batterie_missions(7, 1) == 6
assert batterie_missions(100, 5) == 85
