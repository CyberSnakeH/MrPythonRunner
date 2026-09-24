# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S10 · 49 — Recaler le début d’une étiquette

def rotation_etiquette(texte: str, decalage: int) -> str:
    """Déplacez les premiers caractères à la fin en conservant leur ordre.
    Précondition : 0 <= decalage <= len(texte)
    """
    return texte[decalage:len(texte)] + texte[0:decalage]

# Vérifications
assert rotation_etiquette('ABCDE', 2) == 'CDEAB'
assert rotation_etiquette('abc', 0) == 'abc'
assert rotation_etiquette('', 0) == ''
assert rotation_etiquette('abc', 3) == 'abc'
assert rotation_etiquette('abcd', 1) == 'bcda'
assert rotation_etiquette('a b', 2) == 'ba '
