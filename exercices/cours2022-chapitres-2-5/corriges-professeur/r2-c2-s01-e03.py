# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S01 · 03 — Compter les dalles du pourtour

def dalles_bordure(largeur: int, longueur: int) -> int:
    """Calculez combien de dalles appartiennent au bord d’une terrasse rectangulaire.
    Précondition : largeur >= 2 and longueur >= 2
    """
    deux_lignes: int = 2 * largeur
    deux_colonnes: int = 2 * (longueur - 2)
    return deux_lignes + deux_colonnes

# Vérifications
assert dalles_bordure(4, 5) == 14
assert dalles_bordure(2, 3) == 6
assert dalles_bordure(2, 2) == 4
assert dalles_bordure(3, 3) == 8
assert dalles_bordure(10, 4) == 24
assert dalles_bordure(7, 2) == 14
