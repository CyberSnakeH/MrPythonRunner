# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S11 · 55 — Compter les changements d’état

def changements_mode(journal: str) -> int:
    """Retournez le nombre de changements entre deux relevés consécutifs.
    """
    compte: int = 0
    i: int
    for i in range(1, len(journal)):
        if journal[i] != journal[i - 1]:
            compte = compte + 1
    return compte

# Vérifications
assert changements_mode('AAABBA') == 2
assert changements_mode('xxxx') == 0
assert changements_mode('') == 0
assert changements_mode('A') == 0
assert changements_mode('ABAB') == 3
assert changements_mode('Aa A') == 3
assert changements_mode('  A  ') == 2
