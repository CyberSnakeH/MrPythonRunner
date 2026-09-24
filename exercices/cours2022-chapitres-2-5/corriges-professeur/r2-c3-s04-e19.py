# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S04 · 19 — Le robot change de direction

def position_balancier(mouvements: int) -> int:
    """Retournez la position finale du robot sur son axe.
    Précondition : mouvements >= 0
    """
    position: int = 0
    k: int = 1
    while k <= mouvements:
        if k % 2 == 1:
            position = position + k
        else:
            position = position - k
        k = k + 1
    return position

# Vérifications
assert position_balancier(4) == -2
assert position_balancier(3) == 2
assert position_balancier(0) == 0
assert position_balancier(1) == 1
assert position_balancier(2) == -1
assert position_balancier(9) == 5
