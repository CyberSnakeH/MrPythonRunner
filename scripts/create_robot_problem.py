"""A cumulative twelve-question problem for chapters 2 to 5, in one editor."""
import ast
from collections import Counter
import json
from pathlib import Path
import sys
import tempfile
import textwrap
import time
import zipfile
from datetime import datetime
import shutil
from robot_diagrams import DIAGRAMS, diagram

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from runner.engine import grade
from runner.formats import assign_pack, check_student, export_pack, import_pack
from runner.jobs import Jobs
from runner.storage import Store

QUESTIONS = []


def question(title, signature, result, doc, pre, statement, examples, cases, solution, dependencies=(), reasoning=''):
    number = len(QUESTIONS) + 1
    name = signature.split('(')[0]
    declaration = 'def ' + signature + ' -> ' + result + ':'
    documentation = doc + ('\nPrécondition : ' + pre if pre else '')
    head = declaration + '\n' + textwrap.indent('"""' + documentation + '\n"""', '    ') + '\n'
    neutral = {'int': '0', 'bool': 'False', 'str': '""'}[result]
    starter = head + f'    # Question {number} : remplacez ce retour provisoire.\n    return {neutral}\n'
    source = head + textwrap.indent(textwrap.dedent(solution).strip(), '    ') + '\n'
    assert len(cases) == 4 and len(examples) == 2
    tests = [{'id': f'q{number:02}-t{i+1}', 'label': f'Q{number:02} — ' + label,
              'hidden': i >= 2, 'code': f'assert {name}({args}) == {expected!r}'}
             for i, (label, args, expected) in enumerate(cases)]
    text = f'## Question {number} — {title} · 4 points\n\n{statement}\n\n```python\n{declaration}\n```\n\n'
    text += ('**Précondition :** `' + pre + '`.\n\n') if pre else '**Données :** toute valeur respectant les types de la signature est autorisée.\n\n'
    if dependencies:
        text += '**Fonctions à réutiliser :** ' + ', '.join('`' + d + '`' for d in dependencies) + '. Ne recopiez pas leur logique.\n\n'
    for (_, args, expected), explanation in zip(cases[:2], examples):
        text += f'- `{name}({args})` renvoie `{expected!r}`. {explanation}\n'
    if reasoning:
        text += '\n**À justifier en commentaire :** ' + reasoning + '\n'
    QUESTIONS.append({'number': number, 'name': name, 'title': title, 'statement': text,
                      'source': source, 'starter': starter, 'head': head, 'tests': tests,
                      'dependencies': dependencies, 'neutral': neutral})


question('Fixer le coût d’une action', 'cout_action(action: str)', 'int',
         'Retourne le coût d’une action reconnue, ou -1 pour une action inconnue.', '',
         'Le service technique définit trois commandes : `A` fait avancer le robot et coûte **2 unités** d’énergie ; `R` le fait reculer et coûte **1 unité** ; `P` le laisse en place et coûte **0 unité**. Écrivez `cout_action`. Toute autre chaîne, y compris une minuscule, la chaîne vide ou une chaîne de plusieurs caractères, doit donner `-1`. La valeur négative signale une commande inconnue et ne représente jamais une recharge.',
         ['Avancer consomme deux unités.', 'Une minuscule ne désigne pas une commande reconnue.'],
         [('Avance', "'A'", 2), ('Commande inconnue', "'a'", -1), ('Recul et pause', "'R'", 1), ('Pause', "'P'", 0)],
         'if action == "A":\n    return 2\nelif action == "R":\n    return 1\nelif action == "P":\n    return 0\nreturn -1')

question('Autoriser une action', 'action_possible(energie: int, action: str)', 'bool',
         'Indique si une action est reconnue et peut être entièrement financée.', 'energie >= 0',
         'Le robot ne doit jamais commencer une action qu’il ne peut pas terminer. Écrivez un prédicat qui utilise le coût calculé à la question 1. Une action est possible seulement si elle est reconnue et si son coût ne dépasse pas l’énergie disponible. Une pause reste possible avec une batterie vide. Une commande inconnue doit être refusée, même si son coût conventionnel vaut −1.',
         ['Les deux unités disponibles paient exactement l’avance.', 'La batterie est vide, mais une pause ne consomme rien.'],
         [('Énergie exacte', "2, 'A'", True), ('Pause sans énergie', "0, 'P'", True), ('Batterie insuffisante', "1, 'A'", False), ('Commande inconnue', "100, 'X'", False)],
         'cout: int = cout_action(action)\nreturn cout >= 0 and cout <= energie', ('cout_action',))

question('Mettre à jour la position', 'position_apres(position: int, action: str)', 'int',
         'Retourne la position après une action, sans gérer la batterie.', '',
         'Le couloir est un axe entier sans obstacle : les positions négatives sont autorisées. Une avance `A` augmente la position de **1**, un recul `R` la diminue de **1**, et une pause `P` la laisse inchangée. Pour toute commande inconnue, conservez aussi la position. Cette fonction s’occupe uniquement du déplacement : le contrôle d’énergie sera assuré par les fonctions suivantes. Attention : avancer coûte deux unités d’énergie mais ne déplace que d’une case.',
         ['Depuis la case −2, une avance mène à −1.', 'Un recul depuis l’origine mène à la case −1.'],
         [('Avance', "-2, 'A'", -1), ('Recul', "0, 'R'", -1), ('Pause', "7, 'P'", 7), ('Commande inconnue', "3, 'AA'", 3)],
         'if action == "A":\n    return position + 1\nelif action == "R":\n    return position - 1\nreturn position')

question('Simuler une minute de recharge', 'recharger(energie: int, capacite: int, gain: int)', 'int',
         'Retourne l’énergie après une minute de recharge, sans dépasser la capacité.',
         '0 <= energie <= capacite and gain > 0',
         'Au dépôt, la borne apporte `gain` unités par minute entière. La batterie ne peut pas dépasser sa `capacite` : tout surplus fourni pendant la dernière minute est perdu. Écrivez une fonction qui calcule l’énergie après une seule minute. Une batterie déjà pleine conserve sa charge. Une capacité nulle est autorisée et conduit toujours à zéro. Utilisez une variable intermédiaire et une alternative, sans modifier les paramètres.',
         ['La recharge propose 11 unités, mais la batterie est limitée à 10.', 'L’apport tient entièrement dans la batterie : 2 + 3 = 5.'],
         [('Plafonnement', '8, 10, 3', 10), ('Recharge ordinaire', '2, 10, 3', 5), ('Batterie pleine', '10, 10, 3', 10), ('Capacité nulle', '0, 0, 4', 0)],
         'nouvelle: int = energie + gain\nif nouvelle > capacite:\n    return capacite\nreturn nouvelle')

question('Préparer la batterie avant le départ', 'minutes_recharge(energie: int, capacite: int, gain: int, cible: int)', 'int',
         'Retourne le nombre minimal de minutes pour atteindre au moins la charge cible.',
         '0 <= energie <= capacite and gain > 0 and 0 <= cible <= capacite',
         'Le chef de mission demande une charge d’au moins `cible` unités avant le départ. Simulez des minutes successives avec une boucle **while**, en appelant `recharger` à chaque tour. Arrêtez-vous dès que la charge atteint ou dépasse la cible ; il n’est pas nécessaire d’obtenir une égalité exacte. Si la charge initiale suffit déjà, le résultat vaut zéro. La cible ne dépasse jamais la capacité : elle peut donc être atteinte.',
         ['Les charges successives sont 2, 5 puis 8 : il faut deux minutes.', 'La charge initiale dépasse déjà la cible : aucun temps d’attente.'],
         [('Deux minutes', '2, 10, 3, 8', 2), ('Déjà suffisant', '9, 10, 3, 8', 0), ('Dernière minute plafonnée', '0, 10, 4, 10', 3), ('Batterie vide de capacité nulle', '0, 0, 1, 0', 0)],
         'charge: int = energie\nminutes: int = 0\nwhile charge < cible:\n    charge = recharger(charge, capacite, gain)\n    minutes = minutes + 1\nreturn minutes', ('recharger',),
         'Que représente `charge` après k tours ? Pourquoi une recharge augmente-t-elle strictement la charge tant que la cible n’est pas atteinte ? Raisonnez sur le déficit positif jusqu’à la cible pour établir la terminaison.')

question('Rejoindre un point aussi loin que possible', 'avancer_au_maximum(energie: int, distance: int)', 'int',
         'Retourne le nombre d’avances réalisables, dans la limite de la distance demandée.',
         'energie >= 0 and distance >= 0',
         'Avant de programmer un trajet complet, on étudie une livraison située `distance` cases plus loin. Le robot effectue uniquement des commandes `A`, tant qu’il reste une case à parcourir et que sa batterie permet une nouvelle avance. Écrivez cette simulation avec **while** et retournez le nombre d’avances réellement effectuées. Ne confondez pas la distance atteinte et l’énergie dépensée. La fonction ne recharge jamais la batterie et ne permet pas une avance partiellement payée.',
         ['Cinq unités financent deux avances ; la troisième demanderait deux unités alors qu’il n’en reste qu’une.', 'Le robot s’arrête après deux avances car la destination est atteinte, même s’il reste de l’énergie.'],
         [('Arrêt par batterie', '5, 4', 2), ('Arrêt à destination', '10, 2', 2), ('Destination déjà atteinte', '9, 0', 0), ('Énergie exacte', '6, 3', 3)],
         'reste: int = energie\npas: int = 0\nwhile pas < distance and action_possible(reste, "A"):\n    reste = reste - cout_action("A")\n    pas = pas + 1\nreturn pas', ('action_possible', 'cout_action'),
         r'Établissez $energie = reste + 2 \times pas$ et $0 \leq pas \leq distance$. Donnez un variant naturel, puis expliquez les deux causes possibles d’arrêt. Une formule directe ne répond pas ici à la méthode demandée.')

question('Vérifier le programme reçu', 'programme_valide(programme: str)', 'bool',
         'Indique si tous les caractères du programme sont des commandes reconnues.', '',
         'Un programme est une chaîne : chaque caractère représente une action, exécutée de gauche à droite. Vérifiez que tous les caractères sont reconnus par `cout_action`, à l’aide d’un parcours **for**. Dès qu’un caractère inconnu apparaît, retournez False. La chaîne vide est un programme valide qui ne demande aucune action. Les espaces et les minuscules sont interdits : ne nettoyez pas le programme silencieusement.',
         ['Les quatre caractères A, P, R, A sont tous reconnus.', 'L’espace fait partie de la chaîne et rend le programme invalide.'],
         [('Programme reconnu', "'APRA'", True), ('Espace interdit', "'A R'", False), ('Programme vide', "''", True), ('Minuscule interdite', "'Ar'", False)],
         'action: str\nfor action in programme:\n    if cout_action(action) < 0:\n        return False\nreturn True', ('cout_action',),
         'Expliquez pourquoi la première commande inconnue suffit pour conclure, sans parcourir la suite.')

question('Prévoir l’énergie du trajet entier', 'energie_programme(programme: str)', 'int',
         'Retourne le coût total du programme, ou -1 s’il contient une commande inconnue.', '',
         'Le dépôt veut calculer le besoin énergétique théorique avant de choisir une batterie. Additionnez les coûts des actions avec **for** en réutilisant `cout_action`. Si une seule commande est inconnue, retournez `-1`, quel que soit le coût déjà accumulé. Il n’y a ici aucune limite de batterie : on calcule le coût de tout le programme. Le programme vide et un programme ne contenant que des pauses coûtent zéro.',
         ['Les coûts sont 2 + 0 + 1 + 2, soit cinq unités.', 'Le caractère X invalide tout le calcul, même après deux commandes connues.'],
         [('Somme des coûts', "'APRA'", 5), ('Programme invalide', "'AAX'", -1), ('Programme vide', "''", 0), ('Pauses gratuites', "'PPP'", 0)],
         'total: int = 0\naction: str\nfor action in programme:\n    cout: int = cout_action(action)\n    if cout < 0:\n        return -1\n    total = total + cout\nreturn total', ('cout_action',))

question('Conserver exactement les actions exécutées', 'prefixe_executable(programme: str, energie: int)', 'str',
         'Retourne le préfixe exécuté avant la première action impossible.', 'energie >= 0',
         'Sur le terrain, le robot lit les commandes dans l’ordre. Avant chaque action, il vérifie qu’elle est reconnue et entièrement finançable avec l’énergie restante. Au premier refus, il s’arrête **définitivement** : il ne saute pas la commande pour essayer les suivantes. Retournez la chaîne exacte des actions effectuées avant cet arrêt. Une pause reconnue est incluse même si la batterie est vide. Contrairement à la question 8, une commande inconnue n’annule pas les actions déjà effectuées.',
         ['Après A, il reste une unité ; P est exécutée gratuitement. La seconde A est refusée et R n’est jamais essayée.', 'La première pause est effectuée avant de rencontrer X ; la suite est abandonnée.'],
         [('Ne pas sauter une action', "'APAR', 3", 'AP'), ('Arrêt sur commande inconnue', "'PXAR', 9", 'P'), ('Pauses puis blocage', "'PPA', 0", 'PP'), ('Fin avec énergie nulle', "'ARP', 3", 'ARP')],
         'resultat: str = ""\nreste: int = energie\naction: str\nfor action in programme:\n    if not action_possible(reste, action):\n        return resultat\n    resultat = resultat + action\n    reste = reste - cout_action(action)\nreturn resultat', ('action_possible', 'cout_action'),
         'Expliquez pourquoi le résultat est toujours un préfixe valide du programme et pourquoi l’énergie restante ne devient jamais négative. Le nombre de caractères non encore lus fournit une borne au nombre de tours.')

question('Localiser le robot après son arrêt', 'position_finale(programme: str, energie: int, depart: int)', 'int',
         'Retourne la position après les seules actions effectivement exécutables.', 'energie >= 0',
         'Le suivi de livraison doit afficher la position réelle du robot, même si son trajet a été interrompu. Commencez par obtenir le préfixe de la question 9. Partez ensuite de `depart` et appliquez `position_apres` à chacun des caractères de ce préfixe avec **for**. Les positions négatives restent autorisées. Un programme vide ou une première action refusée laisse le robot au départ. Ne reparcourez pas les commandes situées après l’arrêt.',
         ['Avec trois unités, seules A et P sont exécutées : depuis 10, le robot arrive à 11.', 'Deux reculs consomment les deux unités et déplacent le robot de 0 à −2.'],
         [('Trajet interrompu', "'APAR', 3, 10", 11), ('Position négative', "'RR', 2, 0", -2), ('Commande refusée au départ', "'XA', 9, 4", 4), ('Aller et retour', "'ARP', 3, -2", -2)],
         'execute: str = prefixe_executable(programme, energie)\nposition: int = depart\naction: str\nfor action in execute:\n    position = position_apres(position, action)\nreturn position', ('prefixe_executable', 'position_apres'))

question('Établir le bilan énergétique', 'energie_restante(programme: str, energie: int)', 'int',
         'Retourne l’énergie disponible après l’arrêt du robot.', 'energie >= 0',
         'Le technicien doit savoir si le robot possède encore de l’énergie après sa mission. Obtenez le préfixe réellement exécuté avec `prefixe_executable`, puis calculez son coût avec `energie_programme`. Soustrayez ce coût à l’énergie initiale. Cette question ne demande aucune nouvelle boucle. Une interruption n’implique pas forcément une batterie vide : une unité restante ne permet pas une avance, mais elle reste bien dans la batterie.',
         ['A et P coûtent deux unités ; il en reste une sur les trois disponibles.', 'X est refusée immédiatement : aucune des cinq unités n’a été consommée.'],
         [('Reste insuffisant pour avancer', "'APAR', 3", 1), ('Commande inconnue immédiate', "'XA', 5", 5), ('Dépense exacte', "'ARP', 3", 0), ('Programme vide', "'', 7", 7)],
         'execute: str = prefixe_executable(programme, energie)\nreturn energie - energie_programme(execute)', ('prefixe_executable', 'energie_programme'),
         'Pourquoi energie_programme ne peut-elle pas renvoyer −1 lorsqu’elle reçoit le préfixe exécutable ? Pourquoi le résultat appartient-il à l’intervalle de zéro à l’énergie initiale ?')

question('Produire le compte rendu de mission', 'bilan_mission(programme: str, energie: int, depart: int)', 'str',
         'Retourne le compte rendu textuel standardisé de la mission.', 'energie >= 0',
         'Vous devez maintenant réunir les fonctions dans un compte rendu. **Validez d’abord tout le programme** : s’il contient une commande inconnue, retournez uniquement `INVALIDE`, même si la batterie aurait arrêté le robot avant de la rencontrer. Sinon, construisez trois champs séparés par des points-virgules, sans espace :\n\n'
         '1. `TERMINE` si toutes les commandes ont pu être exécutées, sinon `BLOQUE`. Comparez la longueur du préfixe exécutable à celle du programme.\n'
         '2. `AVANT` si la position finale est strictement supérieure au départ, `ARRIERE` si elle lui est inférieure, sinon `SUR_PLACE`. Il s’agit du déplacement final, pas du sens de la dernière commande.\n'
         '3. `VIDE` si l’énergie restante est nulle, sinon `RESTE`.\n\n'
         'Un programme vide est terminé, laisse le robot sur place et conserve sa batterie. Une mission peut être terminée avec une batterie vide, ou bloquée avec de l’énergie restante. Réutilisez les fonctions existantes et concaténez les trois champs : aucune conversion de nombre en texte ni nouvelle boucle n’est nécessaire.',
         ['Le robot termine l’aller-retour et la pause, revient au départ et dépense ses trois unités.', 'Il effectue A et P, reste une case devant son départ et conserve une unité inutilisable pour l’avance suivante.'],
         [('Mission terminée à sec', "'ARP', 3, 0", 'TERMINE;SUR_PLACE;VIDE'), ('Blocage avec réserve', "'APAR', 3, 10", 'BLOQUE;AVANT;RESTE'), ('Erreur même après un blocage', "'AAX', 0, 0", 'INVALIDE'), ('Mission en recul', "'RR', 5, 7", 'TERMINE;ARRIERE;RESTE')],
         'if not programme_valide(programme):\n    return "INVALIDE"\nexecute: str = prefixe_executable(programme, energie)\nposition: int = position_finale(programme, energie, depart)\nreste: int = energie_restante(programme, energie)\netat: str = "BLOQUE"\nif len(execute) == len(programme):\n    etat = "TERMINE"\nsens: str = "SUR_PLACE"\nif position > depart:\n    sens = "AVANT"\nelif position < depart:\n    sens = "ARRIERE"\nbatterie: str = "RESTE"\nif reste == 0:\n    batterie = "VIDE"\nreturn etat + ";" + sens + ";" + batterie',
         ('programme_valide', 'prefixe_executable', 'position_finale', 'energie_restante'),
         'Cette version privilégie la décomposition mais recalcule plusieurs fois le préfixe. Identifiez ces appels dans vos commentaires et expliquez pourquoi leur résultat reste identique. Il n’est pas demandé d’introduire des tuples ou de modifier les signatures pour optimiser ces appels.')


INTRO = r'''# Problème — Un robot de livraison dans un couloir

Une médiathèque utilise un petit robot pour transporter des documents le long d’un couloir. Avant de le brancher au matériel, vous devez construire son simulateur : prévoir la recharge, interpréter les commandes, arrêter proprement un trajet impossible et produire un compte rendu.

Le robot se trouve sur un axe de positions entières, positives ou négatives. Il possède une quantité entière d’énergie. Il ne se recharge jamais pendant un trajet ; la borne de recharge sera simulée séparément aux questions 4 et 5.

| Commande | Déplacement | Coût en énergie |
|---|---|---|
| `A` | Une case vers les positions croissantes | 2 |
| `R` | Une case vers les positions décroissantes | 1 |
| `P` | Aucun déplacement | 0 |

Un programme tel que `APAR` désigne quatre commandes successives. Les espaces ne sont pas des séparateurs autorisés. Sur le terrain, une commande inconnue ou trop coûteuse arrête le trajet avant son exécution ; aucune commande suivante n’est essayée.

## Organisation du travail

Le sujet comprend **12 questions à 4 points, soit 48 points**, dans **un seul programme Python**. Complétez les fonctions dans l’ordre et conservez celles déjà écrites au-dessus : les dernières questions appellent les premières. Aucun copier-coller entre exercices n’est nécessaire.

Les questions 1 à 4 mobilisent les variables, expressions, booléens et alternatives du chapitre 2. Les questions 5 et 6 utilisent les boucles while du chapitre 3 et les raisonnements du chapitre 4. Les questions 7 à 12 introduisent les parcours for et les chaînes du chapitre 5, en réutilisant aussi la sortie anticipée du chapitre 4. Des commentaires sont demandés pour justifier certaines boucles.

- Conservez les noms, paramètres et types de retour fournis. Annotez vos variables locales et utilisez `return`, sans saisie au clavier.
- Réutilisez les fonctions indiquées dans chaque question. Ne réécrivez pas leurs calculs dans les fonctions suivantes.
- N’utilisez ni listes, ni tuples, ni dictionnaires, ni récursion, ni fonction passée en paramètre. Aucun import n’est nécessaire.
- Vous pouvez supposer les préconditions respectées. Il ne faut pas ajouter de traitement des entrées qui les violent.
- Cliquez sur **Tester mon code** au fil du travail. L’application lance les tests de tout le problème : les échecs des questions non traitées sont donc normaux. Les noms des tests commencent par Q01 à Q12.
- Chaque question possède quatre tests de même poids, dont les deux exemples visibles ci-dessous. Les résultats représentent un barème automatique indicatif ; la réutilisation des fonctions et les raisonnements sont relus par le professeur.

## Fil conducteur : une mission interrompue

Avec le programme `APAR`, une énergie initiale de 3 et un départ en 10 :

| Étape | Décision | Position | Énergie restante |
|---|---|---|---|
| Départ | Aucune action effectuée | 10 | 3 |
| `A` | Exécutée, coût 2 | 11 | 1 |
| `P` | Exécutée, coût 0 | 11 | 1 |
| `A` | Refusée, car 1 < 2 | 11 | 1 |
| `R` | Non examinée : la mission est déjà arrêtée | 11 | 1 |

Les fonctions finales devront donc retrouver le préfixe `AP`, la position 11, l’énergie 1 et le bilan `BLOQUE;AVANT;RESTE`.
'''

GUIDE = '''# Guide professeur — Un robot de livraison

Sujet progressif de 12 questions, dans un seul exercice et un seul éditeur : les fonctions des premières questions sont disponibles pour les suivantes dans le même programme. Le modèle est basé sur les notions des chapitres 2 à 5 du cours fourni, *Éléments de Programmation (en Python)* de Frédéric Peschanski et Romain Demangeon (`cours2022.pdf`). Le scénario et les questions sont rédigés pour cette activité.

## Fichiers

- `professeur-probleme-robot.mrpack` : modèle à importer dans l’espace professeur.
- `SUJET.md` : sujet complet lisible séparément.
- `code-depart.py` : les douze fonctions à compléter, sans solution.
- `corrige-professeur.py` : solution complète et 48 assertions de vérification, à conserver pour le professeur.
- `validation.json` : résultats des vérifications avec MrPython.

Dans l’application : **Professeur → Charger une série**, importer le modèle, puis **Distribuer à un élève** pour renseigner son identifiant et exporter son fichier personnel. L’élève importe ce fichier attribué et saisit son identifiant. Le modèle professeur n’autorise pas l’accès élève sans attribution. Ne distribuez pas le ZIP complet contenant le corrigé.

## Dépendances entre les questions

| Question | Fonction | Réutilise |
|---|---|---|
{{DEPENDENCIES}}

Q1–Q4 : expressions, variables, prédicats et alternatives. Q5–Q6 : simulation while, invariant, variant et arrêt. Q7–Q12 : parcours de chaînes, accumulateurs, arrêt anticipé, concaténation et composition des fonctions.

Le moteur exécute tous les tests du problème à chaque tentative. Tant que certaines fonctions sont incomplètes, leurs tests échouent ; il faut lire les groupes Q01 à Q12. Une erreur de syntaxe ou de typage peut empêcher l’exécution du programme entier. Une erreur dans une fonction auxiliaire peut faire échouer plusieurs questions suivantes.

## Barème et relecture

Le modèle contient un exercice de 48 points et 48 tests de même poids : quatre tests par question, soit quatre points automatiques par question. Deux tests par question sont visibles et deux sont masqués dans l’interface. Les tests masqués restent présents dans le fichier hors ligne. La note est indicative : le professeur doit relire la composition des fonctions, les méthodes demandées et les commentaires. Les tests de valeurs seuls ne prouvent pas qu’une fonction précédente est appelée.

Le corrigé réutilise effectivement les fonctions demandées. Aux questions 10 à 12, plusieurs appels recalculent le préfixe ; c’est un choix pédagogique explicite pour travailler la composition sans tuple ni état partagé. Les fonctions sont déterministes et ne modifient pas leurs arguments : ces recalculs produisent le même résultat.

## Éléments de justification

- Q5 : après k tours, charge est le résultat de k appels à recharger et reste entre zéro et la capacité. Tant que charge < cible <= capacite, le gain strictement positif fait augmenter la charge. La partie positive de cible−charge décroît strictement jusqu’à zéro. La boucle s’arrête au premier nombre de minutes suffisant.
- Q6 : energie = reste + 2 × pas ; reste >= 0 et 0 <= pas <= distance. Le variant distance−pas diminue. À la sortie, la distance est atteinte ou les unités restantes ne financent pas une nouvelle avance. Le stock d’énergie initial n’est jamais modifié.
- Q7 : les caractères déjà parcourus sont valides. Un seul caractère inconnu suffit à réfuter la validité globale ; sans retour anticipé, le programme entier a été validé.
- Q9 : le résultat est le préfixe déjà exécuté ; son coût ajouté à reste donne l’énergie initiale. Une action n’est ajoutée qu’après validation de son coût et de son financement. Une action refusée déclenche un retour immédiat. Le programme étant une chaîne finie, le parcours termine, même si des pauses ne font pas diminuer l’énergie.
- Q11 : le préfixe retourné par Q9 est toujours valide ; energie_programme ne peut donc pas donner −1 sur ce préfixe. Son coût est compris entre zéro et l’énergie initiale, ce qui garantit le même encadrement pour l’énergie restante.
- Q12 : la validation porte sur le programme entier avant tout bilan. Elle peut donc détecter une commande inconnue placée après une action qui aurait déjà bloqué le robot. La comparaison de position est relative au départ, tandis que le champ d’énergie dépend de la valeur restante, pas de la réussite de la mission.

## Vérification

Les 48 tests passent sur le corrigé avec le moteur MrPython. Le code de départ est syntaxiquement valide et exécutable, mais ne réussit pas le problème. Chaque fonction est également remplacée séparément par un retour constant : les tests de sa propre question rejettent cette modification. Un contrôle des appels du corrigé confirme les dépendances annoncées. Le pack est relu après export, attribué à un identifiant de test et exécuté par le processus de travail de l’application. Un autre identifiant est refusé.
'''


def main():
    output = ROOT / 'exercices/probleme-robot-chapitres-2-5'
    solution = '\n\n'.join(q['source'] for q in QUESTIONS)
    starter = '\n\n'.join(q['starter'] for q in QUESTIONS)
    tests = [t for q in QUESTIONS for t in q['tests']]
    subject = INTRO + '\n\n' + '\n\n'.join(q['statement'] for q in QUESTIONS)
    subject = subject.replace('## Organisation du travail', diagram('couloir') + '## Organisation du travail')
    subject = subject.replace('## Question 5', diagram('recharge') + '## Question 5')
    subject = subject.replace('## Question 9', diagram('execution') + '## Question 9')
    subject = subject.replace('## Question 12', diagram('fonctions') + '## Question 12')
    exercise = {'id': 'robot-q01-q12-v1', 'title': 'Un robot de livraison — Questions 1 à 12',
                'kind': 'complete', 'statement': subject, 'starter': starter,
                'points': 48, 'timeout': 5, 'tests': tests}
    pack = {'format': 'mrpython-pack', 'version': 1, 'id': 'probleme-robot-ch2-5-professeur-v1',
            'title': 'Problème progressif — Un robot de livraison',
            'description': '12 questions liées dans un seul programme. Les premières fonctions servent aux suivantes. Chapitres 2 à 5 : alternatives, while, invariants, for et chaînes. Travaillez dans l’ordre et conservez vos fonctions. Les tests portent les numéros Q01 à Q12.',
            'author': 'Sujet pédagogique — chapitres 2 à 5', 'assets': {}, 'exercises': [exercise]}
    assert len(tests) == 48
    ast.parse(starter)
    report = grade(solution, tests, 48)
    initial = grade(starter, tests, 48)
    assert report['status'] == 'passed' and not report['diagnostics'], report
    assert initial['status'] == 'failed', initial
    checks = []
    tree = ast.parse(solution)
    for question_data, function in zip(QUESTIONS, tree.body):
        calls = {node.func.id for node in ast.walk(function) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)}
        assert set(question_data['dependencies']) <= calls
        mutant = '\n\n'.join((q['head'] + '    return ' + q['neutral'] + '\n') if q is question_data else q['source'] for q in QUESTIONS)
        mutation_report = grade(mutant, question_data['tests'], 4)
        assert mutation_report['status'] == 'failed', (question_data['name'], mutation_report)
        checks.append({'question': question_data['number'], 'function': question_data['name'],
                       'tests': 4, 'solution_passed': 4, 'constant_mutation': mutation_report['status'],
                       'required_calls_present': True})
    archive = export_pack(pack)
    assert import_pack(archive) == pack
    assigned = import_pack(export_pack(assign_pack(pack, 'robot-validation-01234')))
    assert check_student(assigned, 'robot-validation-01234') == 'robot-validation-01234'
    with tempfile.TemporaryDirectory(prefix='robot-problem-check-') as directory:
        store = Store(directory)
        store.save_pack(assigned)
        jobs = Jobs(store)
        key = jobs.start(assigned['id'], exercise['id'], solution, 'robot-validation-01234')['id']
        deadline = time.monotonic() + 20
        result = jobs.get(key)
        while result['state'] != 'done' and time.monotonic() < deadline:
            time.sleep(0.05)
            result = jobs.get(key)
        assert result['state'] == 'done' and result['report']['status'] == 'passed', result
        try:
            jobs.start(assigned['id'], exercise['id'], solution, '111')
        except ValueError:
            pass
        else:
            raise AssertionError('Wrong identity accepted')
    # Keep earlier editions before updating the subject at its existing location.
    if output.exists():
        backup = output.parent / 'archives' / ('probleme-robot-avant-tikz-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
        assert output.resolve().is_relative_to(ROOT.resolve()) and backup.resolve().is_relative_to(ROOT.resolve())
        shutil.copytree(output, backup)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'professeur-probleme-robot.mrpack').write_bytes(archive)
    (output / 'SUJET.md').write_text(subject, encoding='utf-8')
    diagrams_dir = output / 'schemas-tikz'
    diagrams_dir.mkdir(exist_ok=True)
    for name, source in DIAGRAMS.items():
        (diagrams_dir / (name + '.tex')).write_text(source + '\n', encoding='utf-8')
    (output / 'code-depart.py').write_text(starter, encoding='utf-8')
    correction = '# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.\n\n' + solution + '\n\n# Vérifications\n' + '\n'.join(t['code'] for t in tests) + '\n'
    (output / 'corrige-professeur.py').write_text(correction, encoding='utf-8')
    dependencies = '\n'.join(f'| Q{q["number"]:02} | `{q["name"]}` | ' + (', '.join('`'+d+'`' for d in q['dependencies']) or 'Aucune') + ' |' for q in QUESTIONS)
    guide = GUIDE.replace('{{DEPENDENCIES}}', dependencies)
    guide += '\n## Schémas TikZJax\n\nQuatre schémas TikZ illustrent le couloir, la recharge, le trajet interrompu et les dépendances entre fonctions. Leurs sources sont dans `schemas-tikz` et dans les blocs `tikz` de l’énoncé. Utiliser la version de l’application avec le rendu TikZJax ; ses ressources sont embarquées pour le mode hors ligne. Dans une ancienne version, les blocs apparaissent comme du code. Le sujet reste compréhensible avec les tableaux et explications textuelles.\n'
    (output / 'LIRE-MOI-PROFESSEUR.md').write_text(guide, encoding='utf-8')
    validation = {'questions': 12, 'tests': 48, 'passed': report['passed'], 'points': 48,
                  'diagnostics': report['diagnostics'], 'starter_status': initial['status'],
                  'worker_status': result['report']['status'], 'worker_passed': result['report']['passed'],
                  'roundtrip': True, 'assignment_checked': True, 'wrong_identity_rejected': True, 'questions_checks': checks,
                  'tikz_diagrams': list(DIAGRAMS)}
    (output / 'validation.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding='utf-8')
    zip_path = output.parent / 'probleme-robot-chapitres-2-5-professeur.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipped:
        for path in sorted(output.rglob('*')):
            if path.is_file():
                zipped.write(path, Path(output.name) / path.relative_to(output))
    with zipfile.ZipFile(zip_path) as zipped:
        assert zipped.testzip() is None
    print(json.dumps({'pack': str(output / 'professeur-probleme-robot.mrpack'), 'zip': str(zip_path), 'tests_passed': 48}, ensure_ascii=True))


if __name__ == '__main__':
    main()
