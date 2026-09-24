# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S02 · 10 — Deux réservations peuvent-elles coexister ?

def reservations_en_conflit(debut1: int, fin1: int, debut2: int, fin2: int) -> bool:
    """Détectez si deux réservations occupent simultanément une salle.
    Précondition : 0 <= debut1 < fin1 <= 1440 and 0 <= debut2 < fin2 <= 1440
    """
    return debut1 < fin2 and debut2 < fin1

# Vérifications
assert reservations_en_conflit(60, 120, 90, 150) == True
assert reservations_en_conflit(60, 120, 120, 180) == False
assert reservations_en_conflit(120, 180, 60, 120) == False
assert reservations_en_conflit(0, 1440, 10, 20) == True
assert reservations_en_conflit(30, 40, 30, 40) == True
assert reservations_en_conflit(0, 10, 20, 30) == False
