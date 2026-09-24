# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S11 · 54 — Vérifier les entrées et les sorties

def journal_coherent(journal: str) -> bool:
    """Indiquez si le journal décrit une salle initialement et finalement vide, sans sortie impossible.
    """
    effectif: int = 0
    c: str
    for c in journal:
        if c == "E":
            effectif = effectif + 1
        elif c == "S":
            effectif = effectif - 1
            if effectif < 0:
                return False
    return effectif == 0

# Vérifications
assert journal_coherent('EESS') == True
assert journal_coherent('SE') == False
assert journal_coherent('') == True
assert journal_coherent('E') == False
assert journal_coherent('E-x-S') == True
assert journal_coherent('ESSE') == False
assert journal_coherent('notes') == True
assert journal_coherent('ESES') == True
