# MrPython, moteur sans interface

Projet d’origine : https://github.com/fredokun/MrPython
Source de cette copie (compatibilité Python récent) : https://github.com/nohtyprm/MrPython
Révision : f5e1a3666c9b5890dea3f2822f0eda069734b572.

Seul le répertoire `typechecking` a été repris. La licence et les auteurs
sont conservés dans LICENSE.python et AUTHORS. Modification locale :
`prog_ast.py` et `typechecker.py` importent `astpp` relativement, sans
modifier sys.path lors de l'import de `prog_ast`.

Le lanceur, le rapport JSON et l'injection de préconditions de Runner sont
dans `runner/engine.py`. Aucun fichier IDLE, tkinter, StudentRunner, canvas
ou interface graphique MrPython n'est embarqué. Les exercices graphiques
MrPython ne sont pas pris en charge dans cette version.

Les programmes de régression du même dépôt sont conservés dans
`tests/fixtures/mrpython`, sous la licence du projet d’origine.
Cette copie est autonome : aucun sous-module ni téléchargement de MrPython
n’est nécessaire au lancement ou aux tests.
