# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S05 · 23 — Mesurer ce que le filtre a capturé

def dechets_retires(pollution: int, seuil: int) -> int:
    """Retournez la quantité totale de déchets retirés.
    Précondition : pollution >= 0 and seuil >= 0
    """
    reste: int = pollution
    while reste > seuil:
        reste = reste // 2
    return pollution - reste

# Vérifications
assert dechets_retires(11, 3) == 9
assert dechets_retires(4, 5) == 0
assert dechets_retires(0, 0) == 0
assert dechets_retires(1, 0) == 1
assert dechets_retires(8, 2) == 6
assert dechets_retires(7, 7) == 0
