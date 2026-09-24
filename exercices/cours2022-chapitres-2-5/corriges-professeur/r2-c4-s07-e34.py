# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S07 · 34 — Ne pas oublier la dernière seconde

def distance_freinage(vitesse: int) -> int:
    """Retournez la distance parcourue jusqu’à l’arrêt dans ce modèle discret.
    Précondition : vitesse >= 0
    """
    v: int = vitesse
    distance: int = 0
    while v > 0:
        distance = distance + v
        if v >= 2:
            v = v - 2
        else:
            v = 0
    return distance

# Vérifications
assert distance_freinage(5) == 9
assert distance_freinage(4) == 6
assert distance_freinage(0) == 0
assert distance_freinage(1) == 1
assert distance_freinage(2) == 2
assert distance_freinage(7) == 16
