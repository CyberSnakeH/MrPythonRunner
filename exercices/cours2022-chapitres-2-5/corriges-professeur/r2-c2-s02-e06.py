# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S02 · 06 — Autoriser une visite de la serre

def ouvrir_serre(temperature: float, humidite: float, entretien: bool) -> bool:
    """Indiquez si une visite de la serre est autorisée.
    Précondition : 0 <= humidite <= 100
    """
    return 18 <= temperature <= 26 and 40 <= humidite <= 70 and not entretien

# Vérifications
assert ouvrir_serre(22.0, 55.0, False) == True
assert ouvrir_serre(22.0, 55.0, True) == False
assert ouvrir_serre(18.0, 40.0, False) == True
assert ouvrir_serre(26.0, 70.0, False) == True
assert ouvrir_serre(17.9, 55.0, False) == False
assert ouvrir_serre(22.0, 70.1, False) == False
