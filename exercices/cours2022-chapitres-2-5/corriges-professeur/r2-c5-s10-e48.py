# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S10 · 48 — Afficher seulement la fin d’une référence

def masquer_reference(reference: str, visibles: int) -> str:
    """Retournez la référence dont seul le suffixe autorisé est visible.
    Précondition : visibles >= 0
    """
    resultat: str = ""
    i: int
    for i in range(0, len(reference)):
        if i < len(reference) - visibles:
            resultat = resultat + "*"
        else:
            resultat = resultat + reference[i]
    return resultat

# Vérifications
assert masquer_reference('AB1245', 3) == '***245'
assert masquer_reference('XY', 5) == 'XY'
assert masquer_reference('', 2) == ''
assert masquer_reference('abc', 0) == '***'
assert masquer_reference('abc', 3) == 'abc'
assert masquer_reference('A B', 1) == '**B'
