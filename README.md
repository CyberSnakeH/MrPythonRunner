# MrPython Runner

**Créer, distribuer et résoudre des exercices Python, avec le moteur pédagogique MrPython.**

MrPython Runner est une application locale en français destinée à l’enseignement
de la programmation. Le professeur prépare une série et ses tests, puis transmet
un fichier personnel à chaque élève. L’élève écrit son programme, le teste avec
MrPython et rend ses réponses sous forme de fichier.

L’application fonctionne dans un navigateur local ou une fenêtre de bureau.
Elle n’exige ni compte en ligne ni serveur d’établissement. Après installation,
les exercices, l’éditeur, les formules et les schémas fonctionnent hors ligne.

## Fonctionnalités

- Espaces professeur et élève, séries attribuées à un identifiant.
- Exercices à écrire, compléter ou corriger ; plusieurs fonctions dans un programme.
- Énoncés Markdown, formules LaTeX avec KaTeX, images et schémas TikZ avec TikZJax.
- Éditeur Monaco avec coloration Python et sauvegarde automatique des brouillons.
- Vérification des types, préconditions et tests `assert` avec MrPython.
- Résultats par test, diagnostics, score partiel, arrêt manuel et délai d’exécution.
- Fichiers portables `.mrpack` pour les séries et `.mrwork` pour les réponses.
- Consultation des copies et recalcul des notes dans l’espace professeur.

## Démarrage rapide depuis les sources

Prérequis : **Python 3.11 ou plus récent** et **Node.js 22.12+ ou 24+**, avec npm.
Clonez le dépôt, ou téléchargez-le via **Code → Download ZIP** puis extrayez-le.
Ouvrez un terminal à la racine du projet, où se trouve `run.py`.

Sous Windows :

```powershell
python scripts/setup.py
python run.py --browser
```

Sous Linux ou macOS :

```sh
python3 scripts/setup.py
python3 run.py --browser
```

La première commande installe les dépendances JavaScript à partir du fichier
verrouillé et construit l’interface. Elle nécessite Internet. Le mode navigateur
n’a aucune dépendance Python externe : la bibliothèque standard suffit.

La seconde commande ouvre l’application sur `127.0.0.1`, uniquement sur votre
appareil. Gardez le terminal ouvert et utilisez **Ctrl+C** pour arrêter le serveur.
Aux lancements suivants, seule la seconde commande est nécessaire. Node.js n’est
plus utilisé pendant l’exécution de l’application.

**Le moteur MrPython est inclus dans ce dépôt.** Il n’y a aucun sous-module,
dépôt voisin ni installation de l’interface graphique MrPython à prévoir.

## Tester en deux minutes

1. Lancez l’application et cliquez sur **Charger une série**.
2. Choisissez [examples/eleve-01234.mrpack](examples/eleve-01234.mrpack).
3. Saisissez l’identifiant **`01234`** et cliquez sur **Commencer la série**.
4. Pour le premier exercice, remplacez `return 0` par `return n * n`.
5. Cliquez sur **Tester mon code**, puis **Rendre mes réponses** pour exporter
   votre travail.

Dans l’espace **Professeur**, la série de démonstration peut être modifiée,
testée et distribuée avec un autre identifiant. Un modèle professeur non attribué
ne peut pas être ouvert comme une série élève.

## Utiliser une distribution de bureau

Lorsqu’une distribution est fournie dans les **Releases** du dépôt, téléchargez
l’archive correspondant à votre système et à votre architecture. Les builds de
développement sont aussi disponibles dans les artefacts du workflow
**Distributions de bureau** de GitHub Actions après une exécution réussie.

| Système | Lancement | Prérequis de la fenêtre native |
|---|---|---|
| Windows | Extraire tout le dossier, ouvrir `MrPythonRunner.exe` | Microsoft Edge WebView2 |
| Linux | Extraire tout le dossier, lancer `./MrPythonRunner` | Bibliothèques Qt/WebEngine et session graphique |
| macOS | Ouvrir `MrPythonRunner.app` | Version et architecture compatibles avec le build |

Conservez le dossier entier : le worker et les ressources accompagnant le
lanceur sont indispensables. Une distribution embarque Python et l’interface
compilée ; Node.js n’est pas nécessaire. Les exécutables actuels ne sont pas
signés ou notariés. Un `.exe` Windows ne fonctionne pas sous Linux ou macOS.

Le mode navigateur depuis les sources est le parcours commun aux trois systèmes.
Le code et les workflows prévoient ces systèmes ; les vérifications locales ont
été effectuées sous Windows. Les autres distributions doivent être validées sur
leurs machines cibles avant diffusion.

## Préparer des cours

Le professeur crée une série, rédige ses énoncés, ajoute le code de départ et les
tests, puis utilise **Essayer l’exercice** pour vérifier une solution. Avec
**Distribuer à un élève**, il saisit l’identifiant choisi et exporte le `.mrpack`
personnel. L’élève importe ce fichier, saisit cet identifiant et commence la série.

Les réponses sont rendues en `.mrwork`. Le professeur conserve son modèle,
ouvre les copies reçues et recalcule les notes avec ses propres tests.

Des contenus prêts à importer sont inclus :

- [Série de démonstration](examples/premiers-pas.mrpack) : trois exercices.
- [Banque des chapitres 2 à 5](exercices/cours2022-chapitres-2-5/LIRE-MOI-PROFESSEUR.md) :
  60 exercices répartis en 12 séries.
- [Problème du robot de livraison](exercices/probleme-robot-chapitres-2-5/LIRE-MOI-PROFESSEUR.md) :
  12 questions liées dans un même programme, avec quatre schémas TikZ.

Les dossiers pédagogiques contiennent aussi les corrigés destinés au professeur.
Pour les élèves, distribuez les fichiers personnels exportés depuis l’application.

## Documentation

- [Guide professeur et élève, LaTeX et TikZ](docs/utilisation.md)
- [Formats de fichiers et sauvegardes](docs/formats.md)
- [Installation native, développement et distributions](docs/developpement.md)
- [Exécution du code et limites](docs/execution.md)
- [Contribuer au projet](CONTRIBUTING.md)

Les données restent sur l’appareil, dans le dossier de données utilisateur de
MrPython Runner. Exportez vos séries et vos réponses pour les déplacer ou les
sauvegarder. `--data-dir chemin` permet de choisir un autre emplacement.

## Limites à connaître

MrPython accepte un sous-ensemble pédagogique de Python. Les exercices graphiques
de MrPython et `input()` interactif ne sont pas pris en charge.

L’exécution se fait dans un processus distinct avec des limites de ressources,
mais **ce n’est pas un bac à sable de sécurité** : le code dispose des droits
de l’utilisateur. N’exécutez que des sujets et copies de confiance.

L’identifiant du fichier constitue un contrôle local d’attribution, pas une
authentification sécurisée. Les tests masqués restent lisibles dans l’archive
distribuée. Le logiciel n’est pas conçu comme une plateforme d’examen inviolable.

## Développement

Après le démarrage rapide :

```sh
python -m unittest discover -s tests -v
python scripts/check_upstream.py
```

La première commande couvre l’application ; la seconde vérifie les 118 programmes
de régression MrPython inclus dans le dépôt. Sous Linux/macOS, utilisez `python3`
si la commande `python` n’est pas disponible.

```text
frontend/                  Interface React/TypeScript et ressources web
runner/                    Serveur local, exécution, formats et stockage SQLite
runner/vendor/mrpython/    Moteur MrPython autonome, licence et provenance
examples/                  Série et fichier élève de démonstration
exercices/                 Sujets, séries, schémas et corrigés pédagogiques
tests/                     Tests de l’application et programmes MrPython
scripts/                   Installation, génération et construction
docs/                      Documentation d’utilisation et de développement
.github/workflows/         Vérifications et distributions multiplateformes
```

## Licence et crédits

Le code original de MrPython Runner est distribué sous **GPL-3.0-or-later** :
voir [LICENSE](LICENSE). Les contributions sont proposées sous cette même licence.

Le moteur provient de [MrPython](https://github.com/fredokun/MrPython), avec les
adaptations de compatibilité du [fork nohtyprm](https://github.com/nohtyprm/MrPython).
Sa licence, ses auteurs et la révision embarquée sont conservés dans
[sa notice](runner/vendor/mrpython/NOTICE.md). Les composants tiers conservent
leurs licences respectives ; voir [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
