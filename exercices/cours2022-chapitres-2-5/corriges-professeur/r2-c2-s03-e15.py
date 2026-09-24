# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S03 · 15 — Un plafond pour chaque journée

def location_casier(heures: int) -> int:
    """Retournez le prix d’une location de casier en euros.
    Précondition : heures >= 0
    """
    jours: int = heures // 24
    reste: int = heures % 24
    fin: int = reste * 2
    if fin > 12:
        fin = 12
    return jours * 12 + fin

# Vérifications
assert location_casier(26) == 16
assert location_casier(8) == 12
assert location_casier(0) == 0
assert location_casier(1) == 2
assert location_casier(6) == 12
assert location_casier(24) == 12
assert location_casier(48) == 24
assert location_casier(49) == 26
