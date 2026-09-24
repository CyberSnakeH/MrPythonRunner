# Problème — Un robot de livraison dans un couloir

Une médiathèque utilise un petit robot pour transporter des documents le long d’un couloir. Avant de le brancher au matériel, vous devez construire son simulateur : prévoir la recharge, interpréter les commandes, arrêter proprement un trajet impossible et produire un compte rendu.

Le robot se trouve sur un axe de positions entières, positives ou négatives. Il possède une quantité entière d’énergie. Il ne se recharge jamais pendant un trajet ; la borne de recharge sera simulée séparément aux questions 4 et 5.

| Commande | Déplacement | Coût en énergie |
|---|---|---|
| `A` | Une case vers les positions croissantes | 2 |
| `R` | Une case vers les positions décroissantes | 1 |
| `P` | Aucun déplacement | 0 |

Un programme tel que `APAR` désigne quatre commandes successives. Les espaces ne sont pas des séparateurs autorisés. Sur le terrain, une commande inconnue ou trop coûteuse arrête le trajet avant son exécution ; aucune commande suivante n’est essayée.



```tikz
% Le couloir : une case par déplacement
\begin{tikzpicture}[x=0.95cm,y=1cm,font=\small]
\definecolor{vert}{RGB}{53,102,81}
\definecolor{bleu}{RGB}{59,105,153}
\draw[->,gray,thick] (-2.7,0) -- (2.8,0);
\foreach \x in {-2,-1,0,1,2} {
  \draw[gray] (\x,-0.09) -- (\x,0.09);
  \node[below] at (\x,-0.1) {$\x$};
}
\draw[fill=vert!12,draw=vert,rounded corners=2pt] (-0.3,0.2) rectangle (0.3,0.7);
\fill[vert] (-0.2,0.16) circle (0.07);
\fill[vert] (0.2,0.16) circle (0.07);
\node[above,text=vert] at (0,0.85) {Robot au d\'epart};
\draw[->,very thick,vert] (0.15,1.65) -- (2.1,1.65)
  node[midway,above,align=center] {A : $+1$ case\\2 unit\'es};
\draw[->,very thick,bleu] (-0.15,1.65) -- (-2.1,1.65)
  node[midway,above,align=center] {R : $-1$ case\\1 unit\'e};
\node[below,align=center] at (0,-0.65) {P : rester sur place\\0 unit\'e d'\'energie};
\end{tikzpicture}
```

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


## Question 1 — Fixer le coût d’une action · 4 points

Le service technique définit trois commandes : `A` fait avancer le robot et coûte **2 unités** d’énergie ; `R` le fait reculer et coûte **1 unité** ; `P` le laisse en place et coûte **0 unité**. Écrivez `cout_action`. Toute autre chaîne, y compris une minuscule, la chaîne vide ou une chaîne de plusieurs caractères, doit donner `-1`. La valeur négative signale une commande inconnue et ne représente jamais une recharge.

```python
def cout_action(action: str) -> int:
```

**Données :** toute valeur respectant les types de la signature est autorisée.

- `cout_action('A')` renvoie `2`. Avancer consomme deux unités.
- `cout_action('a')` renvoie `-1`. Une minuscule ne désigne pas une commande reconnue.


## Question 2 — Autoriser une action · 4 points

Le robot ne doit jamais commencer une action qu’il ne peut pas terminer. Écrivez un prédicat qui utilise le coût calculé à la question 1. Une action est possible seulement si elle est reconnue et si son coût ne dépasse pas l’énergie disponible. Une pause reste possible avec une batterie vide. Une commande inconnue doit être refusée, même si son coût conventionnel vaut −1.

```python
def action_possible(energie: int, action: str) -> bool:
```

**Précondition :** `energie >= 0`.

**Fonctions à réutiliser :** `cout_action`. Ne recopiez pas leur logique.

- `action_possible(2, 'A')` renvoie `True`. Les deux unités disponibles paient exactement l’avance.
- `action_possible(0, 'P')` renvoie `True`. La batterie est vide, mais une pause ne consomme rien.


## Question 3 — Mettre à jour la position · 4 points

Le couloir est un axe entier sans obstacle : les positions négatives sont autorisées. Une avance `A` augmente la position de **1**, un recul `R` la diminue de **1**, et une pause `P` la laisse inchangée. Pour toute commande inconnue, conservez aussi la position. Cette fonction s’occupe uniquement du déplacement : le contrôle d’énergie sera assuré par les fonctions suivantes. Attention : avancer coûte deux unités d’énergie mais ne déplace que d’une case.

```python
def position_apres(position: int, action: str) -> int:
```

**Données :** toute valeur respectant les types de la signature est autorisée.

- `position_apres(-2, 'A')` renvoie `-1`. Depuis la case −2, une avance mène à −1.
- `position_apres(0, 'R')` renvoie `-1`. Un recul depuis l’origine mène à la case −1.


## Question 4 — Simuler une minute de recharge · 4 points

Au dépôt, la borne apporte `gain` unités par minute entière. La batterie ne peut pas dépasser sa `capacite` : tout surplus fourni pendant la dernière minute est perdu. Écrivez une fonction qui calcule l’énergie après une seule minute. Une batterie déjà pleine conserve sa charge. Une capacité nulle est autorisée et conduit toujours à zéro. Utilisez une variable intermédiaire et une alternative, sans modifier les paramètres.

```python
def recharger(energie: int, capacite: int, gain: int) -> int:
```

**Précondition :** `0 <= energie <= capacite and gain > 0`.

- `recharger(8, 10, 3)` renvoie `10`. La recharge propose 11 unités, mais la batterie est limitée à 10.
- `recharger(2, 10, 3)` renvoie `5`. L’apport tient entièrement dans la batterie : 2 + 3 = 5.




```tikz
% Recharge : de 2 à au moins 8 unités
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
\definecolor{vert}{RGB}{53,102,81}
\foreach \x/\niveau/\temps in {0/2/0,2/5/1,4/8/2} {
  \fill[vert!25] (\x,0) rectangle (\x+0.8,\niveau/5);
  \draw[thick,vert] (\x,0) rectangle (\x+0.8,2);
  \draw[thick,vert] (\x+0.25,2) -- (\x+0.25,2.1) -- (\x+0.55,2.1) -- (\x+0.55,2);
  \node at (\x+0.4,0.3) {$\niveau$};
  \node[below] at (\x+0.4,-0.15) {$t=\temps$ min};
}
\draw[->,thick,vert] (0.95,1) -- (1.85,1) node[midway,above] {$+3$};
\draw[->,thick,vert] (2.95,1) -- (3.85,1) node[midway,above] {$+3$};
\draw[dashed,gray] (-0.2,1.6) -- (5,1.6);
\node[above,align=center] at (2.4,2.4) {Capacit\'e : 10\quad Cible : 8};
\node[below,text=vert] at (2.4,-0.8) {La cible est atteinte apr\`es 2 minutes.};
\end{tikzpicture}
```

## Question 5 — Préparer la batterie avant le départ · 4 points

Le chef de mission demande une charge d’au moins `cible` unités avant le départ. Simulez des minutes successives avec une boucle **while**, en appelant `recharger` à chaque tour. Arrêtez-vous dès que la charge atteint ou dépasse la cible ; il n’est pas nécessaire d’obtenir une égalité exacte. Si la charge initiale suffit déjà, le résultat vaut zéro. La cible ne dépasse jamais la capacité : elle peut donc être atteinte.

```python
def minutes_recharge(energie: int, capacite: int, gain: int, cible: int) -> int:
```

**Précondition :** `0 <= energie <= capacite and gain > 0 and 0 <= cible <= capacite`.

**Fonctions à réutiliser :** `recharger`. Ne recopiez pas leur logique.

- `minutes_recharge(2, 10, 3, 8)` renvoie `2`. Les charges successives sont 2, 5 puis 8 : il faut deux minutes.
- `minutes_recharge(9, 10, 3, 8)` renvoie `0`. La charge initiale dépasse déjà la cible : aucun temps d’attente.

**À justifier en commentaire :** Que représente `charge` après k tours ? Pourquoi une recharge augmente-t-elle strictement la charge tant que la cible n’est pas atteinte ? Raisonnez sur le déficit positif jusqu’à la cible pour établir la terminaison.


## Question 6 — Rejoindre un point aussi loin que possible · 4 points

Avant de programmer un trajet complet, on étudie une livraison située `distance` cases plus loin. Le robot effectue uniquement des commandes `A`, tant qu’il reste une case à parcourir et que sa batterie permet une nouvelle avance. Écrivez cette simulation avec **while** et retournez le nombre d’avances réellement effectuées. Ne confondez pas la distance atteinte et l’énergie dépensée. La fonction ne recharge jamais la batterie et ne permet pas une avance partiellement payée.

```python
def avancer_au_maximum(energie: int, distance: int) -> int:
```

**Précondition :** `energie >= 0 and distance >= 0`.

**Fonctions à réutiliser :** `action_possible`, `cout_action`. Ne recopiez pas leur logique.

- `avancer_au_maximum(5, 4)` renvoie `2`. Cinq unités financent deux avances ; la troisième demanderait deux unités alors qu’il n’en reste qu’une.
- `avancer_au_maximum(10, 2)` renvoie `2`. Le robot s’arrête après deux avances car la destination est atteinte, même s’il reste de l’énergie.

**À justifier en commentaire :** Établissez $energie = reste + 2 \times pas$ et $0 \leq pas \leq distance$. Donnez un variant naturel, puis expliquez les deux causes possibles d’arrêt. Une formule directe ne répond pas ici à la méthode demandée.


## Question 7 — Vérifier le programme reçu · 4 points

Un programme est une chaîne : chaque caractère représente une action, exécutée de gauche à droite. Vérifiez que tous les caractères sont reconnus par `cout_action`, à l’aide d’un parcours **for**. Dès qu’un caractère inconnu apparaît, retournez False. La chaîne vide est un programme valide qui ne demande aucune action. Les espaces et les minuscules sont interdits : ne nettoyez pas le programme silencieusement.

```python
def programme_valide(programme: str) -> bool:
```

**Données :** toute valeur respectant les types de la signature est autorisée.

**Fonctions à réutiliser :** `cout_action`. Ne recopiez pas leur logique.

- `programme_valide('APRA')` renvoie `True`. Les quatre caractères A, P, R, A sont tous reconnus.
- `programme_valide('A R')` renvoie `False`. L’espace fait partie de la chaîne et rend le programme invalide.

**À justifier en commentaire :** Expliquez pourquoi la première commande inconnue suffit pour conclure, sans parcourir la suite.


## Question 8 — Prévoir l’énergie du trajet entier · 4 points

Le dépôt veut calculer le besoin énergétique théorique avant de choisir une batterie. Additionnez les coûts des actions avec **for** en réutilisant `cout_action`. Si une seule commande est inconnue, retournez `-1`, quel que soit le coût déjà accumulé. Il n’y a ici aucune limite de batterie : on calcule le coût de tout le programme. Le programme vide et un programme ne contenant que des pauses coûtent zéro.

```python
def energie_programme(programme: str) -> int:
```

**Données :** toute valeur respectant les types de la signature est autorisée.

**Fonctions à réutiliser :** `cout_action`. Ne recopiez pas leur logique.

- `energie_programme('APRA')` renvoie `5`. Les coûts sont 2 + 0 + 1 + 2, soit cinq unités.
- `energie_programme('AAX')` renvoie `-1`. Le caractère X invalide tout le calcul, même après deux commandes connues.




```tikz
% APAR : s’arrêter avant la commande impossible
\begin{tikzpicture}[font=\small,
etat/.style={draw,rounded corners=3pt,minimum width=2.8cm,minimum height=0.8cm,align=center},
fleche/.style={->,thick}]
\definecolor{vert}{RGB}{53,102,81}
\definecolor{rouge}{RGB}{160,63,48}
\node[etat,draw=vert,fill=vert!8] (debut) at (0,0) {D\'epart\\position 10 ; \'energie 3};
\node[etat,draw=vert,fill=vert!8] (avance) at (0,-1.7) {A ex\'ecut\'ee\\position 11 ; \'energie 1};
\node[etat,draw=vert,fill=vert!8] (pause) at (0,-3.4) {P ex\'ecut\'ee\\position 11 ; \'energie 1};
\node[etat,draw=rouge,fill=rouge!6] (arret) at (0,-5.1) {A refus\'ee : $1<2$\\Arr\^et d\'efinitif};
\draw[fleche,vert] (debut) -- (avance) node[midway,right] {co\^ut 2};
\draw[fleche,vert] (avance) -- (pause) node[midway,right] {co\^ut 0};
\draw[fleche,rouge] (pause) -- (arret) node[midway,right] {\'energie insuffisante};
\node[align=center,text=rouge] at (0,-6.3) {R n'est jamais essay\'ee.};
\node[align=center,text=vert] at (0,-7.1) {Pr\'efixe ex\'ecut\'e : AP};
\end{tikzpicture}
```

## Question 9 — Conserver exactement les actions exécutées · 4 points

Sur le terrain, le robot lit les commandes dans l’ordre. Avant chaque action, il vérifie qu’elle est reconnue et entièrement finançable avec l’énergie restante. Au premier refus, il s’arrête **définitivement** : il ne saute pas la commande pour essayer les suivantes. Retournez la chaîne exacte des actions effectuées avant cet arrêt. Une pause reconnue est incluse même si la batterie est vide. Contrairement à la question 8, une commande inconnue n’annule pas les actions déjà effectuées.

```python
def prefixe_executable(programme: str, energie: int) -> str:
```

**Précondition :** `energie >= 0`.

**Fonctions à réutiliser :** `action_possible`, `cout_action`. Ne recopiez pas leur logique.

- `prefixe_executable('APAR', 3)` renvoie `'AP'`. Après A, il reste une unité ; P est exécutée gratuitement. La seconde A est refusée et R n’est jamais essayée.
- `prefixe_executable('PXAR', 9)` renvoie `'P'`. La première pause est effectuée avant de rencontrer X ; la suite est abandonnée.

**À justifier en commentaire :** Expliquez pourquoi le résultat est toujours un préfixe valide du programme et pourquoi l’énergie restante ne devient jamais négative. Le nombre de caractères non encore lus fournit une borne au nombre de tours.


## Question 10 — Localiser le robot après son arrêt · 4 points

Le suivi de livraison doit afficher la position réelle du robot, même si son trajet a été interrompu. Commencez par obtenir le préfixe de la question 9. Partez ensuite de `depart` et appliquez `position_apres` à chacun des caractères de ce préfixe avec **for**. Les positions négatives restent autorisées. Un programme vide ou une première action refusée laisse le robot au départ. Ne reparcourez pas les commandes situées après l’arrêt.

```python
def position_finale(programme: str, energie: int, depart: int) -> int:
```

**Précondition :** `energie >= 0`.

**Fonctions à réutiliser :** `prefixe_executable`, `position_apres`. Ne recopiez pas leur logique.

- `position_finale('APAR', 3, 10)` renvoie `11`. Avec trois unités, seules A et P sont exécutées : depuis 10, le robot arrive à 11.
- `position_finale('RR', 2, 0)` renvoie `-2`. Deux reculs consomment les deux unités et déplacent le robot de 0 à −2.


## Question 11 — Établir le bilan énergétique · 4 points

Le technicien doit savoir si le robot possède encore de l’énergie après sa mission. Obtenez le préfixe réellement exécuté avec `prefixe_executable`, puis calculez son coût avec `energie_programme`. Soustrayez ce coût à l’énergie initiale. Cette question ne demande aucune nouvelle boucle. Une interruption n’implique pas forcément une batterie vide : une unité restante ne permet pas une avance, mais elle reste bien dans la batterie.

```python
def energie_restante(programme: str, energie: int) -> int:
```

**Précondition :** `energie >= 0`.

**Fonctions à réutiliser :** `prefixe_executable`, `energie_programme`. Ne recopiez pas leur logique.

- `energie_restante('APAR', 3)` renvoie `1`. A et P coûtent deux unités ; il en reste une sur les trois disponibles.
- `energie_restante('XA', 5)` renvoie `5`. X est refusée immédiatement : aucune des cinq unités n’a été consommée.

**À justifier en commentaire :** Pourquoi energie_programme ne peut-elle pas renvoyer −1 lorsqu’elle reçoit le préfixe exécutable ? Pourquoi le résultat appartient-il à l’intervalle de zéro à l’énergie initiale ?




```tikz
% Les fonctions se construisent les unes sur les autres
\begin{tikzpicture}[font=\small,
bloc/.style={draw,rounded corners=2pt,align=center,inner sep=6pt},
lien/.style={->,thick,draw=black!55}]
\definecolor{vert}{RGB}{53,102,81}
\node[bloc] (cout) at (0,0) {Q1\\\texttt{cout\_action}};
\node[bloc] (possible) at (0,-1.35) {Q2\\\texttt{action\_possible}};
\node[bloc,draw=vert,fill=vert!8] (prefixe) at (0,-2.7) {Q9\\\texttt{prefixe\_executable}};
\node[bloc] (position) at (-1.9,-4.2) {Q10\\\texttt{position\_finale}};
\node[bloc] (energie) at (1.9,-4.2) {Q11\\\texttt{energie\_restante}};
\node[bloc,draw=vert,fill=vert!8] (bilan) at (0,-5.8) {Q12\\\texttt{bilan\_mission}};
\draw[lien] (cout) -- (possible);
\draw[lien] (possible) -- (prefixe);
\draw[lien] (prefixe) -- (position);
\draw[lien] (prefixe) -- (energie);
\draw[lien] (position) -- (bilan);
\draw[lien] (energie) -- (bilan);
\end{tikzpicture}
```

Une flèche signifie que la fonction du bas utilise celle du haut. Cette vue est simplifiée : tous les appels à réutiliser restent indiqués dans chaque question.

## Question 12 — Produire le compte rendu de mission · 4 points

Vous devez maintenant réunir les fonctions dans un compte rendu. **Validez d’abord tout le programme** : s’il contient une commande inconnue, retournez uniquement `INVALIDE`, même si la batterie aurait arrêté le robot avant de la rencontrer. Sinon, construisez trois champs séparés par des points-virgules, sans espace :

1. `TERMINE` si toutes les commandes ont pu être exécutées, sinon `BLOQUE`. Comparez la longueur du préfixe exécutable à celle du programme.
2. `AVANT` si la position finale est strictement supérieure au départ, `ARRIERE` si elle lui est inférieure, sinon `SUR_PLACE`. Il s’agit du déplacement final, pas du sens de la dernière commande.
3. `VIDE` si l’énergie restante est nulle, sinon `RESTE`.

Un programme vide est terminé, laisse le robot sur place et conserve sa batterie. Une mission peut être terminée avec une batterie vide, ou bloquée avec de l’énergie restante. Réutilisez les fonctions existantes et concaténez les trois champs : aucune conversion de nombre en texte ni nouvelle boucle n’est nécessaire.

```python
def bilan_mission(programme: str, energie: int, depart: int) -> str:
```

**Précondition :** `energie >= 0`.

**Fonctions à réutiliser :** `programme_valide`, `prefixe_executable`, `position_finale`, `energie_restante`. Ne recopiez pas leur logique.

- `bilan_mission('ARP', 3, 0)` renvoie `'TERMINE;SUR_PLACE;VIDE'`. Le robot termine l’aller-retour et la pause, revient au départ et dépense ses trois unités.
- `bilan_mission('APAR', 3, 10)` renvoie `'BLOQUE;AVANT;RESTE'`. Il effectue A et P, reste une case devant son départ et conserve une unité inutilisable pour l’avance suivante.

**À justifier en commentaire :** Cette version privilégie la décomposition mais recalcule plusieurs fois le préfixe. Identifiez ces appels dans vos commentaires et expliquez pourquoi leur résultat reste identique. Il n’est pas demandé d’introduire des tuples ou de modifier les signatures pour optimiser ces appels.
