# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S09 · 44 — Garder la plus grande charge observée

def pic_charge(initial: int, tours: int) -> int:
    """Retournez la plus grande charge observée, état initial compris.
    Précondition : initial >= 0 and tours >= 0
    """
    charge: int = initial
    pic: int = initial
    i: int = 0
    while i < tours:
        if charge % 2 == 0:
            charge = charge // 2
        else:
            charge = charge + 3
        if charge > pic:
            pic = charge
        i = i + 1
    return pic

# Vérifications
assert pic_charge(5, 3) == 8
assert pic_charge(8, 2) == 8
assert pic_charge(7, 0) == 7
assert pic_charge(0, 4) == 0
assert pic_charge(1, 3) == 4
assert pic_charge(9, 1) == 12
