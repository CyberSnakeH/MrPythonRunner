# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S06 · 29 — Alterner les zones à contrôler

def charge_tournees(jours: int, zones: int) -> int:
    """Retournez le nombre total de minutes de contrôle.
    Précondition : jours >= 0 and zones >= 0
    """
    total: int = 0
    j: int = 1
    while j <= jours:
        z: int = 1
        while z <= zones:
            if (j + z) % 2 == 0:
                total = total + z
            z = z + 1
        j = j + 1
    return total

# Vérifications
assert charge_tournees(2, 3) == 6
assert charge_tournees(1, 1) == 1
assert charge_tournees(0, 4) == 0
assert charge_tournees(4, 0) == 0
assert charge_tournees(3, 3) == 10
assert charge_tournees(2, 2) == 3
