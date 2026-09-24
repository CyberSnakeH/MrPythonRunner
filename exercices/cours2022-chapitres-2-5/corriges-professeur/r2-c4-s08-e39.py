# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S08 · 39 — Interrompre le contrôle au bon moment

def controles_avant_alerte(nombre: int, alerte: int) -> int:
    """Retournez le nombre de postes contrôlés avant l’arrêt de la tournée.
    Précondition : nombre >= 0 and 0 <= alerte <= nombre
    """
    poste: int = 1
    compte: int = 0
    while poste <= nombre:
        compte = compte + 1
        if poste == alerte:
            return compte
        poste = poste + 1
    return compte

# Vérifications
assert controles_avant_alerte(8, 3) == 3
assert controles_avant_alerte(8, 0) == 8
assert controles_avant_alerte(0, 0) == 0
assert controles_avant_alerte(5, 1) == 1
assert controles_avant_alerte(5, 5) == 5
assert controles_avant_alerte(1, 1) == 1
