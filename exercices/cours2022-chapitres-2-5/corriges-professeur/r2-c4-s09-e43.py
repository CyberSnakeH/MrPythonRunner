# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S09 · 43 — Auditer une séquence de mesures

def alertes_capteur(nombre: int, seuil: int) -> int:
    """Comptez les mesures strictement supérieures au seuil.
    Précondition : nombre >= 0 and 0 <= seuil <= 10
    """
    i: int = 1
    compte: int = 0
    while i <= nombre:
        if (7 * i) % 11 > seuil:
            compte = compte + 1
        i = i + 1
    return compte

# Vérifications
assert alertes_capteur(4, 5) == 3
assert alertes_capteur(4, 10) == 0
assert alertes_capteur(0, 0) == 0
assert alertes_capteur(1, 7) == 0
assert alertes_capteur(1, 6) == 1
assert alertes_capteur(11, 0) == 10
