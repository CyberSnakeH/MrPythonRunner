# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S03 · 12 — Livrer ce qui est disponible

def quantite_a_expedier(demande: int, stock: int, autoriser_partiel: bool) -> int:
    """Retournez le nombre d’articles à expédier immédiatement.
    Précondition : demande >= 0 and stock >= 0
    """
    if stock >= demande:
        return demande
    if autoriser_partiel:
        return stock
    return 0

# Vérifications
assert quantite_a_expedier(8, 5, True) == 5
assert quantite_a_expedier(8, 5, False) == 0
assert quantite_a_expedier(5, 5, False) == 5
assert quantite_a_expedier(3, 20, True) == 3
assert quantite_a_expedier(0, 5, True) == 0
assert quantite_a_expedier(5, 0, True) == 0
assert quantite_a_expedier(2, 3, False) == 2
