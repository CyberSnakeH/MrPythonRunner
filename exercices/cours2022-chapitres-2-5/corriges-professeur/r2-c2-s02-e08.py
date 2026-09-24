# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S02 · 08 — Au moins deux colis identiques

def commande_partageable(articles: int, par_colis: int) -> bool:
    """Indiquez si une commande peut être répartie en au moins deux colis pleins et identiques.
    Précondition : articles >= 0 and par_colis >= 0
    """
    return par_colis > 0 and articles % par_colis == 0 and articles // par_colis >= 2

# Vérifications
assert commande_partageable(12, 4) == True
assert commande_partageable(4, 4) == False
assert commande_partageable(0, 4) == False
assert commande_partageable(9, 0) == False
assert commande_partageable(0, 0) == False
assert commande_partageable(10, 4) == False
assert commande_partageable(8, 4) == True
