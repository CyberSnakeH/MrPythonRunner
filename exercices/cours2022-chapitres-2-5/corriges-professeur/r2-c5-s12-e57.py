# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S12 · 57 — Encoder les bits sans perdre les séparateurs

def coder_signal(signal: str) -> str:
    """Encodez chaque bit et conservez les autres caractères.
    """
    resultat: str = ""
    c: str
    for c in signal:
        if c == "0":
            resultat = resultat + "01"
        elif c == "1":
            resultat = resultat + "10"
        else:
            resultat = resultat + c
    return resultat

# Vérifications
assert coder_signal('010') == '011001'
assert coder_signal('1-0') == '10-01'
assert coder_signal('') == ''
assert coder_signal('0') == '01'
assert coder_signal('1') == '10'
assert coder_signal('abc') == 'abc'
assert coder_signal('0 1') == '01 10'
