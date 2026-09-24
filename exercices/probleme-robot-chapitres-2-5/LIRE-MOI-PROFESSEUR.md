# Guide professeur — Un robot de livraison

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
| Q01 | `cout_action` | Aucune |
| Q02 | `action_possible` | `cout_action` |
| Q03 | `position_apres` | Aucune |
| Q04 | `recharger` | Aucune |
| Q05 | `minutes_recharge` | `recharger` |
| Q06 | `avancer_au_maximum` | `action_possible`, `cout_action` |
| Q07 | `programme_valide` | `cout_action` |
| Q08 | `energie_programme` | `cout_action` |
| Q09 | `prefixe_executable` | `action_possible`, `cout_action` |
| Q10 | `position_finale` | `prefixe_executable`, `position_apres` |
| Q11 | `energie_restante` | `prefixe_executable`, `energie_programme` |
| Q12 | `bilan_mission` | `programme_valide`, `prefixe_executable`, `position_finale`, `energie_restante` |

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

## Schémas TikZJax

Quatre schémas TikZ illustrent le couloir, la recharge, le trajet interrompu et les dépendances entre fonctions. Leurs sources sont dans `schemas-tikz` et dans les blocs `tikz` de l’énoncé. Utiliser la version de l’application avec le rendu TikZJax ; ses ressources sont embarquées pour le mode hors ligne. Dans une ancienne version, les blocs apparaissent comme du code. Le sujet reste compréhensible avec les tableaux et explications textuelles.
