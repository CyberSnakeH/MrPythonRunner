# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S03 · 13 — Donner priorité à l’alerte forte

def mode_ventilation(temperature: int, co2: int) -> int:
    """Choisissez le mode 0, 1 ou 2 du ventilateur.
    Précondition : co2 >= 0
    """
    if temperature >= 30 or co2 >= 1500:
        return 2
    elif temperature >= 24 or co2 >= 1000:
        return 1
    return 0

# Vérifications
assert mode_ventilation(26, 800) == 1
assert mode_ventilation(25, 1500) == 2
assert mode_ventilation(23, 999) == 0
assert mode_ventilation(24, 0) == 1
assert mode_ventilation(0, 1000) == 1
assert mode_ventilation(30, 0) == 2
assert mode_ventilation(-5, 800) == 0
