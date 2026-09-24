# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S02 · 07 — Une borne libre ne suffit pas

def demander_recharge(batterie: int, borne_libre: bool, mission_urgente: bool) -> bool:
    """Décidez si le robot doit demander la borne de recharge.
    Précondition : 0 <= batterie <= 100
    """
    motif: bool = batterie < 30 or mission_urgente
    return borne_libre and motif

# Vérifications
assert demander_recharge(20, True, False) == True
assert demander_recharge(80, False, True) == False
assert demander_recharge(30, True, False) == False
assert demander_recharge(100, True, True) == True
assert demander_recharge(0, False, False) == False
assert demander_recharge(29, True, False) == True
assert demander_recharge(80, True, False) == False
