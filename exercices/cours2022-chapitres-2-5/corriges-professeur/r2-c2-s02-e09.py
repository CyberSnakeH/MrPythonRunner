# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S02 · 09 — L’alarme de désaccord

def deux_capteurs_valides(a: float, b: float, tolerance: float) -> bool:
    """Indiquez si deux mesures sont toutes deux recevables et suffisamment proches.
    Précondition : tolerance >= 0
    """
    return 0 <= a <= 100 and 0 <= b <= 100 and -tolerance <= a - b <= tolerance

# Vérifications
assert deux_capteurs_valides(48.0, 50.0, 2.0) == True
assert deux_capteurs_valides(110.0, 110.0, 1.0) == False
assert deux_capteurs_valides(0.0, 0.0, 0.0) == True
assert deux_capteurs_valides(100.0, 100.0, 0.0) == True
assert deux_capteurs_valides(10.0, 13.0, 2.0) == False
assert deux_capteurs_valides(-1.0, 0.0, 5.0) == False
assert deux_capteurs_valides(50.0, 48.0, 2.0) == True
