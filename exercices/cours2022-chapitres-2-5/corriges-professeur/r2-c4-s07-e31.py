# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S07 · 31 — Distribuer des lots équitables
# Après t tours, objets = reste + t*equipes ; reste reste naturel et décroît d’un entier
# strictement positif. À la sortie : 0 <= reste < equipes.

def reste_distribution(objets: int, equipes: int) -> int:
    """Retournez le nombre d’objets qui ne peuvent plus être distribués équitablement.
    Précondition : objets >= 0 and equipes > 0
    """
    reste: int = objets
    while reste >= equipes:
        reste = reste - equipes
    return reste

# Vérifications
assert reste_distribution(14, 4) == 2
assert reste_distribution(3, 5) == 3
assert reste_distribution(0, 3) == 0
assert reste_distribution(12, 4) == 0
assert reste_distribution(8, 1) == 0
assert reste_distribution(23, 6) == 5
