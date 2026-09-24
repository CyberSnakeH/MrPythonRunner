# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S04 · 16 — Installer des rangées de chaises

def places_gradins(premier: int, supplement: int, rangees: int) -> int:
    """Retournez le nombre total de chaises à installer.
    Précondition : premier >= 0 and supplement >= 0 and rangees >= 0
    """
    total: int = 0
    taille: int = premier
    i: int = 0
    while i < rangees:
        total = total + taille
        taille = taille + supplement
        i = i + 1
    return total

# Vérifications
assert places_gradins(4, 2, 3) == 18
assert places_gradins(4, 2, 0) == 0
assert places_gradins(5, 0, 4) == 20
assert places_gradins(0, 3, 3) == 9
assert places_gradins(7, 2, 1) == 7
assert places_gradins(1, 1, 5) == 15
