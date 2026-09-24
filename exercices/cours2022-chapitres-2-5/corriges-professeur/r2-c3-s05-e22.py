# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S05 · 22 — Faire entrer une bande dans son étui

def pliages_format(longueur: int, limite: int) -> int:
    """Retournez le nombre minimal de pliages nécessaires.
    Précondition : longueur >= 1 and limite >= 1
    """
    reste: int = longueur
    compte: int = 0
    while reste > limite:
        reste = (reste + 1) // 2
        compte = compte + 1
    return compte

# Vérifications
assert pliages_format(9, 3) == 2
assert pliages_format(4, 4) == 0
assert pliages_format(1, 1) == 0
assert pliages_format(3, 1) == 2
assert pliages_format(8, 1) == 3
assert pliages_format(17, 2) == 4
