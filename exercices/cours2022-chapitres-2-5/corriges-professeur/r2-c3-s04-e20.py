# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S04 · 20 — Retirer les pièces à contrôler

def stock_apres_tri(stock: int, jours: int) -> int:
    """Retournez le stock restant après les opérations de tri.
    Précondition : stock >= 0 and jours >= 0
    """
    reste: int = stock
    j: int = 0
    while j < jours:
        reste = reste - reste // 3
        j = j + 1
    return reste

# Vérifications
assert stock_apres_tri(10, 2) == 5
assert stock_apres_tri(2, 8) == 2
assert stock_apres_tri(0, 5) == 0
assert stock_apres_tri(12, 0) == 12
assert stock_apres_tri(9, 1) == 6
assert stock_apres_tri(27, 3) == 8
