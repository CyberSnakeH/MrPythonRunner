# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S06 · 27 — Installer les balises d’une grille

def cases_balisees(largeur: int, hauteur: int) -> int:
    """Comptez les cases qui reçoivent une balise.
    Précondition : largeur >= 0 and hauteur >= 0
    """
    total: int = 0
    x: int = 0
    while x < largeur:
        y: int = 0
        while y < hauteur:
            if (x + y) % 3 == 0:
                total = total + 1
            y = y + 1
        x = x + 1
    return total

# Vérifications
assert cases_balisees(3, 2) == 2
assert cases_balisees(0, 4) == 0
assert cases_balisees(1, 1) == 1
assert cases_balisees(2, 2) == 1
assert cases_balisees(3, 3) == 3
assert cases_balisees(4, 4) == 6
