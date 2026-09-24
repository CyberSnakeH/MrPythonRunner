# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S08 · 40 — Arrêter quand le bloc est indivisible

def taille_apres_reductions(taille: int, maximum: int) -> int:
    """Retournez la taille obtenue après les réductions utiles.
    Précondition : taille >= 0 and maximum >= 0
    """
    reste: int = taille
    etape: int = 0
    while etape < maximum and reste > 1:
        reste = (reste + 1) // 2
        etape = etape + 1
    return reste

# Vérifications
assert taille_apres_reductions(13, 2) == 4
assert taille_apres_reductions(1, 1000000) == 1
assert taille_apres_reductions(0, 1000000) == 0
assert taille_apres_reductions(9, 0) == 9
assert taille_apres_reductions(3, 10) == 1
assert taille_apres_reductions(8, 2) == 2
