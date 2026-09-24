# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S06 · 26 — Comparer les compositions d’un groupe

def formules_visite(adultes_max: int, enfants_max: int, budget: int) -> int:
    """Comptez les compositions de groupe admissibles.
    Précondition : adultes_max >= 0 and enfants_max >= 0 and budget >= 0
    """
    total: int = 0
    a: int = 1
    while a <= adultes_max:
        e: int = 1
        while e <= enfants_max:
            if 3 * a + 2 * e <= budget:
                total = total + 1
            e = e + 1
        a = a + 1
    return total

# Vérifications
assert formules_visite(2, 2, 8) == 3
assert formules_visite(3, 3, 4) == 0
assert formules_visite(0, 4, 20) == 0
assert formules_visite(1, 1, 5) == 1
assert formules_visite(2, 2, 10) == 4
assert formules_visite(1, 3, 7) == 2
