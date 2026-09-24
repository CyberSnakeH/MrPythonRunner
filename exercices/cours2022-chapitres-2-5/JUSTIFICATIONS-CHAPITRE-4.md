# Éléments de correction — chapitre 4

Ces indications complètent les corrigés exécutables. Les lettres t ou k utilisées dans un raisonnement peuvent être des compteurs mathématiques, sans devoir toutes apparaître dans le programme.

## S07 — Conserver une relation vraie

31. **Distribution.** Après t tournées, objets = reste + t × equipes et reste >= 0. Chaque tour retire un entier strictement positif. À la sortie, 0 <= reste < equipes. Aucune tournée supplémentaire n’est donc possible.
32. **Monnaie.** montant = reste + valeur déjà rendue, avec reste >= 0. Chaque choix de pièce vaut au plus le reste et au moins 1 ; le reste est un variant. Le compteur dénombre les pièces, tandis que leur somme représente la valeur rendue. Le sujet demande de suivre une règle donnée, pas de prouver son optimalité.
33. **Stock.** Avant chaque tour, stock est la quantité après les t cycles terminés et stock >= 0. L’ajout conserve cette propriété ; le retrait borné par le stock la conserve aussi. Le variant tours − t décroît, même si le stock se stabilise.
34. **Freinage.** La distance est la somme des déplacements déjà effectués, et v est la vitesse du prochain déplacement. v est un entier naturel qui décroît strictement dans chaque branche. À vitesse 1, il faut compter un dernier mètre avant de fixer v à zéro.
35. **Cuve.** initial + t × apport = stock + pertes, avec 0 <= stock <= capacite. Ajouter l’apport puis transférer le surplus vers les pertes préserve cette égalité. Le variant tours − t assure l’arrêt. À la fin, pertes est bien tout ce qui a débordé.

## S08 — Éviter le travail inutile

36. **Parking.** Tous les numéros compris entre depart et numero exclu ont été refusés. La sortie est donc le premier numéro autorisé. Il existe toujours un entier de la forme 15k+1 supérieur ou égal au départ, ni multiple de 3 ni multiple de 5 ; la recherche est bornée par le prochain de ces entiers.
37. **Créneau.** La division entière arrondie vers le haut trouve le premier multiple de periode supérieur ou égal à depart. Chaque tour avance d’une période, donc n’ignore aucun créneau possible. Pendant la pause, le déficit positif pause_fin − t diminue strictement ; sa partie positive est un variant naturel, nul une fois la pause dépassée. La borne finale de pause est exclue.
38. **Énergie.** duree = complets × cycle + reste, avec 0 <= reste < cycle. Un cycle entier coûte 8 + 2 × (cycle − 1). Une fin non vide coûte 8 + 2 × (reste − 1) ; une fin vide coûte zéro. Le programme effectue un nombre borné d’opérations arithmétiques, contrairement au parcours minute par minute. Il s’agit du nombre d’opérations, sans analyse du coût des grands entiers.
39. **Alerte.** Avant le poste p, p−1 postes ont été contrôlés sans déclenchement. Le compteur est augmenté pour inclure le poste courant, puis le retour anticipé empêche tout contrôle supplémentaire. En l’absence d’alerte, la boucle parcourt tous les postes. Le respect de la boucle demandée doit être lu, car une formule peut fournir les mêmes valeurs.
40. **Réduction.** reste est la taille après etape réductions et 0 <= etape <= maximum. Le variant maximum − etape décroît. Si reste > 1, sa moitié arrondie vers le haut est strictement inférieure à reste. Dès reste <= 1, toute réduction supplémentaire serait sans effet ; la garde combinée l’évite.

## S09 — Auditer des simulations

41. **Stockage.** Après t doublements, place = capacite × 2^t, avec capacite >= 1. Pendant la boucle, le déficit positif besoin − place diminue strictement. En prenant la partie positive de ce déficit, on obtient un variant naturel, nul à la sortie. La dernière capacité suffit ; si un agrandissement a eu lieu, la capacité précédente ne suffisait pas. Le résultat place − besoin est non négatif.
42. **Extensions.** Après k achats, prix = 2^k, la dépense vaut 2^k − 1 et credits = reste + dépense. La garde garantit un reste non négatif après paiement. Le reste décroît strictement, puisque le prix est toujours positif. À la sortie, le prochain achat est impossible.
43. **Capteur.** Au début du tour i, compte est le nombre d’alertes parmi les indices 1 à i−1, et 1 <= i <= nombre+1. La comparaison stricte correspond au sujet. Le variant nombre+1−i décroît. À la sortie i = nombre+1, toutes les mesures demandées, et seulement elles, ont été traitées.
44. **Pic.** Après i tours, pic est le maximum des i+1 états allant de l’état initial à la charge courante. Chaque mise à jour conserve cette propriété. Le variant est tours−i ; la charge n’est pas un variant puisqu’elle peut augmenter. Avec zéro tour, le pic reste l’état initial.
45. **Robots.** Après t tours, a = gauche + 2t et b = droite − t. L’écart vaut droite−gauche−3t. Tant qu’il est positif, le nombre de tours encore nécessaires vaut son tiers arrondi vers le haut. Sa partie non négative décroît jusqu’à zéro. À la sortie a >= b ; un dépassement est autorisé et aucun tour supplémentaire n’est nécessaire.
