# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S11 · 51 — Compter des blocs sans utiliser split

def compter_mots_message(message: str) -> int:
    """Comptez les blocs non vides séparés par des espaces simples.
    """
    compte: int = 0
    dans_mot: bool = False
    c: str
    for c in message:
        if c == " ":
            dans_mot = False
        else:
            if not dans_mot:
                compte = compte + 1
            dans_mot = True
    return compte

# Vérifications
assert compter_mots_message('  salut  tout le-monde ') == 3
assert compter_mots_message('   ') == 0
assert compter_mots_message('') == 0
assert compter_mots_message('bonjour') == 1
assert compter_mots_message('a\tb c') == 2
assert compter_mots_message('a,b') == 1
assert compter_mots_message(' a b ') == 2
