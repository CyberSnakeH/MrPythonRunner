# Utiliser MrPython Runner

## Préparer et distribuer une série


Pour un schéma, insérer un bloc de code marqué `tikz` (ou `tikzjax`) dans
l’énoncé. Le contenu est compilé localement, puis affiché comme SVG. Exemple :

````markdown
```tikz
% Un déplacement du robot
\begin{tikzpicture}
  \draw[->,thick] (0,0) -- (3,0) node[midway,above] {Avancer};
\end{tikzpicture}
```
````

Les bibliothèques `arrows.meta`, `positioning`, `calc` et `shapes.geometric`
sont préchargées. Utiliser les commandes LaTeX d’accentuation dans les libellés
(par exemple `\'e`). Le premier commentaire sert de légende. Le rendu se lance
à proximité de la zone visible, se met à jour après une courte pause de saisie
et s’arrête après 20 secondes en cas de dessin invalide ou trop coûteux.
Un lien « Voir le code TikZ » garde la source accessible. La compilation utilise
un worker séparé et les SVG sont nettoyés avant affichage ; le HTML arbitraire
des énoncés reste désactivé.

1. Choisir **Professeur**, puis **Créer une série**.
2. Renseigner le titre, l'auteur et les consignes générales via **Série**.
3. Préparer chaque énoncé, éventuellement avec `$x^2$`, `$$…$$` et des images.
4. Définir le code de départ et au moins un test `assert` par exercice.
5. Utiliser **Essayer l'exercice** pour valider les tests avec une solution.
6. **Distribuer à un élève**, renseigner son identifiant (ex. `01234`), puis
   **Exporter le fichier élève**. Transmettre ce `.mrpack` à cet élève et lui
   communiquer son identifiant. Répéter l’export pour chaque élève.
7. **Ouvrir une copie** `.mrwork`, puis **Recalculer les notes** pour corriger
   avec les tests de la série actuellement ouverte.

Le modèle professeur reste dans l’application ; chaque élève reçoit une copie
distincte en lecture seule. Dans la fenêtre de distribution, **Sauvegarder le
modèle professeur** permet de conserver le modèle `.mrpack` sur un autre appareil.
Conservez ce modèle pour ouvrir les copies rendues et recalculer les notes.
Un identifiant est du texte : `01234` diffère de `1234`, et `Alice` de `alice`.
Seuls les espaces au début et à la fin sont ignorés.

Les brouillons professeur sont sauvegardés automatiquement. Une série
incomplète peut être sauvegardée, mais l'export exige des exercices avec des
tests syntaxiquement valides. Chaque test doit contenir un `assert` au niveau
principal, et ne doit pas absorber les échecs d'assertion. Les tests restent du
code professeur : leur pertinence doit être vérifiée avec la solution d'essai.

## Parcours élève

1. **Charger une série** avec le fichier personnel reçu du professeur, puis
   l’écran **Entrez l’identifiant fourni par votre professeur** s’affiche.
   Saisir l’identifiant attribué et cliquer **Commencer la série**. Le champ
   reste vide à chaque import, même après une session précédente ; un
   identifiant différent est refusé et les exercices restent inaccessibles.
2. Écrire sa solution et cliquer **Tester mon code**.
3. Retrouver ses brouillons sur ce même appareil avec le même identifiant.
4. **Rendre mes réponses** exporte un fichier `.mrwork` à transmettre.
5. Sur un autre appareil, charger d'abord la même série, saisir son identifiant puis utiliser
   **Reprendre** avec son `.mrwork`.

Attendez l'indication de sauvegarde avant de fermer. Le fichier `.mrpack`
ne contient jamais les réponses ; exporter un sujet ne sauvegarde donc pas
les solutions de l'élève. Aucune transmission automatique n'est effectuée.
L’identifiant est demandé à chaque ouverture ou changement de série. Les modèles,
y compris les séries de démonstration et anciens fichiers non attribués, sont
inaccessibles dans l’espace élève ; le professeur doit passer par **Distribuer à
un élève** pour les attribuer. Il peut toujours essayer ses exercices depuis
l’espace professeur. Le fichier `examples/eleve-01234.mrpack` permet de tester
le parcours élève avec l’identifiant `01234` ; `111` est refusé.
