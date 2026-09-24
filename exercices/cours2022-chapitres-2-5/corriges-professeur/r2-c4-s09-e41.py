# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S09 · 41 — Agrandir un espace de stockage

def espace_inutilise(capacite: int, besoin: int) -> int:
    """Retournez l’espace libre après les agrandissements nécessaires.
    Précondition : capacite >= 1 and besoin >= 0
    """
    place: int = capacite
    while place < besoin:
        place = 2 * place
    return place - besoin

# Vérifications
assert espace_inutilise(3, 8) == 4
assert espace_inutilise(10, 4) == 6
assert espace_inutilise(1, 0) == 1
assert espace_inutilise(4, 4) == 0
assert espace_inutilise(2, 9) == 7
assert espace_inutilise(5, 11) == 9
