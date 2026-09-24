# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S09 · 42 — Acheter des extensions successives

def achats_croissants(credits: int) -> int:
    """Retournez le nombre d’extensions entièrement achetées.
    Précondition : credits >= 0
    """
    reste: int = credits
    prix: int = 1
    compte: int = 0
    while reste >= prix:
        reste = reste - prix
        prix = prix * 2
        compte = compte + 1
    return compte

# Vérifications
assert achats_croissants(7) == 3
assert achats_croissants(6) == 2
assert achats_croissants(0) == 0
assert achats_croissants(1) == 1
assert achats_croissants(2) == 1
assert achats_croissants(15) == 4
assert achats_croissants(31) == 5
