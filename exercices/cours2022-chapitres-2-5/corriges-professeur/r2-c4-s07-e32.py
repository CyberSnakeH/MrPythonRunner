# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S07 · 32 — Appliquer la règle de rendu de monnaie

def pieces_caisse(montant: int) -> int:
    """Retournez le nombre de pièces distribuées par la règle imposée.
    Précondition : montant >= 0
    """
    reste: int = montant
    compte: int = 0
    while reste > 0:
        if reste >= 5:
            reste = reste - 5
        elif reste >= 2:
            reste = reste - 2
        else:
            reste = reste - 1
        compte = compte + 1
    return compte

# Vérifications
assert pieces_caisse(12) == 3
assert pieces_caisse(8) == 3
assert pieces_caisse(0) == 0
assert pieces_caisse(1) == 1
assert pieces_caisse(4) == 2
assert pieces_caisse(10) == 2
assert pieces_caisse(19) == 5
