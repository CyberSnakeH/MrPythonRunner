# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S12 · 58 — Extraire la partie utile d’une ligne

def couper_commentaire(ligne: str) -> str:
    """Retournez tout ce qui précède le premier marqueur de commentaire.
    """
    resultat: str = ""
    c: str
    for c in ligne:
        if c == "#":
            return resultat
        resultat = resultat + c
    return resultat

# Vérifications
assert couper_commentaire('nom=Eva #élève') == 'nom=Eva '
assert couper_commentaire('#tout ignorer') == ''
assert couper_commentaire('') == ''
assert couper_commentaire('abc') == 'abc'
assert couper_commentaire('a#b#c') == 'a'
assert couper_commentaire('a #') == 'a '
assert couper_commentaire('"#"') == '"'
