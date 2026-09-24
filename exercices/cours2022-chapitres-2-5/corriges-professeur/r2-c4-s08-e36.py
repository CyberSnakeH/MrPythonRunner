# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S08 · 36 — Trouver un numéro disponible

def prochaine_place(depart: int) -> int:
    """Retournez le premier numéro admissible supérieur ou égal au départ.
    Précondition : depart >= 1
    """
    numero: int = depart
    while numero % 3 == 0 or numero % 5 == 0:
        numero = numero + 1
    return numero

# Vérifications
assert prochaine_place(9) == 11
assert prochaine_place(7) == 7
assert prochaine_place(1) == 1
assert prochaine_place(15) == 16
assert prochaine_place(3) == 4
assert prochaine_place(5) == 7
assert prochaine_place(29) == 29
