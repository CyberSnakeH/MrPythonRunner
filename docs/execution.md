# Exécution du code et limites


MrPython est un environnement pédagogique : certaines constructions Python,
bibliothèques et conventions ne sont pas acceptées par son vérificateur.
Le support graphique `Image/show_image` et `input()` interactif ne sont pas
inclus. Les QCM et réponses numériques ne sont pas implémentés dans cette version.

Chaque correction tourne dans un nouveau processus, dans un dossier temporaire,
avec un délai global de 1 à 30 secondes. Chaque test repart de nouvelles variables
globales élève, mais les modules importés restent communs au processus. La sortie
capturée est limitée à 32 000 caractères. Sous Windows, un Job Object limite la
mémoire à 512 Mo et empêche les processus enfants ; sous Linux, les limites Unix
incluent 512 Mo d'espace d'adressage. Sur macOS, la mémoire n'est pas plafonnée de
manière portable ; le délai et les limites CPU/fichiers s'appliquent.

**Il ne s'agit pas d'un bac à sable de sécurité.** Le Python exécuté dispose
des droits de l'utilisateur, notamment sur ses fichiers et son réseau. Utilisez
des sujets et copies de confiance. Une utilisation avec du code hostile nécessite
une isolation OS/VM supplémentaire. Les espaces professeur/élève sont des modes
d'interface. L’application vérifie l’identifiant attribué avant d’ouvrir les
exercices, sauvegarder, corriger ou reprendre les réponses. Cet identifiant reste
lisible dans le fichier : ce contrôle local n’est pas une authentification
sécurisée et ne protège pas d’une modification volontaire de l’archive.

Les tests masqués sont consultables dans le fichier distribué. Ne distribuez
pas les corrigés ou tests que vous souhaitez garder confidentiels. Les résultats
calculent une réussite fonctionnelle ; les contraintes de méthode (ex. employer
une boucle) ne sont pas automatiquement vérifiées.
