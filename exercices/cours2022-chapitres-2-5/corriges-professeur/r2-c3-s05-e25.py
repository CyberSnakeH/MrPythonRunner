# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S05 · 25 — Atteindre la sortie du puits

def ascension_sonde(hauteur: int, montee: int, glissade: int) -> int:
    """Retournez le nombre de journées nécessaires pour sortir du puits.
    Précondition : hauteur >= 0 and montee > glissade >= 0
    """
    position: int = 0
    jours: int = 0
    while position < hauteur:
        position = position + montee
        jours = jours + 1
        if position < hauteur:
            position = position - glissade
    return jours

# Vérifications
assert ascension_sonde(5, 3, 2) == 3
assert ascension_sonde(2, 3, 2) == 1
assert ascension_sonde(0, 3, 2) == 0
assert ascension_sonde(10, 4, 1) == 3
assert ascension_sonde(6, 2, 0) == 3
assert ascension_sonde(3, 3, 2) == 1
