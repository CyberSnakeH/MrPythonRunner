# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S03 · 11 — Le prix d’un dépôt au vestiaire

def cout_consigne(volume: int, fragile: bool) -> int:
    """Retournez le prix d’un dépôt en euros entiers.
    Précondition : volume > 0
    """
    prix: int = 0
    if volume <= 10:
        prix = 2
    elif volume <= 30:
        prix = 4
    else:
        prix = 7
    if fragile:
        prix = prix + 3
    return prix

# Vérifications
assert cout_consigne(8, True) == 5
assert cout_consigne(30, False) == 4
assert cout_consigne(10, False) == 2
assert cout_consigne(11, False) == 4
assert cout_consigne(31, False) == 7
assert cout_consigne(31, True) == 10
assert cout_consigne(1, False) == 2
