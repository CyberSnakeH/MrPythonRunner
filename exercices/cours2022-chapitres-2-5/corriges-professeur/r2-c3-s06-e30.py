# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S06 · 30 — Préparer une commande sans boîte incomplète

def assemblages_boites(articles: int) -> int:
    """Comptez les répartitions exactes en boîtes de deux et de cinq articles.
    Précondition : articles >= 0
    """
    total: int = 0
    a: int = 0
    while 2 * a <= articles:
        b: int = 0
        while 2 * a + 5 * b <= articles:
            if 2 * a + 5 * b == articles:
                total = total + 1
            b = b + 1
        a = a + 1
    return total

# Vérifications
assert assemblages_boites(10) == 2
assert assemblages_boites(0) == 1
assert assemblages_boites(1) == 0
assert assemblages_boites(2) == 1
assert assemblages_boites(7) == 1
assert assemblages_boites(20) == 3
assert assemblages_boites(11) == 1
