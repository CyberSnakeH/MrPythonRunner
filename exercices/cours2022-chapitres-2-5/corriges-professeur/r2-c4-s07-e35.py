# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S07 · 35 — Comptabiliser les pertes de la cuve
# Invariant : initial + t*apport = stock + pertes et 0 <= stock <= capacite. Variant tours-t. Le
# débordement change la répartition entre stock et pertes, jamais leur somme.

def eau_debordee(initial: int, apport: int, capacite: int, tours: int) -> int:
    """Retournez le volume cumulé qui a débordé de la cuve.
    Précondition : 0 <= initial <= capacite and apport >= 0 and tours >= 0
    """
    stock: int = initial
    pertes: int = 0
    t: int = 0
    while t < tours:
        stock = stock + apport
        if stock > capacite:
            pertes = pertes + stock - capacite
            stock = capacite
        t = t + 1
    return pertes

# Vérifications
assert eau_debordee(3, 4, 10, 2) == 1
assert eau_debordee(10, 3, 10, 2) == 6
assert eau_debordee(0, 4, 0, 3) == 12
assert eau_debordee(5, 8, 10, 0) == 0
assert eau_debordee(0, 5, 10, 2) == 0
assert eau_debordee(2, 0, 3, 8) == 0
