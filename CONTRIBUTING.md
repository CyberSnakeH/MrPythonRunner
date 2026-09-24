# Contribuer

Les corrections, améliorations de l’interface et nouveaux exercices sont les
bienvenus. Pour un changement important, ouvrir une issue décrivant le problème
et le comportement attendu avant de commencer.

## Environnement

Installer Python 3.11+ et Node.js 22.12+ ou 24+, puis suivre le
[guide de développement](docs/developpement.md). Le moteur MrPython est inclus ;
aucun sous-module n’est nécessaire.

## Proposer une modification

1. Créer une branche dédiée à un changement cohérent.
2. Conserver les textes d’interface en français et les types TypeScript stricts.
3. Ajouter une vérification ciblée lorsqu’un comportement fonctionnel change.
4. Construire l’interface et lancer les contrôles ci-dessous.
5. Décrire dans la pull request le problème résolu, le résultat et les vérifications.

```sh
python scripts/setup.py
python -m unittest discover -s tests -v
python scripts/check_upstream.py
python scripts/smoke_bundle.py --source
```

Ne pas versionner de bases utilisateur, copies d’élèves, environnements virtuels,
paquets installés, caches ou distributions compilées. Utiliser des identifiants
fictifs dans les exemples et les tests. Conserver les licences et attributions
des composants tiers.

Toute modification du moteur embarqué doit être documentée dans sa
[notice](runner/vendor/mrpython/NOTICE.md), avec un contrôle de non-régression.
Les contraintes de l’exécution locale sont décrites dans
[docs/execution.md](docs/execution.md).

En proposant une contribution, vous acceptez sa distribution sous la licence
GPL-3.0-or-later du projet, sous réserve des licences des composants tiers.
