# Composants tiers

- MrPython, auteurs listés dans `runner/vendor/mrpython/AUTHORS`, licence
  `runner/vendor/mrpython/LICENSE.python`. Source et modifications :
  `runner/vendor/mrpython/NOTICE.md`.
- Monaco Editor (Microsoft), React (Meta), Vite, TypeScript, Tailwind CSS,
  KaTeX, react-markdown, remark, rehype et Phosphor : voir les licences
  incluses avec leurs paquets npm.
- Geist et Geist Mono : SIL Open Font License, incluse avec les polices.
- TikZJax, Jim Fowler, Glenn Rice et Rodrigo Schwencke : paquet
  `@rod2ik/tikzjax` 1.6.0, GPL-3.0+, https://github.com/rod2ik/tikzjax.
  Le moteur TeX/WebAssembly, les fichiers TeX et les polices de sa distribution
  sont embarqués sans modification dans `frontend/dist/vendor/tikzjax`.
  Le fichier `LICENSE` et les notices du worker y sont conservés.
- DOMPurify (Cure53, Apache-2.0 ou MPL-2.0) nettoie les SVG générés ;
  threads.js (MIT) fournit l’interface du worker. Licences dans les paquets npm.
- pywebview et ses dépendances natives, PyInstaller et le runtime Python :
  voir les licences de leurs distributions.

`scripts/build_desktop.py` copie les fichiers de licence des dépendances
installées dans la distribution (`licenses/dependencies`). Aucune interface
graphique IDLE/Tkinter de MrPython n'est incluse. Les noms MrPython et ceux des
composants tiers identifient les projets d'origine, sans revendication
d'affiliation.
