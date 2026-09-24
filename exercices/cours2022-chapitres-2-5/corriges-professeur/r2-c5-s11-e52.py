# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S11 · 52 — Repérer la plus longue période active

def plus_longue_activation(journal: str) -> int:
    """Retournez la longueur du plus long bloc de caractères 1 consécutifs.
    """
    courant: int = 0
    maximum: int = 0
    c: str
    for c in journal:
        if c == "1":
            courant = courant + 1
            if courant > maximum:
                maximum = courant
        else:
            courant = 0
    return maximum

# Vérifications
assert plus_longue_activation('11011101') == 3
assert plus_longue_activation('001111') == 4
assert plus_longue_activation('') == 0
assert plus_longue_activation('000') == 0
assert plus_longue_activation('1') == 1
assert plus_longue_activation('11x111') == 3
assert plus_longue_activation('10101') == 1
