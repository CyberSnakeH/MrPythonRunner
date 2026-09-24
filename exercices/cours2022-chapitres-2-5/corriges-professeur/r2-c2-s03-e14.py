# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S03 · 14 — Un colis perdu ne marque aucun point

def points_livraison(retard: int, perdu: bool) -> int:
    """Calculez le score de qualité d’une livraison.
    """
    if perdu:
        return 0
    if retard <= 0:
        return 100
    elif retard <= 10:
        return 80
    elif retard <= 30:
        return 50
    return 0

# Vérifications
assert points_livraison(6, False) == 80
assert points_livraison(-3, True) == 0
assert points_livraison(0, False) == 100
assert points_livraison(10, False) == 80
assert points_livraison(11, False) == 50
assert points_livraison(30, False) == 50
assert points_livraison(31, False) == 0
assert points_livraison(12, True) == 0
