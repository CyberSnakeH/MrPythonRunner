# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S11 · 53 — Retrouver le premier niveau qui redescend

from typing import Optional

def premiere_baisse(niveaux: str) -> Optional[int]:
    """Retournez l’indice de la première baisse, ou None s’il n’y en a pas.
    """
    i: int
    for i in range(1, len(niveaux)):
        if niveaux[i] < niveaux[i - 1]:
            return i
    return None

# Vérifications
assert premiere_baisse('124355') == 3
assert premiere_baisse('1229') == None
assert premiere_baisse('') == None
assert premiere_baisse('7') == None
assert premiere_baisse('91') == 1
assert premiere_baisse('AAAB') == None
assert premiere_baisse('ACB') == 2
