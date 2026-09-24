# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S04 · 18 — Deux montants de versement

def epargne_alternee(semaines: int, petit: int, grand: int) -> int:
    """Calculez le montant déposé après le nombre de semaines indiqué.
    Précondition : semaines >= 0 and petit >= 0 and grand >= 0
    """
    total: int = 0
    s: int = 1
    while s <= semaines:
        if s % 2 == 1:
            total = total + petit
        else:
            total = total + grand
        s = s + 1
    return total

# Vérifications
assert epargne_alternee(5, 2, 5) == 16
assert epargne_alternee(1, 7, 3) == 7
assert epargne_alternee(0, 4, 8) == 0
assert epargne_alternee(4, 0, 3) == 6
assert epargne_alternee(3, 5, 5) == 15
assert epargne_alternee(2, 9, 1) == 10
