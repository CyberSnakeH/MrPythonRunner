# Formats et sauvegardes


Un `.mrpack` est un ZIP versionné contenant `manifest.json` et des images
dans `assets/`. Les IDs stables relient les réponses à la série et à chaque
exercice. Le fichier JSON d'exemple documente le schéma complet.
La version 1 correspond au modèle non attribué ; la version 2 ajoute
`assignment: {source_pack_id, student_id}`. L’ID de la copie est stable pour un
couple modèle/élève, et différent de celui du modèle et des autres élèves.
Les anciennes versions de l’application doivent être mises à jour pour lire
ces fichiers attribués.

Un `.mrwork` est un ZIP contenant `submission.json` : identifiant élève,
empreinte de la série, codes soumis et résultats locaux indicatifs. Le
professeur recalcule les notes ; l'application ne fait pas confiance aux
résultats contenus dans ce fichier.
La version 2 ajoute `source_pack_id`, permettant au professeur de rattacher les
réponses au modèle original sans importer le fichier élève.

Les imports vérifient le format, les tailles et les noms ; aucun fichier
d'archive n'est extrait ni exécuté lors de l'import. Une série de même ID
mais de contenu différent demande confirmation avant remplacement.

Les bases locales sont enregistrées dans :

- Windows : `%LOCALAPPDATA%/MrPythonRunner/runner.sqlite3`
- macOS : `~/Library/Application Support/MrPythonRunner/runner.sqlite3`
- Linux : `${XDG_DATA_HOME:-~/.local/share}/MrPythonRunner/runner.sqlite3`

`python run.py --data-dir chemin` permet de choisir un autre dossier.
Sauvegardez ce dossier application fermée, ou exportez les séries et réponses.
