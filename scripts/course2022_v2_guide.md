# Nouvelle banque professeur — chapitres 2 à 5

Cette édition remplace les 60 exercices de la première banque par 60 nouveaux problèmes rédigés pour l’application. Elle s’appuie sur les notions du cours, sans reprendre ses énoncés ou ses démonstrations comme exercices à rendre. Les algorithmes d’initiation restent naturellement proches des schémas étudiés : accumulateur, parcours, invariant, recherche et transformation.

Source pédagogique : *Éléments de Programmation (en Python)*, Frédéric Peschanski et Romain Demangeon, document fourni `cours2022.pdf`. Les pages citées sont les numéros imprimés, pas le compteur du lecteur PDF.

## Contenu et progression

Les 12 séries comportent chacune 5 exercices : 3 fonctions à écrire, 1 programme à compléter et 1 programme à corriger. Chaque énoncé comporte une situation, un objectif précis, les paramètres et règles de calcul, une signature, deux exemples expliqués, les préconditions et les cas limites pertinents.

Cette sélection porte sur les notions principales des chapitres 2 à 5. Elle n’utilise ni `Callable`, ni récursion, ni listes, ni tuples, ni ensembles, ni dictionnaires dans les solutions. `Optional[int]` est expliqué dans l’unique exercice qui retourne un indice ou `None`. Les importations de typage nécessaires sont déjà présentes dans le code de départ.

{{PROGRESSION}}

Total : **60 exercices, {{TESTS}} tests, {{POINTS}} points**. Les deux premiers tests de chaque exercice correspondent aux exemples expliqués et sont visibles. Les autres sont masqués dans l’interface élève.

## Charger et distribuer

1. Dans l’application, choisir **Professeur**, puis **Charger une série**.
2. Importer `professeur-chapitres-2-a-5.mrpack` pour toute la banque, ou un fichier du dossier `series` pour une séance de cinq exercices.
3. Lire et, si nécessaire, adapter les énoncés et tests. Le fichier `ENONCES.md` permet aussi de lire les 60 sujets sans ouvrir l’application.
4. Utiliser **Distribuer à un élève**, saisir l’identifiant choisi par le professeur et exporter le fichier personnel.
5. L’élève importe ce fichier personnel et saisit exactement cet identifiant avant de commencer.

Le modèle professeur est volontairement non attribué : il ne permet pas d’entrer dans une série depuis l’espace élève. Le ZIP complet et les corrigés sont réservés au professeur. Aucun corrigé n’est inclus dans les `.mrpack`. Les tests masqués font partie du fichier hors ligne ; leur masquage dans l’interface ne constitue pas un chiffrement.

## Remplacement de la première édition

Les noms des fichiers principaux sont conservés. Les identifiants internes des modèles et des exercices comportent désormais `r2`, pour éviter de rattacher les anciennes réponses à des problèmes différents. Après remplacement du fichier sur le disque, **réimporter le nouveau `.mrpack` dans l’application** : les séries déjà importées sont stockées séparément et ne changent pas automatiquement.

L’ancienne édition est conservée dans le dossier voisin `archives`. Pour corriger d’anciens fichiers `.mrwork`, garder leur ancien modèle. Pour les nouvelles réponses, employer le modèle utilisé lors de la distribution : banque complète et séries séparées ont des identifiants de modèles différents.

## Conseils de correction

- Chapitre 2 : demander des variables locales annotées, une expression logique exacte et une attention aux bornes. Aucune boucle n’est nécessaire.
- Chapitre 3 : travailler `while` avant d’introduire `for` au chapitre 5. Faire tracer les états et distinguer quantité restante, quantité cumulée et nombre de tours.
- Chapitre 4 : lire les commentaires d’invariant, de variant et de justification. Les tests ne prouvent ni la correction générale, ni la terminaison, ni la complexité. Les consignes de méthode demandent une relecture humaine.
- Chapitre 5 : faire traiter les chaînes vides et protéger les accès indicés. Les espaces, la casse, les marqueurs et la ponctuation suivent exactement les règles propres à chaque problème.
- Les programmes à corriger contiennent des erreurs de logique ; tous sont syntaxiquement valides et s’exécutent sur les tests fournis. Les exercices à compléter possèdent un point de départ partiel.
- Les résultats flottants sont comparés sans arrondi avec des tolérances relative et absolue de 1e-9. Les tests respectent les préconditions.

## Corrigés et contrôles

`corriges-professeur` contient un fichier Python par exercice, avec la solution et ses tests. Pour essayer une solution dans l’application, copier la fonction et son éventuel import ; les assertions de fin servent à la vérification séparée. `JUSTIFICATIONS-CHAPITRE-4.md` propose les éléments de correction des raisonnements.

Le générateur vérifie les 60 solutions avec le moteur MrPython de l’application, les 60 codes de départ et 60 programmes retournant une réponse constante. Toutes les solutions réussissent tous leurs tests sans diagnostic MrPython ; chaque code de départ échoue à au moins un test et chaque réponse constante est rejetée. Les 13 `.mrpack` sont relus après export. L’attribution à un identifiant, le refus d’un identifiant différent et six exécutions par le processus de travail de l’application sont également vérifiés. Le détail se trouve dans `validation.json`.

Reconstruction depuis le dossier de l’application : `python scripts/create_course2022.py`. Le générateur prépare et valide l’édition avant de remplacer les fichiers livrés.
