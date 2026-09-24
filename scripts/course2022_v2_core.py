"""Shared authoring helpers for the second, fully rewritten exercise collection."""
import textwrap

SERIES = [
    (2, 'Préparer un atelier', '2.1–2.2', '19–32', 'Variables locales, calculs intermédiaires et ordre des opérations.'),
    (2, 'Décider si une action est possible', '2.3.1–2.3.2', '33–41', 'Comparaisons, conjonctions, disjonctions et court-circuit.'),
    (2, 'Appliquer des règles de gestion', '2.3.3', '41–42', 'Alternatives multiples, priorités et seuils.'),
    (3, 'Simuler une activité répétée', '3.1–3.3.2', '43–54', 'Boucles while, compteurs et accumulateurs.'),
    (3, 'Attendre un événement', '3.2–3.3', '45–55', 'Conditions d’arrêt, suites et changements d’état.'),
    (3, 'Explorer plusieurs possibilités', '3.3.4', '56–57', 'Parcours de candidats et boucles imbriquées.'),
    (4, 'Conserver une relation vraie', '4.1–4.2', '63–69', 'Invariants, variants et justification du résultat.'),
    (4, 'Éviter le travail inutile', '4.3', '69–78', 'Sortie anticipée et factorisation des calculs.'),
    (4, 'Auditer des simulations', '4.1–4.3', '63–78', 'Cas limites, arrêt et validation raisonnée.'),
    (5, 'Fabriquer des étiquettes', '5.1–5.2', '81–92', 'Range, concaténation, indices et découpages.'),
    (5, 'Analyser des journaux', '5.3.1', '93–101', 'Réductions, parcours indicés et résultat optionnel.'),
    (5, 'Nettoyer et interpréter des messages', '5.3.2–5.3.3', '101–107', 'Transformations, filtrages et petits automates à état.'),
]
ITEMS = []


def ex(series, name, title, signature, result, doc, pre, context, rules, examples,
       cases, body, *, kind='function', starter=None, method='', notes='', imports='', points=4):
    number = len(ITEMS) + 1
    chapter, theme, section, pages, _ = SERIES[series-1]
    header = f'def {name}({signature}) -> {result}:'
    documentation = doc + ('\nPrécondition : ' + pre if pre else '')
    head = (imports + '\n\n' if imports else '') + header + '\n' + textwrap.indent('"""' + documentation + '\n"""', '    ') + '\n'
    neutral = {'int':'0', 'float':'0.0', 'bool':'False', 'str':'""', 'Optional[int]':'None'}[result]
    solution = head + textwrap.indent(textwrap.dedent(body).strip(), '    ') + '\n'
    initial = head + textwrap.indent(textwrap.dedent(starter).strip() if starter else '# Écrivez votre programme ici.\nreturn ' + neutral, '    ') + '\n'
    tests = []
    for i, (args, expected) in enumerate(cases):
        call = f'{name}({args})'
        code = f'assert {call} == {expected!r}'
        if isinstance(expected, float):
            code = f'import math\nassert math.isclose({call}, {expected!r}, rel_tol=1e-9, abs_tol=1e-9)'
        tests.append({'id':f'test-{i+1:02}', 'label':f'Exemple expliqué {i+1}' if i<2 else f'Cas complémentaire {i-1}', 'hidden':i>=2, 'code':code})
    instruction = {'function':'Écrivez la fonction', 'complete':'Complétez la fonction fournie', 'debug':'Corrigez la fonction fournie'}[kind]
    statement = f'**Chapitre {chapter} · Série {series:02} — {theme}**\n\n## Situation\n\n{context}\n\n'
    statement += f'## Votre mission\n\n{instruction} `{name}`. {doc}\n\n{rules}\n\n'
    statement += f'### Fonction attendue\n\n```python\n{header}\n```\n\n'
    if imports:
        statement += f'Import fourni dans le code de départ : `{imports}`.\n\n'
    statement += f'### Exemples expliqués\n\n'
    for i, ((args, expected), explanation) in enumerate(zip(cases[:2], examples), 1):
        statement += f'**Exemple {i}.** `{name}({args})` renvoie `{expected!r}`. {explanation}\n\n'
    statement += '### Conditions sur les données\n\n'
    statement += (f'Vous pouvez supposer que `{pre}`. ' if pre else 'Les paramètres respectent les types de la signature. ')
    statement += 'Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.\n\n'
    if method:
        statement += f'### Méthode et justification\n\n{method}\n\n'
    statement += 'Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.\n\n'
    if result == 'float':
        statement += 'Ne faites pas d’arrondi. Les comparaisons automatiques utilisent des tolérances relative et absolue de $10^{-9}$.\n\n'
    statement += f'*Notions mobilisées : sections {section}, pages imprimées {pages} du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*'
    assert len(context.split()) >= 25, (name, 'context too short')
    assert len(rules.split()) >= 35, (name, 'rules too short')
    assert len(cases) >= 6
    assert len(examples) == 2
    exercise = {'id':f'r2-c{chapter}-s{series:02}-e{number:02}', 'title':f'S{series:02} · {number:02} — {title}',
                'kind':kind, 'statement':statement, 'starter':initial, 'points':points, 'timeout':5, 'tests':tests}
    ITEMS.append({'series':series, 'exercise':exercise, 'solution':solution, 'head':head,
                  'name':name, 'notes':notes, 'cases':cases})
