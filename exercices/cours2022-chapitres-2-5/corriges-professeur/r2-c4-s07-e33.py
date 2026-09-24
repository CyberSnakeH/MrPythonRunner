# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S07 · 33 — Une demande limitée par le stock

def stock_controle(initial: int, arrivage: int, demande: int, tours: int) -> int:
    """Retournez le stock après tous les cycles d’approvisionnement et de vente.
    Précondition : initial >= 0 and arrivage >= 0 and demande >= 0 and tours >= 0
    """
    stock: int = initial
    t: int = 0
    while t < tours:
        stock = stock + arrivage
        if stock >= demande:
            stock = stock - demande
        else:
            stock = 0
        t = t + 1
    return stock

# Vérifications
assert stock_controle(3, 2, 4, 2) == 0
assert stock_controle(10, 5, 2, 2) == 16
assert stock_controle(7, 1, 9, 0) == 7
assert stock_controle(0, 0, 0, 4) == 0
assert stock_controle(0, 3, 3, 2) == 0
assert stock_controle(5, 0, 2, 2) == 1
