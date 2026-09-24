# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S06 · 28 — Deux navettes au même arrêt

def passages_communs(periode_a: int, periode_b: int, fin: int) -> int:
    """Comptez les instants où les deux navettes passent ensemble.
    Précondition : periode_a > 0 and periode_b > 0 and fin >= 0
    """
    minute: int = 1
    compte: int = 0
    while minute <= fin:
        if minute % periode_a == 0 and minute % periode_b == 0:
            compte = compte + 1
        minute = minute + 1
    return compte

# Vérifications
assert passages_communs(2, 3, 12) == 2
assert passages_communs(2, 3, 5) == 0
assert passages_communs(1, 1, 0) == 0
assert passages_communs(4, 4, 12) == 3
assert passages_communs(1, 3, 10) == 3
assert passages_communs(5, 7, 35) == 1
