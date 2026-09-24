# Installation et développement

## Construire l’interface

Le dépôt contient tout le code MrPython nécessaire. Python 3.11+ et Node.js
22.12+ (ou 24+) sont requis pour préparer l’interface. Depuis la racine :

```sh
python scripts/setup.py
python run.py --browser
```

Sous Linux/macOS, remplacer `python` par `python3` si nécessaire. Le script
d’installation lance `npm ci` puis `npm run build` dans `frontend`. Après une
modification de l’interface, `npm run build` suffit ; après une modification du
fichier verrouillé, relancer le script d’installation.

Les ressources de Monaco, KaTeX et TikZJax sont servies localement. La commande
`prebuild` copie le moteur TeX/WebAssembly et les polices de TikZJax depuis son
paquet npm. Le répertoire `frontend/public/vendor` est généré et n’est pas versionné.

Le mode navigateur utilise seulement la bibliothèque standard Python. Il est
normal de ne pas avoir de fichier `requirements.txt` pour ce mode.

## Fenêtre native depuis les sources

Construire d’abord l’interface avec la procédure ci-dessus.

### Windows

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -e ".[desktop]"
.venv/Scripts/python.exe run.py
```

Microsoft Edge WebView2 doit être installé pour la fenêtre native.

### macOS

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[desktop]'
.venv/bin/python run.py
```

La fenêtre utilise WebKit.

### Linux

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[desktop]' 'pywebview[qt]>=6,<7'
PYWEBVIEW_GUI=qt .venv/bin/python run.py
```

Les bibliothèques système de Qt/WebEngine et une session graphique sont nécessaires.
Leur installation dépend de la distribution. En cas de dépendance graphique
manquante, le mode `--browser` permet d’utiliser l’application sans pywebview.

## Vérifier le projet

Après construction de l’interface :

```sh
python -m unittest discover -s tests -v
python scripts/check_upstream.py
python scripts/smoke_bundle.py --source
```

Ces commandes vérifient respectivement le moteur et l’application, les 118
programmes de régression MrPython, puis le lancement réel du serveur et du worker.
Le dernier contrôle utilise un dossier temporaire sans toucher aux données utilisateur.
Les tests de l’interface compilée ne doivent pas être ignorés faute de build.

Le workflow `ci.yml` construit l’interface et vérifie le mode navigateur sous
Windows, Linux et macOS, avec Python 3.11 et 3.14. Les résultats des exécutions
GitHub Actions font foi pour chaque environnement.

## Construire une distribution

Dans l’environnement virtuel du système cible :

```sh
python -m pip install -e '.[desktop,build]'
python scripts/build_desktop.py
python scripts/archive_desktop.py
```

Sous Linux, installer également `pywebview[qt]>=6,<7`. Le script de construction
compile l’interface, exécute les tests, regroupe les licences, lance PyInstaller
et vérifie le worker ainsi que le serveur embarqués. Les fichiers sont produits
dans `dist/`. `archive_desktop.py` produit un ZIP Windows ou un TAR.GZ Linux/macOS
qui conserve les permissions des exécutables.

Un build doit être effectué pour chaque système et architecture : PyInstaller
ne fait pas de compilation croisée. Les distributions ne sont pas signées ou
notariées. Tester aussi la fenêtre native et ses dialogues sur les machines cibles.

Sur GitHub, le workflow **Distributions de bureau** se lance manuellement depuis
**Actions**, ou lors de la publication d’un tag `v*`. Il produit des artefacts
téléchargeables ; il ne publie pas automatiquement de Release.

## Contenus pédagogiques

Les sujets utilisables sont déjà versionnés dans `exercices/`. Pour les régénérer :

```sh
python scripts/create_course2022.py
python scripts/create_robot_problem.py
```

Les générateurs vérifient les corrigés et les attributions avant de produire
les fichiers. Ils conservent une archive de la version précédente dans
`exercices/archives/` et génèrent un ZIP professeur. Ces archives locales et les
rapports temporaires ne sont pas destinés au dépôt. Les sources TikZ du problème
sont définies dans `scripts/robot_diagrams.py`.

## Dépannage

| Symptôme | Action |
|---|---|
| « Interface absente » | Exécuter `python scripts/setup.py` depuis la racine. |
| Commande `python` introuvable | Essayer `python3` sur Linux/macOS ou `py` sous Windows. |
| Node.js/npm introuvable | Installer Node.js et rouvrir le terminal. |
| Une erreur d’installation npm | Vérifier la connexion, les paramètres de proxy et la version Node.js. |
| Le navigateur ne s’ouvre pas | Copier l’URL complète affichée dans le terminal, y compris son fragment de session. |
| La fenêtre native ne démarre pas | Utiliser `--browser` et vérifier WebView2 ou les bibliothèques Qt. |
| Le modèle professeur est refusé à l’élève | Attribuer le modèle via « Distribuer à un élève », puis importer le fichier exporté. |
| Les schémas TikZ apparaissent comme du code | Mettre à jour l’application, reconstruire l’interface et recharger la page. |

Le serveur écoute uniquement `127.0.0.1`. Il n’est pas destiné à être exposé sur
Internet. Les détails des protections et de leurs limites sont dans
[Exécution du code](execution.md).
