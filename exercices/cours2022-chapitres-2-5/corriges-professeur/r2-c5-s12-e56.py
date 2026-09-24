# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S12 · 56 — Nettoyer une ligne saisie au clavier

def normaliser_espaces(texte: str) -> str:
    """Retournez le texte sans espaces aux extrémités et avec un seul espace entre les blocs.
    """
    resultat: str = ""
    attente: bool = False
    c: str
    for c in texte:
        if c == " ":
            if len(resultat) > 0:
                attente = True
        else:
            if attente:
                resultat = resultat + " "
            resultat = resultat + c
            attente = False
    return resultat

# Vérifications
assert normaliser_espaces('  bon   jour  ') == 'bon jour'
assert normaliser_espaces('   ') == ''
assert normaliser_espaces('') == ''
assert normaliser_espaces('abc') == 'abc'
assert normaliser_espaces(' a ') == 'a'
assert normaliser_espaces('a  b   c') == 'a b c'
assert normaliser_espaces(' a\tb  c ') == 'a\tb c'
