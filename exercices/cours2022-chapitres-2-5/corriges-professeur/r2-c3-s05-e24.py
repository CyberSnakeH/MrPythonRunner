# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S05 · 24 — Financer des journées complètes

def jours_reserve(stock: int, cout_initial: int) -> int:
    """Retournez le nombre de journées que la réserve peut financer entièrement.
    Précondition : stock >= 0 and cout_initial > 0
    """
    reste: int = stock
    cout: int = cout_initial
    jours: int = 0
    while reste >= cout:
        reste = reste - cout
        cout = cout + 1
        jours = jours + 1
    return jours

# Vérifications
assert jours_reserve(10, 3) == 2
assert jours_reserve(3, 3) == 1
assert jours_reserve(0, 1) == 0
assert jours_reserve(2, 3) == 0
assert jours_reserve(15, 1) == 5
assert jours_reserve(7, 3) == 2
