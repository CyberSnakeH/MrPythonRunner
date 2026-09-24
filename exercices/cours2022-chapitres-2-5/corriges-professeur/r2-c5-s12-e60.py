# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S12 · 60 — Interpréter une touche de répétition

def executer_repetitions(commandes: str) -> str:
    """Construisez le texte produit par les caractères ordinaires et la commande plus.
    """
    resultat: str = ""
    dernier: str = ""
    c: str
    for c in commandes:
        if c == "+":
            resultat = resultat + dernier
        else:
            resultat = resultat + c
            dernier = c
    return resultat

# Vérifications
assert executer_repetitions('ab++c+') == 'abbbcc'
assert executer_repetitions('++x+') == 'xx'
assert executer_repetitions('') == ''
assert executer_repetitions('+++') == ''
assert executer_repetitions('abc') == 'abc'
assert executer_repetitions('a+b++') == 'aabbb'
assert executer_repetitions('a +b') == 'a  b'
