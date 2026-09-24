# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S12 · 59 — Lire la première annotation entre crochets

def contenu_balise(texte: str) -> str:
    """Retournez le contenu de la première annotation complète.
    """
    ouvert: bool = False
    resultat: str = ""
    c: str
    for c in texte:
        if ouvert:
            if c == "]":
                return resultat
            resultat = resultat + c
        elif c == "[":
            ouvert = True
    return ""

# Vérifications
assert contenu_balise('avant[ok]apres[non]') == 'ok'
assert contenu_balise('avant[incomplet') == ''
assert contenu_balise('') == ''
assert contenu_balise('abc]def') == ''
assert contenu_balise('[]') == ''
assert contenu_balise(']x[a[b]z') == 'a[b'
assert contenu_balise('[a b]') == 'a b'
