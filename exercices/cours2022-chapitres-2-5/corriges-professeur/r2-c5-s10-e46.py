# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S10 · 46 — Dessiner les graduations d’une règle

def marquages_regle(debut: int, fin: int, pas: int) -> str:
    """Construisez la ligne de graduations correspondant à l’intervalle demandé.
    Précondition : pas > 0
    """
    resultat: str = ""
    i: int
    for i in range(debut, fin):
        if i % pas == 0:
            resultat = resultat + "|"
        else:
            resultat = resultat + "."
    return resultat

# Vérifications
assert marquages_regle(0, 7, 3) == '|..|..|'
assert marquages_regle(-2, 3, 2) == '|.|.|'
assert marquages_regle(3, 3, 2) == ''
assert marquages_regle(5, 2, 1) == ''
assert marquages_regle(1, 4, 5) == '...'
assert marquages_regle(1, 4, 1) == '|||'
