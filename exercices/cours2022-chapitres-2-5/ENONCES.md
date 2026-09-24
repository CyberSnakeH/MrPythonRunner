# Les 60 nouveaux énoncés — chapitres 2 à 5

Édition 2. Les corrigés sont fournis séparément au professeur.


---

# S01 · 01 — Découper un rouleau sans gaspillage

**Chapitre 2 · Série 01 — Préparer un atelier**

## Situation

Un atelier imprime plusieurs affiches à la suite sur un même rouleau. Chaque affiche occupe une hauteur connue. Pour permettre la découpe, une bande de papier est laissée entre deux affiches voisines, mais aucune bande supplémentaire ne doit être prévue aux deux extrémités.

## Votre mission

Écrivez la fonction `ruban_affiches`. Calculez la longueur de papier nécessaire pour imprimer une rangée d’affiches.

`nombre` est le nombre d’affiches, `hauteur` leur hauteur en centimètres et `separation` la largeur de chaque bande, dans la même unité. Retournez une longueur en centimètres. Pour une seule affiche, aucune séparation n’est nécessaire. Une séparation nulle est autorisée. Décomposez votre calcul en papier imprimé et papier réservé à la découpe.

### Fonction attendue

```python
def ruban_affiches(nombre: int, hauteur: float, separation: float) -> float:
```

### Exemples expliqués

**Exemple 1.** `ruban_affiches(3, 30.0, 2.0)` renvoie `94.0`. Les trois affiches occupent 90 cm et les deux séparations 4 cm : il faut 94 cm.

**Exemple 2.** `ruban_affiches(1, 12.5, 4.0)` renvoie `12.5`. Une seule affiche occupe 12,5 cm ; la séparation de 4 cm ne sert pas.

### Conditions sur les données

Vous pouvez supposer que `nombre >= 1 and hauteur > 0 and separation >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez deux variables locales pour les deux contributions. Aucune boucle n’est nécessaire.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

Ne faites pas d’arrondi. Les comparaisons automatiques utilisent des tolérances relative et absolue de $10^{-9}$.

*Notions mobilisées : sections 2.1–2.2, pages imprimées 19–32 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def ruban_affiches(nombre: int, hauteur: float, separation: float) -> float:
    """Calculez la longueur de papier nécessaire pour imprimer une rangée d’affiches.
    Précondition : nombre >= 1 and hauteur > 0 and separation >= 0
    """
    # Écrivez votre programme ici.
    return 0.0
```

---

# S01 · 02 — Une réserve à ne pas consommer

**Chapitre 2 · Série 01 — Préparer un atelier**

## Situation

Un robot d’inventaire doit conserver une partie de sa batterie pour rejoindre sa base. Le responsable connaît l’énergie actuellement disponible, la réserve à protéger et la consommation horaire pendant le travail. Il veut une durée prévisionnelle, pas une heure d’arrivée arrondie.

## Votre mission

Complétez la fonction fournie `autonomie_robot`. Retournez le nombre d’heures pendant lesquelles le robot peut travailler avant d’atteindre sa réserve.

`charge` et `reserve` sont des énergies en Wh ; `consommation` est une énergie consommée par heure, en Wh/h. Le robot peut utiliser exactement la différence entre charge et réserve. Retournez une durée réelle en heures. Si la charge est déjà égale à la réserve, le résultat vaut zéro. Ne convertissez pas la durée en minutes.

### Fonction attendue

```python
def autonomie_robot(charge: float, reserve: float, consommation: float) -> float:
```

### Exemples expliqués

**Exemple 1.** `autonomie_robot(120.0, 30.0, 30.0)` renvoie `3.0`. Il reste 90 Wh utilisables ; à 30 Wh/h, ils permettent 3 heures de travail.

**Exemple 2.** `autonomie_robot(50.0, 50.0, 8.0)` renvoie `0.0`. Toute l’énergie est réservée au retour : aucune durée de travail n’est disponible.

### Conditions sur les données

Vous pouvez supposer que `0 <= reserve <= charge and consommation > 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

Ne faites pas d’arrondi. Les comparaisons automatiques utilisent des tolérances relative et absolue de $10^{-9}$.

*Notions mobilisées : sections 2.1–2.2, pages imprimées 19–32 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def autonomie_robot(charge: float, reserve: float, consommation: float) -> float:
    """Retournez le nombre d’heures pendant lesquelles le robot peut travailler avant d’atteindre sa réserve.
    Précondition : 0 <= reserve <= charge and consommation > 0
    """
    utilisable: float = charge - reserve
    # Convertissez cette énergie en une durée de travail.
    return 0.0
```

---

# S01 · 03 — Compter les dalles du pourtour

**Chapitre 2 · Série 01 — Préparer un atelier**

## Situation

Une terrasse est recouverte d’une grille rectangulaire de dalles identiques. Le jardinier souhaite peindre uniquement les dalles du pourtour. Une dalle d’angle appartient à deux côtés, mais elle ne sera peinte qu’une fois : la commande de peinture doit donc éviter de la compter deux fois.

## Votre mission

Écrivez la fonction `dalles_bordure`. Calculez combien de dalles appartiennent au bord d’une terrasse rectangulaire.

`largeur` et `longueur` donnent le nombre de dalles dans les deux directions, et non des longueurs en mètres. Comptez toute dalle située sur la première ou la dernière ligne, ou sur la première ou la dernière colonne. Si une dimension vaut 2, toutes les dalles sont sur le bord. Retournez un entier.

### Fonction attendue

```python
def dalles_bordure(largeur: int, longueur: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `dalles_bordure(4, 5)` renvoie `14`. Une grille de 4 par 5 contient 20 dalles, dont 6 à l’intérieur : 14 sont au bord.

**Exemple 2.** `dalles_bordure(2, 3)` renvoie `6`. Une terrasse de deux dalles de large n’a pas de dalle intérieure : les 6 sont à peindre.

### Conditions sur les données

Vous pouvez supposer que `largeur >= 2 and longueur >= 2`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Faites un calcul direct avec des variables intermédiaires, sans boucle.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.1–2.2, pages imprimées 19–32 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def dalles_bordure(largeur: int, longueur: int) -> int:
    """Calculez combien de dalles appartiennent au bord d’une terrasse rectangulaire.
    Précondition : largeur >= 2 and longueur >= 2
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S01 · 04 — Les octets oubliés par l’appareil photo

**Chapitre 2 · Série 01 — Préparer un atelier**

## Situation

Un appareil de laboratoire regroupe ses photos dans une archive. Son logiciel de prévision ne compte actuellement que les pixels, ce qui sous-estime l’espace à réserver. Le format impose aussi un en-tête global et une petite fiche descriptive avant chaque photographie, même si toutes ont les mêmes dimensions.

## Votre mission

Corrigez la fonction fournie `taille_archive`. Retournez la taille en octets d’une archive de photographies non compressées.

Chaque pixel occupe exactement 3 octets. Chaque photo possède en plus une fiche de 16 octets. L’archive possède toujours un en-tête de 128 octets, y compris lorsqu’elle contient zéro photo. `largeur` et `hauteur` sont des nombres de pixels. Corrigez le code pour retourner la taille totale, sans convertir en kilo-octets.

### Fonction attendue

```python
def taille_archive(nombre: int, largeur: int, hauteur: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `taille_archive(2, 2, 3)` renvoie `196`. Chaque photo demande 2×3×3 + 16 = 34 octets. Deux photos et l’en-tête occupent 196 octets.

**Exemple 2.** `taille_archive(0, 10, 10)` renvoie `128`. Sans photo, seul l’en-tête global de 128 octets est écrit.

### Conditions sur les données

Vous pouvez supposer que `nombre >= 0 and largeur > 0 and hauteur > 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.1–2.2, pages imprimées 19–32 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def taille_archive(nombre: int, largeur: int, hauteur: int) -> int:
    """Retournez la taille en octets d’une archive de photographies non compressées.
    Précondition : nombre >= 0 and largeur > 0 and hauteur > 0
    """
    image: int = largeur * hauteur * 3
    return nombre * image
```

---

# S01 · 05 — Préparer les badges d’une rencontre

**Chapitre 2 · Série 01 — Préparer un atelier**

## Situation

Une association prépare une rencontre. Chaque personne reçoit un badge et une attache. Il reste des badges vierges d’une rencontre précédente, mais aucune attache. Le trésorier veut connaître uniquement le montant des achats à effectuer cette fois, en tenant compte du stock déjà payé.

## Votre mission

Écrivez la fonction `budget_badges`. Calculez le budget d’achat en centimes pour les badges et leurs attaches.

`participants` et `accompagnants` sont les deux effectifs présents ; chaque personne compte de la même façon. `stock` est le nombre de badges réutilisables, jamais supérieur à l’effectif total. Un badge neuf coûte 35 centimes et une attache 12 centimes. Achetez une attache pour chaque personne, y compris lorsqu’elle reçoit un ancien badge. Retournez un nombre entier de centimes.

### Fonction attendue

```python
def budget_badges(participants: int, accompagnants: int, stock: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `budget_badges(10, 2, 4)` renvoie `424`. Il faut 12 attaches et seulement 8 badges neufs : 12×12 + 8×35 = 424 centimes.

**Exemple 2.** `budget_badges(3, 2, 5)` renvoie `60`. Les cinq badges sont en stock, mais les cinq attaches coûtent encore 60 centimes.

### Conditions sur les données

Vous pouvez supposer que `participants >= 0 and accompagnants >= 0 and 0 <= stock <= participants + accompagnants`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.1–2.2, pages imprimées 19–32 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def budget_badges(participants: int, accompagnants: int, stock: int) -> int:
    """Calculez le budget d’achat en centimes pour les badges et leurs attaches.
    Précondition : participants >= 0 and accompagnants >= 0 and 0 <= stock <= participants + accompagnants
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S02 · 06 — Autoriser une visite de la serre

**Chapitre 2 · Série 02 — Décider si une action est possible**

## Situation

La serre pédagogique ouvre aux visiteurs uniquement lorsque ses deux capteurs indiquent des conditions confortables. Pendant une intervention technique, les visites sont interdites quelles que soient les mesures. Le gardien souhaite que l’application rende une décision unique à partir des trois informations reçues.

## Votre mission

Écrivez la fonction `ouvrir_serre`. Indiquez si une visite de la serre est autorisée.

`temperature` est exprimée en degrés Celsius ; `humidite` est un pourcentage. La température doit être comprise entre 18 et 26 inclus et l’humidité entre 40 et 70 inclus. `entretien` vaut True lorsqu’une intervention est en cours. Retournez True seulement si les deux plages sont respectées et si aucune intervention n’a lieu.

### Fonction attendue

```python
def ouvrir_serre(temperature: float, humidite: float, entretien: bool) -> bool:
```

### Exemples expliqués

**Exemple 1.** `ouvrir_serre(22.0, 55.0, False)` renvoie `True`. 22 °C et 55 % respectent les deux plages ; aucun entretien ne bloque la visite.

**Exemple 2.** `ouvrir_serre(22.0, 55.0, True)` renvoie `False`. Les mesures sont bonnes mais l’intervention en cours interdit l’ouverture.

### Conditions sur les données

Vous pouvez supposer que `0 <= humidite <= 100`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.1–2.3.2, pages imprimées 33–41 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def ouvrir_serre(temperature: float, humidite: float, entretien: bool) -> bool:
    """Indiquez si une visite de la serre est autorisée.
    Précondition : 0 <= humidite <= 100
    """
    # Écrivez votre programme ici.
    return False
```

---

# S02 · 07 — Une borne libre ne suffit pas

**Chapitre 2 · Série 02 — Décider si une action est possible**

## Situation

Un robot partage une borne avec d’autres appareils. Il ne doit jamais demander une place déjà occupée. En temps normal, il attend que sa batterie soit faible ; avant une mission urgente, il demande une recharge préventive, même si sa batterie n’est pas encore faible.

## Votre mission

Complétez la fonction fournie `demander_recharge`. Décidez si le robot doit demander la borne de recharge.

`batterie` est un pourcentage entier. Une batterie est faible lorsque ce nombre est strictement inférieur à 30. `borne_libre` indique si la borne est disponible et `mission_urgente` si une recharge préventive est souhaitée. La demande est acceptée uniquement si la borne est libre et si au moins un des deux motifs de recharge existe. À 30 %, la batterie n’est pas faible.

### Fonction attendue

```python
def demander_recharge(batterie: int, borne_libre: bool, mission_urgente: bool) -> bool:
```

### Exemples expliqués

**Exemple 1.** `demander_recharge(20, True, False)` renvoie `True`. La batterie à 20 % suffit à motiver la demande et la borne est libre.

**Exemple 2.** `demander_recharge(80, False, True)` renvoie `False`. L’urgence motive une recharge, mais une borne occupée reste indisponible.

### Conditions sur les données

Vous pouvez supposer que `0 <= batterie <= 100`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.1–2.3.2, pages imprimées 33–41 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def demander_recharge(batterie: int, borne_libre: bool, mission_urgente: bool) -> bool:
    """Décidez si le robot doit demander la borne de recharge.
    Précondition : 0 <= batterie <= 100
    """
    motif: bool = batterie < 30 or mission_urgente
    # Tenez également compte de la disponibilité.
    return False
```

---

# S02 · 08 — Au moins deux colis identiques

**Chapitre 2 · Série 02 — Décider si une action est possible**

## Situation

Le service expédition souhaite séparer certaines commandes en plusieurs colis de même taille, sans reliquat. Un opérateur propose un nombre d’articles par colis. Il peut se tromper et saisir zéro : le logiciel doit refuser cette proposition proprement, sans déclencher une division par zéro.

## Votre mission

Écrivez la fonction `commande_partageable`. Indiquez si une commande peut être répartie en au moins deux colis pleins et identiques.

`articles` est la quantité totale et `par_colis` la capacité proposée. Une proposition est valide si la capacité est strictement positive, si tous les articles entrent dans des colis pleins et si au moins deux colis sont nécessaires. Une commande vide et une commande tenant dans un seul colis sont refusées. Retournez un booléen, sans lever d’erreur lorsque par_colis vaut zéro.

### Fonction attendue

```python
def commande_partageable(articles: int, par_colis: int) -> bool:
```

### Exemples expliqués

**Exemple 1.** `commande_partageable(12, 4)` renvoie `True`. Les 12 articles forment trois colis de 4 : la répartition est valide.

**Exemple 2.** `commande_partageable(4, 4)` renvoie `False`. Les 4 articles forment un seul colis ; la condition de deux colis n’est pas satisfaite.

### Conditions sur les données

Vous pouvez supposer que `articles >= 0 and par_colis >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez le court-circuit de `and` pour protéger le reste et la division entière.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.1–2.3.2, pages imprimées 33–41 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def commande_partageable(articles: int, par_colis: int) -> bool:
    """Indiquez si une commande peut être répartie en au moins deux colis pleins et identiques.
    Précondition : articles >= 0 and par_colis >= 0
    """
    # Écrivez votre programme ici.
    return False
```

---

# S02 · 09 — L’alarme de désaccord

**Chapitre 2 · Série 02 — Décider si une action est possible**

## Situation

Deux capteurs mesurent simultanément un niveau de remplissage. Pour éviter qu’une valeur aberrante passe inaperçue, le système ne valide pas seulement leur proximité : chacun doit aussi fournir une mesure dans la plage physique autorisée. Deux capteurs en panne peuvent en effet donner la même mauvaise valeur.

## Votre mission

Corrigez la fonction fournie `deux_capteurs_valides`. Indiquez si deux mesures sont toutes deux recevables et suffisamment proches.

`a` et `b` sont des pourcentages qui doivent chacun appartenir à [0,100]. Leur différence doit être comprise entre -tolerance et +tolerance, bornes incluses. Une seule valeur hors de [0,100] invalide l’ensemble, même si l’écart est faible. Corrigez le programme qui ne contrôle actuellement que l’accord entre les mesures. Retournez True si toutes les conditions sont remplies.

### Fonction attendue

```python
def deux_capteurs_valides(a: float, b: float, tolerance: float) -> bool:
```

### Exemples expliqués

**Exemple 1.** `deux_capteurs_valides(48.0, 50.0, 2.0)` renvoie `True`. L’écart vaut 2 points et les deux mesures sont physiques : la validation réussit.

**Exemple 2.** `deux_capteurs_valides(110.0, 110.0, 1.0)` renvoie `False`. Les capteurs s’accordent, mais 110 % est impossible : la validation doit échouer.

### Conditions sur les données

Vous pouvez supposer que `tolerance >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.1–2.3.2, pages imprimées 33–41 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def deux_capteurs_valides(a: float, b: float, tolerance: float) -> bool:
    """Indiquez si deux mesures sont toutes deux recevables et suffisamment proches.
    Précondition : tolerance >= 0
    """
    return -tolerance <= a - b <= tolerance
```

---

# S02 · 10 — Deux réservations peuvent-elles coexister ?

**Chapitre 2 · Série 02 — Décider si une action est possible**

## Situation

Une salle ne peut accueillir qu’un groupe à la fois. Les réservations sont enregistrées en minutes depuis minuit. Un groupe peut entrer exactement quand le précédent sort : le logiciel doit donc distinguer un véritable chevauchement d’un simple contact entre deux horaires.

## Votre mission

Écrivez la fonction `reservations_en_conflit`. Détectez si deux réservations occupent simultanément une salle.

Chaque réservation occupe l’intervalle allant de son début inclus à sa fin exclue. Retournez True s’il existe une durée strictement positive pendant laquelle les deux groupes seraient présents. Les paramètres ne sont pas nécessairement fournis dans l’ordre chronologique. Une réservation entièrement contenue dans l’autre constitue un conflit ; deux réservations consécutives n’en constituent pas.

### Fonction attendue

```python
def reservations_en_conflit(debut1: int, fin1: int, debut2: int, fin2: int) -> bool:
```

### Exemples expliqués

**Exemple 1.** `reservations_en_conflit(60, 120, 90, 150)` renvoie `True`. Les deux groupes seraient présents de la minute 90 à la minute 120.

**Exemple 2.** `reservations_en_conflit(60, 120, 120, 180)` renvoie `False`. Le premier groupe sort à 120, exactement quand le second entre : aucun conflit.

### Conditions sur les données

Vous pouvez supposer que `0 <= debut1 < fin1 <= 1440 and 0 <= debut2 < fin2 <= 1440`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.1–2.3.2, pages imprimées 33–41 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def reservations_en_conflit(debut1: int, fin1: int, debut2: int, fin2: int) -> bool:
    """Détectez si deux réservations occupent simultanément une salle.
    Précondition : 0 <= debut1 < fin1 <= 1440 and 0 <= debut2 < fin2 <= 1440
    """
    # Écrivez votre programme ici.
    return False
```

---

# S03 · 11 — Le prix d’un dépôt au vestiaire

**Chapitre 2 · Série 03 — Appliquer des règles de gestion**

## Situation

Le vestiaire d’un festival classe les objets selon leur volume. Les objets fragiles nécessitent une protection supplémentaire, mais restent dans la même catégorie de taille. L’équipe souhaite une fonction unique qui applique correctement les seuils et ajoute la protection une seule fois.

## Votre mission

Écrivez la fonction `cout_consigne`. Retournez le prix d’un dépôt en euros entiers.

`volume` est un nombre entier de litres. Jusqu’à 10 litres inclus, le tarif de base vaut 2 euros ; de 11 à 30 litres inclus, il vaut 4 euros ; au-delà de 30 litres, il vaut 7 euros. Si `fragile` vaut True, ajoutez 3 euros quel que soit le volume. Retournez le total, sans afficher de texte.

### Fonction attendue

```python
def cout_consigne(volume: int, fragile: bool) -> int:
```

### Exemples expliqués

**Exemple 1.** `cout_consigne(8, True)` renvoie `5`. Un objet de 8 litres coûte 2 euros ; la protection ajoute 3 euros, soit 5.

**Exemple 2.** `cout_consigne(30, False)` renvoie `4`. 30 litres appartiennent encore à la catégorie intermédiaire à 4 euros.

### Conditions sur les données

Vous pouvez supposer que `volume > 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.3, pages imprimées 41–42 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def cout_consigne(volume: int, fragile: bool) -> int:
    """Retournez le prix d’un dépôt en euros entiers.
    Précondition : volume > 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S03 · 12 — Livrer ce qui est disponible

**Chapitre 2 · Série 03 — Appliquer des règles de gestion**

## Situation

Une boutique prépare une commande avec un stock parfois insuffisant. Certains clients acceptent une livraison partielle ; d’autres veulent recevoir toute leur commande en une seule fois. La fonction doit choisir la quantité à envoyer maintenant sans dépasser ni la demande ni le stock disponible.

## Votre mission

Complétez la fonction fournie `quantite_a_expedier`. Retournez le nombre d’articles à expédier immédiatement.

Si le stock couvre la demande, expédiez exactement la quantité demandée, quelle que soit l’option. Si le stock est insuffisant et que `autoriser_partiel` vaut True, expédiez tout le stock. Dans le cas contraire, n’expédiez rien. Une demande nulle produit toujours zéro. Ne modifiez pas le stock : retournez seulement la quantité calculée.

### Fonction attendue

```python
def quantite_a_expedier(demande: int, stock: int, autoriser_partiel: bool) -> int:
```

### Exemples expliqués

**Exemple 1.** `quantite_a_expedier(8, 5, True)` renvoie `5`. Il manque trois articles, mais le client accepte de recevoir les cinq disponibles.

**Exemple 2.** `quantite_a_expedier(8, 5, False)` renvoie `0`. Sans autorisation de livraison partielle, les cinq articles restent en attente.

### Conditions sur les données

Vous pouvez supposer que `demande >= 0 and stock >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.3, pages imprimées 41–42 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def quantite_a_expedier(demande: int, stock: int, autoriser_partiel: bool) -> int:
    """Retournez le nombre d’articles à expédier immédiatement.
    Précondition : demande >= 0 and stock >= 0
    """
    if stock >= demande:
        return demande
    # Traitez le stock insuffisant suivant le choix du client.
    return 0
```

---

# S03 · 13 — Donner priorité à l’alerte forte

**Chapitre 2 · Série 03 — Appliquer des règles de gestion**

## Situation

Une salle possède trois modes de ventilation. Les règles de température et de qualité de l’air peuvent se déclencher en même temps. Le régulateur doit toujours retenir le mode le plus fort demandé par une des mesures, plutôt que de s’arrêter à la première alerte modérée.

## Votre mission

Écrivez la fonction `mode_ventilation`. Choisissez le mode 0, 1 ou 2 du ventilateur.

Le mode 2 est obligatoire si la température atteint 30 degrés ou si le CO₂ atteint 1500 ppm. Sinon, choisissez le mode 1 si la température atteint 24 degrés ou si le CO₂ atteint 1000 ppm. Si aucune condition n’est satisfaite, choisissez 0. Les valeurs seuils sont incluses et un seul dépassement suffit à activer un mode.

### Fonction attendue

```python
def mode_ventilation(temperature: int, co2: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `mode_ventilation(26, 800)` renvoie `1`. 26 degrés déclenchent seulement le mode 1 ; le CO₂ reste bas.

**Exemple 2.** `mode_ventilation(25, 1500)` renvoie `2`. Malgré une température modérée, les 1500 ppm imposent le mode 2.

### Conditions sur les données

Vous pouvez supposer que `co2 >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.3, pages imprimées 41–42 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def mode_ventilation(temperature: int, co2: int) -> int:
    """Choisissez le mode 0, 1 ou 2 du ventilateur.
    Précondition : co2 >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S03 · 14 — Un colis perdu ne marque aucun point

**Chapitre 2 · Série 03 — Appliquer des règles de gestion**

## Situation

Une coopérative évalue ses tournées avec un score simple. Le retard représente l’écart entre l’heure réelle et l’heure prévue : une valeur négative signifie une arrivée en avance. La perte d’un colis annule cependant tous les points, même si une heure de livraison a été enregistrée par erreur.

## Votre mission

Corrigez la fonction fournie `points_livraison`. Calculez le score de qualité d’une livraison.

Un colis perdu reçoit toujours 0 point. Pour les autres, un retard inférieur ou égal à 0 donne 100 points ; de 1 à 10 minutes incluses, 80 ; de 11 à 30 incluses, 50 ; au-delà, 0. Le programme fourni ne tient pas compte des pertes. Corrigez-le sans changer cette grille de retard ni la signature.

### Fonction attendue

```python
def points_livraison(retard: int, perdu: bool) -> int:
```

### Exemples expliqués

**Exemple 1.** `points_livraison(6, False)` renvoie `80`. Six minutes de retard donnent 80 points lorsque le colis est bien arrivé.

**Exemple 2.** `points_livraison(-3, True)` renvoie `0`. Le colis est perdu : le score est nul, même avec une heure enregistrée en avance.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.3, pages imprimées 41–42 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def points_livraison(retard: int, perdu: bool) -> int:
    """Calculez le score de qualité d’une livraison.
    """
    if retard <= 0:
        return 100
    elif retard <= 10:
        return 80
    elif retard <= 30:
        return 50
    return 0
```

---

# S03 · 15 — Un plafond pour chaque journée

**Chapitre 2 · Série 03 — Appliquer des règles de gestion**

## Situation

La gare facture ses casiers par tranches de 24 heures à partir du début de la location. Une tranche complète coûte 12 euros. Pour la dernière tranche incomplète, la facturation est horaire mais ne peut jamais dépasser ce même forfait : il faut appliquer le plafond au bon endroit.

## Votre mission

Écrivez la fonction `location_casier`. Retournez le prix d’une location de casier en euros.

`heures` est une durée entière déjà mesurée ; aucune heure supplémentaire ne doit être arrondie. Chaque bloc complet de 24 heures coûte 12 euros. Les heures restantes coûtent 2 euros chacune, avec un maximum de 12 euros pour ce reste. Une durée nulle coûte zéro. Retournez le total de tous les blocs et du dernier reste.

### Fonction attendue

```python
def location_casier(heures: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `location_casier(26)` renvoie `16`. 26 heures font un bloc de 24 heures à 12 euros et deux heures à 4 euros : total 16.

**Exemple 2.** `location_casier(8)` renvoie `12`. Huit heures coûteraient 16 euros à l’heure, mais le plafond ramène le prix à 12.

### Conditions sur les données

Vous pouvez supposer que `heures >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 2.3.3, pages imprimées 41–42 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def location_casier(heures: int) -> int:
    """Retournez le prix d’une location de casier en euros.
    Précondition : heures >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S04 · 16 — Installer des rangées de chaises

**Chapitre 3 · Série 04 — Simuler une activité répétée**

## Situation

La salle d’un festival s’élargit à mesure que l’on s’éloigne de la scène. Les bénévoles installent une première rangée, puis ajoutent toujours le même nombre de chaises à chaque nouvelle rangée. Ils doivent préparer le stock total avant de commencer.

## Votre mission

Écrivez la fonction `places_gradins`. Retournez le nombre total de chaises à installer.

`premier` est le nombre de chaises de la première rangée ; `supplement` est le nombre ajouté pour passer à la suivante. `rangees` est le nombre de rangées effectivement installées. Une installation sans rangée demande zéro chaise. Une augmentation nulle donne des rangées identiques. Simulez les rangées une à une avec une boucle while.

### Fonction attendue

```python
def places_gradins(premier: int, supplement: int, rangees: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `places_gradins(4, 2, 3)` renvoie `18`. Les rangées contiennent 4, 6 et 8 chaises : leur total vaut 18.

**Exemple 2.** `places_gradins(4, 2, 0)` renvoie `0`. Aucune rangée n’est installée ; le stock nécessaire est nul.

### Conditions sur les données

Vous pouvez supposer que `premier >= 0 and supplement >= 0 and rangees >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Indiquez dans un commentaire ce que représentent le compteur, la taille courante et le total avant chaque tour.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.1–3.3.2, pages imprimées 43–54 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def places_gradins(premier: int, supplement: int, rangees: int) -> int:
    """Retournez le nombre total de chaises à installer.
    Précondition : premier >= 0 and supplement >= 0 and rangees >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S04 · 17 — Des missions de plus en plus coûteuses

**Chapitre 3 · Série 04 — Simuler une activité répétée**

## Situation

Un robot d’essai effectue des missions numérotées à partir de un. La première consomme une unité de batterie, la deuxième deux unités, et ainsi de suite. Le laboratoire fournit assez d’énergie pour toutes les missions prévues et veut simuler leur consommation successive.

## Votre mission

Complétez la fonction fournie `batterie_missions`. Retournez la charge restante après toutes les missions.

`charge` désigne la quantité initiale d’énergie et `missions` le nombre de missions à effectuer. La mission de numéro k retire exactement k unités. Complétez la boucle pour retirer chaque consommation une seule fois. Retournez l’énergie restante, pas l’énergie consommée. Avec zéro mission, toute la charge initiale reste disponible.

### Fonction attendue

```python
def batterie_missions(charge: int, missions: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `batterie_missions(20, 3)` renvoie `14`. Les trois missions retirent 1 + 2 + 3 = 6 unités ; il en reste 14.

**Exemple 2.** `batterie_missions(8, 0)` renvoie `8`. Aucune mission n’est effectuée, donc les 8 unités sont conservées.

### Conditions sur les données

Vous pouvez supposer que `missions >= 0 and charge >= missions * (missions + 1) // 2`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.1–3.3.2, pages imprimées 43–54 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def batterie_missions(charge: int, missions: int) -> int:
    """Retournez la charge restante après toutes les missions.
    Précondition : missions >= 0 and charge >= missions * (missions + 1) // 2
    """
    reste: int = charge
    k: int = 1
    while k <= missions:
        # Ajoutez ici la consommation de cette mission.
        k = k + 1
    return reste
```

---

# S04 · 18 — Deux montants de versement

**Chapitre 3 · Série 04 — Simuler une activité répétée**

## Situation

Une classe finance une sortie grâce à des versements hebdomadaires. Les deux groupes d’élèves contribuent à tour de rôle : le premier verse un montant fixé, puis le second un autre montant. Le compte est vide avant la première semaine.

## Votre mission

Écrivez la fonction `epargne_alternee`. Calculez le montant déposé après le nombre de semaines indiqué.

`petit` est le versement des semaines impaires, en euros, et `grand` celui des semaines paires ; ces noms n’imposent pas un ordre entre les montants. La première semaine utilise donc `petit`. Retournez le cumul après `semaines` versements, en utilisant une boucle while. Zéro semaine signifie qu’aucun versement n’a encore eu lieu.

### Fonction attendue

```python
def epargne_alternee(semaines: int, petit: int, grand: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `epargne_alternee(5, 2, 5)` renvoie `16`. Les versements sont 2, 5, 2, 5, 2 : le compte contient 16 euros.

**Exemple 2.** `epargne_alternee(1, 7, 3)` renvoie `7`. Une seule semaine apporte uniquement le premier montant, soit 7 euros.

### Conditions sur les données

Vous pouvez supposer que `semaines >= 0 and petit >= 0 and grand >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.1–3.3.2, pages imprimées 43–54 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def epargne_alternee(semaines: int, petit: int, grand: int) -> int:
    """Calculez le montant déposé après le nombre de semaines indiqué.
    Précondition : semaines >= 0 and petit >= 0 and grand >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S04 · 19 — Le robot change de direction

**Chapitre 3 · Série 04 — Simuler une activité répétée**

## Situation

Un robot de démonstration part de l’origine d’un axe gradué. Pour tester son moteur, il avance d’une unité, recule de deux, avance de trois, puis recule de quatre. Le programme fourni oublie les changements de direction et doit être corrigé.

## Votre mission

Corrigez la fonction fournie `position_balancier`. Retournez la position finale du robot sur son axe.

Les mouvements sont numérotés de 1 à `mouvements`. Un numéro impair ajoute ce numéro à la position ; un numéro pair le soustrait. Les positions négatives sont autorisées. Retournez la position signée et non la distance parcourue. Sans mouvement, le robot reste à zéro. Conservez une simulation avec une boucle while.

### Fonction attendue

```python
def position_balancier(mouvements: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `position_balancier(4)` renvoie `-2`. Les positions successives sont 1, −1, 2 et −2 ; le résultat est −2.

**Exemple 2.** `position_balancier(3)` renvoie `2`. Les trois déplacements donnent 1 − 2 + 3 = 2.

### Conditions sur les données

Vous pouvez supposer que `mouvements >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.1–3.3.2, pages imprimées 43–54 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def position_balancier(mouvements: int) -> int:
    """Retournez la position finale du robot sur son axe.
    Précondition : mouvements >= 0
    """
    position: int = 0
    k: int = 1
    while k <= mouvements:
        position = position + k
        k = k + 1
    return position
```

---

# S04 · 20 — Retirer les pièces à contrôler

**Chapitre 3 · Série 04 — Simuler une activité répétée**

## Situation

Un atelier conserve un lot de pièces dans une réserve. Chaque matin, il prélève pour contrôle un tiers entier des pièces actuellement présentes. Les pièces prélevées ne reviennent pas dans la réserve et aucun nouvel arrivage n’a lieu pendant la période étudiée.

## Votre mission

Écrivez la fonction `stock_apres_tri`. Retournez le stock restant après les opérations de tri.

À chaque journée, retirez `stock_courant // 3` pièces du stock courant. Le calcul doit être refait après chaque prélèvement : il ne porte pas toujours sur le stock initial. `jours` peut être nul. Un stock inférieur à trois reste inchangé puisque son tiers entier vaut zéro. Retournez le nombre de pièces encore présentes.

### Fonction attendue

```python
def stock_apres_tri(stock: int, jours: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `stock_apres_tri(10, 2)` renvoie `5`. On retire 3 pièces sur 10, puis 2 sur 7 : il reste 5 pièces.

**Exemple 2.** `stock_apres_tri(2, 8)` renvoie `2`. Avec deux pièces, chaque prélèvement vaut zéro ; le stock reste égal à 2.

### Conditions sur les données

Vous pouvez supposer que `stock >= 0 and jours >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.1–3.3.2, pages imprimées 43–54 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def stock_apres_tri(stock: int, jours: int) -> int:
    """Retournez le stock restant après les opérations de tri.
    Précondition : stock >= 0 and jours >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S05 · 21 — Atteindre le financement de la sortie

**Chapitre 3 · Série 05 — Attendre un événement**

## Situation

Une collecte dispose déjà d’une somme de départ. La campagne attire progressivement davantage de personnes : elle rapporte un montant connu le premier jour, puis un euro de plus à chaque nouveau jour. L’organisateur veut annoncer quand le financement sera suffisant.

## Votre mission

Écrivez la fonction `jours_collecte`. Retournez le premier nombre de jours permettant d’atteindre l’objectif.

`initial` et `objectif` sont des sommes en euros ; `premier_gain` est le gain du jour 1. Le jour suivant rapporte un euro supplémentaire par rapport au précédent. Arrêtez-vous dès que la somme cumulée est supérieure ou égale à l’objectif. Si la somme initiale suffit déjà, retournez zéro. Ne poursuivez pas jusqu’à une égalité exacte.

### Fonction attendue

```python
def jours_collecte(initial: int, objectif: int, premier_gain: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `jours_collecte(10, 20, 3)` renvoie `3`. Les gains 3, 4 et 5 portent le total de 10 à 13, 17 puis 22 : trois jours suffisent.

**Exemple 2.** `jours_collecte(30, 20, 2)` renvoie `0`. Les 30 euros de départ dépassent déjà l’objectif de 20 euros.

### Conditions sur les données

Vous pouvez supposer que `initial >= 0 and objectif >= 0 and premier_gain > 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.2–3.3, pages imprimées 45–55 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def jours_collecte(initial: int, objectif: int, premier_gain: int) -> int:
    """Retournez le premier nombre de jours permettant d’atteindre l’objectif.
    Précondition : initial >= 0 and objectif >= 0 and premier_gain > 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S05 · 22 — Faire entrer une bande dans son étui

**Chapitre 3 · Série 05 — Attendre un événement**

## Situation

Une machine plie une bande de carton pour la faire entrer dans un étui. Les longueurs sont mesurées en unités entières. Lorsqu’une longueur est impaire, la moitié la plus longue détermine l’encombrement final : il faut donc arrondir la moitié vers le haut.

## Votre mission

Complétez la fonction fournie `pliages_format`. Retournez le nombre minimal de pliages nécessaires.

`longueur` est l’encombrement initial et `limite` l’encombrement maximal accepté par l’étui. Un pliage remplace une longueur L par `(L + 1) // 2`. Comptez les pliages jusqu’à obtenir une longueur inférieure ou égale à la limite. Si elle est déjà acceptable, retournez zéro. Complétez le comptage sans changer la règle d’arrondi.

### Fonction attendue

```python
def pliages_format(longueur: int, limite: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `pliages_format(9, 3)` renvoie `2`. La longueur passe de 9 à 5, puis à 3 : deux pliages suffisent.

**Exemple 2.** `pliages_format(4, 4)` renvoie `0`. Une bande de longueur 4 entre déjà dans l’étui de limite 4.

### Conditions sur les données

Vous pouvez supposer que `longueur >= 1 and limite >= 1`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.2–3.3, pages imprimées 45–55 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def pliages_format(longueur: int, limite: int) -> int:
    """Retournez le nombre minimal de pliages nécessaires.
    Précondition : longueur >= 1 and limite >= 1
    """
    reste: int = longueur
    compte: int = 0
    while reste > limite:
        reste = (reste + 1) // 2
        # Mémorisez le pliage effectué.
    return compte
```

---

# S05 · 23 — Mesurer ce que le filtre a capturé

**Chapitre 3 · Série 05 — Attendre un événement**

## Situation

Un dispositif filtre un liquide en plusieurs passages. Après chaque passage, il ne reste que la moitié entière des particules présentes auparavant. Le technicien arrête le dispositif lorsque la quantité restante respecte le seuil, puis pèse tous les déchets capturés.

## Votre mission

Écrivez la fonction `dechets_retires`. Retournez la quantité totale de déchets retirés.

`pollution` est le nombre initial de particules et `seuil` le maximum autorisé après traitement. Chaque passage remplace le nombre courant par sa division entière par deux. Retournez le nombre de particules retirées au total, et non le nombre de passages ni le reste. Si le liquide respecte déjà le seuil, aucun déchet n’est retiré.

### Fonction attendue

```python
def dechets_retires(pollution: int, seuil: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `dechets_retires(11, 3)` renvoie `9`. Les restes sont 5 puis 2 ; sur 11 particules initiales, 9 ont été retirées.

**Exemple 2.** `dechets_retires(4, 5)` renvoie `0`. Le seuil de 5 accepte déjà les 4 particules : aucun filtrage n’a lieu.

### Conditions sur les données

Vous pouvez supposer que `pollution >= 0 and seuil >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.2–3.3, pages imprimées 45–55 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def dechets_retires(pollution: int, seuil: int) -> int:
    """Retournez la quantité totale de déchets retirés.
    Précondition : pollution >= 0 and seuil >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S05 · 24 — Financer des journées complètes

**Chapitre 3 · Série 05 — Attendre un événement**

## Situation

Un chantier utilise une réserve de crédits pour ses frais quotidiens. Le premier jour a un coût connu ; chaque jour suivant coûte un crédit de plus. Une journée ne commence que si la réserve permet de payer son coût entier, sans emprunt.

## Votre mission

Corrigez la fonction fournie `jours_reserve`. Retournez le nombre de journées que la réserve peut financer entièrement.

`stock` est le nombre initial de crédits disponibles. Les coûts successifs sont `cout_initial`, puis ce montant augmenté de un, de deux, et ainsi de suite. Il est permis de vider exactement la réserve. Dès que la prochaine journée coûte plus que le reste, arrêtez le comptage. Le programme fourni compte à tort une journée non finançable.

### Fonction attendue

```python
def jours_reserve(stock: int, cout_initial: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `jours_reserve(10, 3)` renvoie `2`. Les coûts 3 puis 4 laissent 3 crédits ; les 5 crédits du troisième jour manquent.

**Exemple 2.** `jours_reserve(3, 3)` renvoie `1`. Les 3 crédits paient exactement une journée, puis la réserve est vide.

### Conditions sur les données

Vous pouvez supposer que `stock >= 0 and cout_initial > 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.2–3.3, pages imprimées 45–55 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def jours_reserve(stock: int, cout_initial: int) -> int:
    """Retournez le nombre de journées que la réserve peut financer entièrement.
    Précondition : stock >= 0 and cout_initial > 0
    """
    reste: int = stock
    cout: int = cout_initial
    jours: int = 0
    while reste > 0:
        reste = reste - cout
        cout = cout + 1
        jours = jours + 1
    return jours
```

---

# S05 · 25 — Atteindre la sortie du puits

**Chapitre 3 · Série 05 — Attendre un événement**

## Situation

Une sonde remonte un conduit vertical. Pendant la journée elle gagne une hauteur fixe ; la nuit elle glisse légèrement. Dès qu’elle atteint la sortie pendant une journée, elle est récupérée : elle ne subit donc pas la glissade de cette dernière nuit.

## Votre mission

Écrivez la fonction `ascension_sonde`. Retournez le nombre de journées nécessaires pour sortir du puits.

La sonde part de la hauteur zéro. `hauteur` est la hauteur de sortie ; `montee` le gain diurne et `glissade` la perte nocturne, dans la même unité. Comptez une journée pour chaque montée effectuée. Testez la sortie avant de soustraire la glissade. Une sortie de hauteur zéro est déjà atteinte et demande zéro journée.

### Fonction attendue

```python
def ascension_sonde(hauteur: int, montee: int, glissade: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `ascension_sonde(5, 3, 2)` renvoie `3`. Les fins de nuit sont à 1 puis 2 ; la troisième montée atteint 5 et permet la sortie.

**Exemple 2.** `ascension_sonde(2, 3, 2)` renvoie `1`. La première montée de 3 dépasse la sortie située à 2 : une journée suffit.

### Conditions sur les données

Vous pouvez supposer que `hauteur >= 0 and montee > glissade >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.2–3.3, pages imprimées 45–55 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def ascension_sonde(hauteur: int, montee: int, glissade: int) -> int:
    """Retournez le nombre de journées nécessaires pour sortir du puits.
    Précondition : hauteur >= 0 and montee > glissade >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S06 · 26 — Comparer les compositions d’un groupe

**Chapitre 3 · Série 06 — Explorer plusieurs possibilités**

## Situation

Un musée cherche les différentes compositions possibles pour une visite familiale. Il ne distingue pas les personnes individuellement : un groupe est défini uniquement par son nombre d’adultes et son nombre d’enfants. Chaque composition doit respecter le budget disponible pour les billets.

## Votre mission

Écrivez la fonction `formules_visite`. Comptez les compositions de groupe admissibles.

Un adulte paie 3 euros et un enfant 2 euros. Comptez les couples d’effectifs contenant au moins un adulte et un enfant, sans dépasser `adultes_max`, `enfants_max` et `budget`. Les bornes maximales sont incluses. Deux groupes ayant les mêmes effectifs ne comptent qu’une fois. Si un effectif maximal vaut zéro, aucune composition n’est possible.

### Fonction attendue

```python
def formules_visite(adultes_max: int, enfants_max: int, budget: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `formules_visite(2, 2, 8)` renvoie `3`. Avec un budget de 8, les effectifs possibles sont (1,1), (1,2) et (2,1).

**Exemple 2.** `formules_visite(3, 3, 4)` renvoie `0`. Même le groupe minimal coûte 5 euros : un budget de 4 ne suffit pas.

### Conditions sur les données

Vous pouvez supposer que `adultes_max >= 0 and enfants_max >= 0 and budget >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez deux boucles while imbriquées ; réinitialisez le compteur intérieur pour chaque adulte possible.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.3.4, pages imprimées 56–57 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def formules_visite(adultes_max: int, enfants_max: int, budget: int) -> int:
    """Comptez les compositions de groupe admissibles.
    Précondition : adultes_max >= 0 and enfants_max >= 0 and budget >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S06 · 27 — Installer les balises d’une grille

**Chapitre 3 · Série 06 — Explorer plusieurs possibilités**

## Situation

Une équipe quadrille une zone rectangulaire pour un exercice d’orientation. Les cases sont repérées par deux coordonnées entières commençant à zéro. Pour répartir régulièrement les balises, elle choisit uniquement les cases dont la somme des coordonnées est un multiple de trois.

## Votre mission

Complétez la fonction fournie `cases_balisees`. Comptez les cases qui reçoivent une balise.

`largeur` donne le nombre de colonnes et `hauteur` le nombre de lignes. Les coordonnées x vont de zéro à largeur moins un ; les coordonnées y de zéro à hauteur moins un. La case (0,0) reçoit une balise lorsqu’elle existe. Une dimension nulle définit une grille vide. Complétez le test dans les deux boucles fournies.

### Fonction attendue

```python
def cases_balisees(largeur: int, hauteur: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `cases_balisees(3, 2)` renvoie `2`. Dans une grille 3 par 2, les cases (0,0) et (2,1) sont retenues.

**Exemple 2.** `cases_balisees(0, 4)` renvoie `0`. Sans colonne, aucune case n’existe, même avec quatre lignes.

### Conditions sur les données

Vous pouvez supposer que `largeur >= 0 and hauteur >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.3.4, pages imprimées 56–57 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def cases_balisees(largeur: int, hauteur: int) -> int:
    """Comptez les cases qui reçoivent une balise.
    Précondition : largeur >= 0 and hauteur >= 0
    """
    total: int = 0
    x: int = 0
    while x < largeur:
        y: int = 0
        while y < hauteur:
            # Décidez si cette case reçoit une balise.
            y = y + 1
        x = x + 1
    return total
```

---

# S06 · 28 — Deux navettes au même arrêt

**Chapitre 3 · Série 06 — Explorer plusieurs possibilités**

## Situation

Deux navettes partent ensemble à l’ouverture d’un parc puis repassent à intervalles réguliers. Le responsable veut prévoir les encombrements sur une période donnée. Le départ initial n’est pas compté, car les visiteurs ne sont pas encore admis à cet instant.

## Votre mission

Écrivez la fonction `passages_communs`. Comptez les instants où les deux navettes passent ensemble.

Les périodes sont exprimées en minutes entières. La navette A passe aux multiples positifs de `periode_a`, et B aux multiples positifs de `periode_b`. Comptez les minutes communes entre 1 et `fin`, borne finale incluse. Une durée nulle donne zéro passage commun. Parcourez les minutes et vérifiez les deux conditions de passage.

### Fonction attendue

```python
def passages_communs(periode_a: int, periode_b: int, fin: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `passages_communs(2, 3, 12)` renvoie `2`. Les passages communs ont lieu aux minutes 6 et 12 : il y en a deux.

**Exemple 2.** `passages_communs(2, 3, 5)` renvoie `0`. La première rencontre serait à la minute 6, après la fin fixée à 5.

### Conditions sur les données

Vous pouvez supposer que `periode_a > 0 and periode_b > 0 and fin >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.3.4, pages imprimées 56–57 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def passages_communs(periode_a: int, periode_b: int, fin: int) -> int:
    """Comptez les instants où les deux navettes passent ensemble.
    Précondition : periode_a > 0 and periode_b > 0 and fin >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S06 · 29 — Alterner les zones à contrôler

**Chapitre 3 · Série 06 — Explorer plusieurs possibilités**

## Situation

Une équipe inspecte plusieurs zones pendant une campagne de contrôle. La zone numéro z demande z minutes. Pour répartir la charge, une zone n’est inspectée que les jours où la somme de son numéro et du numéro du jour est paire.

## Votre mission

Corrigez la fonction fournie `charge_tournees`. Retournez le nombre total de minutes de contrôle.

Les jours vont de 1 à `jours` et les zones de 1 à `zones`, bornes incluses. Pour chaque couple jour-zone dont la somme est paire, ajoutez le numéro de la zone au total. Comptez du temps, pas seulement des inspections. Aucune zone ou aucune journée donne zéro. Corrigez le compteur de zone qui n’est pas réinitialisé dans le programme.

### Fonction attendue

```python
def charge_tournees(jours: int, zones: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `charge_tournees(2, 3)` renvoie `6`. Le jour 1 coûte 1 + 3 = 4 minutes et le jour 2 coûte 2 minutes : total 6.

**Exemple 2.** `charge_tournees(1, 1)` renvoie `1`. Le seul jour inspecte la zone 1 pour une minute.

### Conditions sur les données

Vous pouvez supposer que `jours >= 0 and zones >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.3.4, pages imprimées 56–57 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def charge_tournees(jours: int, zones: int) -> int:
    """Retournez le nombre total de minutes de contrôle.
    Précondition : jours >= 0 and zones >= 0
    """
    total: int = 0
    j: int = 1
    z: int = 1
    while j <= jours:
        while z <= zones:
            if (j + z) % 2 == 0:
                total = total + z
            z = z + 1
        j = j + 1
    return total
```

---

# S06 · 30 — Préparer une commande sans boîte incomplète

**Chapitre 3 · Série 06 — Explorer plusieurs possibilités**

## Situation

Un fabricant dispose de deux formats de boîtes, contenant respectivement deux et cinq articles. Il souhaite connaître le nombre de façons de préparer une commande sans article restant et sans boîte incomplète. L’ordre des boîtes dans le carton n’a aucune importance.

## Votre mission

Écrivez la fonction `assemblages_boites`. Comptez les répartitions exactes en boîtes de deux et de cinq articles.

Une répartition est définie par un nombre de boîtes de deux et un nombre de boîtes de cinq, tous deux éventuellement nuls. Comptez chaque couple une seule fois. Pour zéro article, le couple sans aucune boîte est une répartition valable : le résultat vaut un. Parcourez les nombres de boîtes possibles avec deux boucles while imbriquées.

### Fonction attendue

```python
def assemblages_boites(articles: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `assemblages_boites(10)` renvoie `2`. Dix articles permettent cinq boîtes de deux ou deux boîtes de cinq : deux répartitions.

**Exemple 2.** `assemblages_boites(0)` renvoie `1`. Une commande vide possède exactement la répartition sans boîte.

### Conditions sur les données

Vous pouvez supposer que `articles >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 3.3.4, pages imprimées 56–57 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def assemblages_boites(articles: int) -> int:
    """Comptez les répartitions exactes en boîtes de deux et de cinq articles.
    Précondition : articles >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S07 · 31 — Distribuer des lots équitables

**Chapitre 4 · Série 07 — Conserver une relation vraie**

## Situation

Un animateur distribue des objets à plusieurs équipes. Il procède par tournées complètes, en donnant exactement un objet à chaque équipe. Dès qu’il ne peut plus terminer une tournée, il conserve tous les objets restants pour une prochaine activité.

## Votre mission

Écrivez la fonction `reste_distribution`. Retournez le nombre d’objets qui ne peuvent plus être distribués équitablement.

`objets` est le stock initial et `equipes` le nombre d’équipes. Une tournée retire exactement autant d’objets qu’il y a d’équipes. Il est interdit de commencer une tournée incomplète. Retournez le stock restant, qui peut être nul. Programmez les soustractions successives sans utiliser `%` ni `//`, puis justifiez pourquoi toutes les équipes reçoivent autant d’objets.

### Fonction attendue

```python
def reste_distribution(objets: int, equipes: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `reste_distribution(14, 4)` renvoie `2`. Trois tournées distribuent 12 objets ; il en reste 2 sur les 14 disponibles.

**Exemple 2.** `reste_distribution(3, 5)` renvoie `3`. Les 3 objets ne permettent aucune tournée auprès de 5 équipes.

### Conditions sur les données

Vous pouvez supposer que `objets >= 0 and equipes > 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Expliquez l’invariant $objets = reste + t \times equipes$, où $t$ est le nombre de tournées terminées. Justifiez que `reste` est un entier naturel qui diminue strictement à chaque tour, puis utilisez la condition d’arrêt pour encadrer le résultat.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.2, pages imprimées 63–69 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def reste_distribution(objets: int, equipes: int) -> int:
    """Retournez le nombre d’objets qui ne peuvent plus être distribués équitablement.
    Précondition : objets >= 0 and equipes > 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S07 · 32 — Appliquer la règle de rendu de monnaie

**Chapitre 4 · Série 07 — Conserver une relation vraie**

## Situation

Une caisse pédagogique ne possède que des pièces de cinq, deux et une unités. Son mécanisme applique une règle précise : tant que possible, il choisit une pièce de cinq ; ensuite des pièces de deux ; enfin une pièce de une si nécessaire.

## Votre mission

Complétez la fonction fournie `pieces_caisse`. Retournez le nombre de pièces distribuées par la règle imposée.

`montant` est la somme entière à rendre. Comptez une pièce à chaque retrait, quel que soit son montant. Le stock de chaque pièce est illimité. Respectez l’ordre cinq, deux, un et retournez le nombre de pièces effectivement sorties. Un montant nul ne demande aucune pièce. Complétez les retraits dans une boucle qui conserve une somme restante non négative.

### Fonction attendue

```python
def pieces_caisse(montant: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `pieces_caisse(12)` renvoie `3`. Douze unités sont rendues avec 5, 5 et 2 : trois pièces.

**Exemple 2.** `pieces_caisse(8)` renvoie `3`. Huit unités sont rendues avec 5, 2 et 1 : trois pièces également.

### Conditions sur les données

Vous pouvez supposer que `montant >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Exprimez une relation entre le montant initial, le reste et la valeur déjà rendue. Le compteur de pièces seul ne donne pas la valeur rendue. Justifiez que chaque branche fait progresser la boucle.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.2, pages imprimées 63–69 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def pieces_caisse(montant: int) -> int:
    """Retournez le nombre de pièces distribuées par la règle imposée.
    Précondition : montant >= 0
    """
    reste: int = montant
    compte: int = 0
    while reste > 0:
        # Remplacez ce retrait par le choix de la pièce autorisée.
        reste = reste - 1
        compte = compte + 1
    return compte
```

---

# S07 · 33 — Une demande limitée par le stock

**Chapitre 4 · Série 07 — Conserver une relation vraie**

## Situation

Une petite boutique reçoit un arrivage régulier avant l’ouverture. Elle satisfait ensuite une demande fixe, mais ne vend jamais un article absent du stock. Les demandes non satisfaites sont abandonnées et ne sont pas reportées au jour suivant.

## Votre mission

Écrivez la fonction `stock_controle`. Retournez le stock après tous les cycles d’approvisionnement et de vente.

`initial` est le stock avant le premier cycle. À chaque cycle, ajoutez `arrivage`, puis retirez `demande` si le stock suffit ; sinon, vendez tout ce qui reste et fixez le stock à zéro. Répétez exactement `tours` fois. Un nombre de cycles nul laisse le stock initial inchangé. Retournez le stock final, pas les ventes cumulées.

### Fonction attendue

```python
def stock_controle(initial: int, arrivage: int, demande: int, tours: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `stock_controle(3, 2, 4, 2)` renvoie `0`. Les stocks après vente sont 1, puis 0 : la seconde demande ne peut être satisfaite entièrement.

**Exemple 2.** `stock_controle(10, 5, 2, 2)` renvoie `16`. Chaque cycle ajoute trois articles nets ; après deux cycles, le stock passe de 10 à 16.

### Conditions sur les données

Vous pouvez supposer que `initial >= 0 and arrivage >= 0 and demande >= 0 and tours >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Justifiez l’invariant `stock >= 0`. Proposez ensuite un variant lié au nombre de cycles restant à effectuer, même lorsque le stock ne change plus.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.2, pages imprimées 63–69 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def stock_controle(initial: int, arrivage: int, demande: int, tours: int) -> int:
    """Retournez le stock après tous les cycles d’approvisionnement et de vente.
    Précondition : initial >= 0 and arrivage >= 0 and demande >= 0 and tours >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S07 · 34 — Ne pas oublier la dernière seconde

**Chapitre 4 · Série 07 — Conserver une relation vraie**

## Situation

Un simulateur de freinage raisonne par secondes entières. Pendant une seconde, le véhicule avance de sa vitesse courante en mètres ; ensuite seulement, sa vitesse diminue de deux unités. La vitesse ne devient jamais négative. Le programme actuel oublie parfois le dernier déplacement.

## Votre mission

Corrigez la fonction fournie `distance_freinage`. Retournez la distance parcourue jusqu’à l’arrêt dans ce modèle discret.

`vitesse` est la vitesse entière initiale. Tant qu’elle est positive, ajoutez sa valeur à la distance, puis diminuez-la de deux, en la ramenant à zéro si nécessaire. Le véhicule déjà immobile parcourt zéro mètre. Corrigez le code en traitant aussi les vitesses impaires, pour lesquelles une dernière seconde à vitesse un doit être comptée.

### Fonction attendue

```python
def distance_freinage(vitesse: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `distance_freinage(5)` renvoie `9`. Les vitesses utilisées sont 5, 3 et 1 : la distance totale vaut 9.

**Exemple 2.** `distance_freinage(4)` renvoie `6`. Avec une vitesse initiale de 4, les déplacements valent 4 puis 2, soit 6 mètres.

### Conditions sur les données

Vous pouvez supposer que `vitesse >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Indiquez ce que contient `distance` avant chaque tour. Montrez que la vitesse courante constitue un variant naturel, y compris lors du dernier tour.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.2, pages imprimées 63–69 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def distance_freinage(vitesse: int) -> int:
    """Retournez la distance parcourue jusqu’à l’arrêt dans ce modèle discret.
    Précondition : vitesse >= 0
    """
    v: int = vitesse
    distance: int = 0
    while v > 1:
        distance = distance + v
        v = v - 2
    return distance
```

---

# S07 · 35 — Comptabiliser les pertes de la cuve

**Chapitre 4 · Série 07 — Conserver une relation vraie**

## Situation

Une cuve reçoit régulièrement de l’eau de pluie. Elle possède une capacité fixe et ne se vide pas pendant l’observation. À chaque apport, seule la quantité qui tient encore dans la cuve est conservée ; le surplus part dans un bac de récupération.

## Votre mission

Écrivez la fonction `eau_debordee`. Retournez le volume cumulé qui a débordé de la cuve.

Tous les volumes sont des litres entiers. `initial` est le volume de départ, `apport` le volume reçu à chaque tour et `capacite` le volume maximal conservé. Simulez exactement `tours` apports et additionnez les débordements successifs. Retournez le volume du bac, pas celui de la cuve. Une capacité nulle est possible ; tout apport déborde alors.

### Fonction attendue

```python
def eau_debordee(initial: int, apport: int, capacite: int, tours: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `eau_debordee(3, 4, 10, 2)` renvoie `1`. La cuve passe de 3 à 7 puis à 10 ; seul un litre du second apport déborde.

**Exemple 2.** `eau_debordee(10, 3, 10, 2)` renvoie `6`. Une cuve pleine perd les deux apports de 3 litres : le bac reçoit 6 litres.

### Conditions sur les données

Vous pouvez supposer que `0 <= initial <= capacite and apport >= 0 and tours >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Écrivez et expliquez l’invariant $initial + t \times apport = stock + pertes$, complété par $0 \leq stock \leq capacite$. Donnez un variant de boucle. La relation de conservation doit rester vraie après un débordement.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.2, pages imprimées 63–69 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def eau_debordee(initial: int, apport: int, capacite: int, tours: int) -> int:
    """Retournez le volume cumulé qui a débordé de la cuve.
    Précondition : 0 <= initial <= capacite and apport >= 0 and tours >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S08 · 36 — Trouver un numéro disponible

**Chapitre 4 · Série 08 — Éviter le travail inutile**

## Situation

Un parking réserve les emplacements dont le numéro est multiple de trois aux véhicules techniques et ceux dont le numéro est multiple de cinq aux livraisons. Un visiteur ordinaire cherche le premier emplacement qu’il a le droit d’utiliser à partir d’un numéro donné.

## Votre mission

Écrivez la fonction `prochaine_place`. Retournez le premier numéro admissible supérieur ou égal au départ.

`depart` est un entier positif et peut lui-même convenir. Un emplacement est admissible seulement si son numéro n’est divisible ni par trois ni par cinq. Examinez les numéros croissants et arrêtez la recherche dès le premier numéro convenable. Retournez ce numéro, pas le nombre d’emplacements examinés. Le parking est supposé prolonger indéfiniment sa numérotation.

### Fonction attendue

```python
def prochaine_place(depart: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `prochaine_place(9)` renvoie `11`. Les numéros 9 et 10 sont réservés ; 11 est le premier numéro admissible.

**Exemple 2.** `prochaine_place(7)` renvoie `7`. Le numéro 7 est déjà autorisé : aucune avancée n’est nécessaire.

### Conditions sur les données

Vous pouvez supposer que `depart >= 1`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Expliquez pourquoi tous les numéros sautés sont interdits. Pour justifier l’existence d’un résultat, vous pouvez observer les numéros de la forme 15k+1.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.3, pages imprimées 69–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def prochaine_place(depart: int) -> int:
    """Retournez le premier numéro admissible supérieur ou égal au départ.
    Précondition : depart >= 1
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S08 · 37 — Planifier hors d’une interruption

**Chapitre 4 · Série 08 — Éviter le travail inutile**

## Situation

Une machine peut démarrer un nouveau cycle uniquement à des minutes multiples d’une période. Une intervention bloque temporairement les démarrages. Le responsable souhaite connaître le premier départ possible après la disponibilité de la commande, sans parcourir toutes les minutes intermédiaires.

## Votre mission

Complétez la fonction fournie `premier_creneau`. Retournez la première minute de départ utilisable.

Le résultat doit être supérieur ou égal à `depart` et multiple de `periode`. Les minutes de `pause_debut` inclus à `pause_fin` exclu sont interdites. Une pause vide ne bloque rien. Complétez le programme en avançant directement d’un créneau au suivant pendant la pause. Un départ exactement à la fin de la pause est autorisé.

### Fonction attendue

```python
def premier_creneau(depart: int, periode: int, pause_debut: int, pause_fin: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `premier_creneau(7, 5, 9, 14)` renvoie `15`. Le premier multiple de 5 après 7 est 10, mais il est bloqué ; 15 est autorisé.

**Exemple 2.** `premier_creneau(12, 3, 6, 12)` renvoie `12`. La minute 12 est à la fin de la pause et constitue déjà un créneau.

### Conditions sur les données

Vous pouvez supposer que `depart >= 0 and periode > 0 and 0 <= pause_debut <= pause_fin`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Justifiez que le premier calcul donne le plus petit multiple admissible avant prise en compte de la pause. Dans la boucle, `pause_fin - t` diminue tant que le créneau reste bloqué.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.3, pages imprimées 69–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def premier_creneau(depart: int, periode: int, pause_debut: int, pause_fin: int) -> int:
    """Retournez la première minute de départ utilisable.
    Précondition : depart >= 0 and periode > 0 and 0 <= pause_debut <= pause_fin
    """
    t: int = ((depart + periode - 1) // periode) * periode
    # Avancez si ce premier créneau appartient à la pause.
    return t
```

---

# S08 · 38 — Regrouper les cycles identiques

**Chapitre 4 · Série 08 — Éviter le travail inutile**

## Situation

Un capteur alterne une minute de réveil et plusieurs minutes de veille. Le même cycle recommence tant que l’appareil reste allumé. Pour prévoir de très longues durées, le technicien veut remplacer une simulation minute par minute par un calcul regroupant les cycles complets.

## Votre mission

Écrivez la fonction `energie_veille`. Calculez l’énergie totale consommée pendant la durée demandée.

Chaque cycle dure `cycle` minutes : sa première minute consomme 8 unités d’énergie, chacune des autres 2 unités. L’observation commence au début d’un cycle et dure exactement `duree` minutes. Calculez séparément les cycles complets et le cycle final éventuellement incomplet. Zéro minute ne consomme rien. Un cycle de durée un ne contient que des minutes de réveil.

### Fonction attendue

```python
def energie_veille(duree: int, cycle: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `energie_veille(7, 3)` renvoie `32`. Sept minutes avec des cycles de trois coûtent 12 + 12 + 8 = 32 unités.

**Exemple 2.** `energie_veille(2, 5)` renvoie `10`. Deux minutes du premier cycle coûtent 8 + 2 = 10 unités.

### Conditions sur les données

Vous pouvez supposer que `duree >= 0 and cycle >= 1`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

N’utilisez aucune boucle. Expliquez pourquoi une fin vide ne doit pas ajouter les 8 unités d’un réveil. Comparez le nombre d’opérations avec une simulation de chaque minute.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.3, pages imprimées 69–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def energie_veille(duree: int, cycle: int) -> int:
    """Calculez l’énergie totale consommée pendant la durée demandée.
    Précondition : duree >= 0 and cycle >= 1
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S08 · 39 — Interrompre le contrôle au bon moment

**Chapitre 4 · Série 08 — Éviter le travail inutile**

## Situation

Un agent contrôle des postes dans l’ordre de leur numérotation. Une alerte impose d’arrêter immédiatement la tournée, après avoir contrôlé le poste concerné. Le journal de test indique à l’avance le numéro de ce poste, ou zéro si aucune alerte ne sera rencontrée.

## Votre mission

Corrigez la fonction fournie `controles_avant_alerte`. Retournez le nombre de postes contrôlés avant l’arrêt de la tournée.

Les postes sont numérotés de 1 à `nombre`. `alerte` vaut zéro en l’absence d’incident ; sinon il donne le poste qui arrête la tournée. Le poste déclencheur compte parmi les contrôles effectués. Corrigez le code pour sortir dès sa rencontre. S’il n’y a aucun poste, le résultat vaut zéro ; sans alerte, tous les postes sont contrôlés.

### Fonction attendue

```python
def controles_avant_alerte(nombre: int, alerte: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `controles_avant_alerte(8, 3)` renvoie `3`. Le contrôle s’arrête au poste 3, donc seuls trois postes sont examinés sur les huit.

**Exemple 2.** `controles_avant_alerte(8, 0)` renvoie `8`. Avec zéro comme indicateur d’alerte, les huit postes sont tous contrôlés.

### Conditions sur les données

Vous pouvez supposer que `nombre >= 0 and 0 <= alerte <= nombre`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Conservez une boucle pour travailler la sortie anticipée. Expliquez pourquoi le retour doit se placer après le comptage du poste courant. Le respect de cette méthode est vérifié par lecture du code.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.3, pages imprimées 69–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def controles_avant_alerte(nombre: int, alerte: int) -> int:
    """Retournez le nombre de postes contrôlés avant l’arrêt de la tournée.
    Précondition : nombre >= 0 and 0 <= alerte <= nombre
    """
    poste: int = 1
    compte: int = 0
    while poste <= nombre:
        compte = compte + 1
        poste = poste + 1
    return compte
```

---

# S08 · 40 — Arrêter quand le bloc est indivisible

**Chapitre 4 · Série 08 — Éviter le travail inutile**

## Situation

Un outil réduit un bloc de données en ne conservant que sa moitié supérieure arrondie. Un utilisateur fixe un nombre maximal de réductions, mais poursuivre après avoir atteint zéro ou un élément serait inutile : la taille ne changerait plus.

## Votre mission

Écrivez la fonction `taille_apres_reductions`. Retournez la taille obtenue après les réductions utiles.

Une réduction remplace une taille T par `(T + 1) // 2`. Effectuez au plus `maximum` réductions et arrêtez-vous aussi dès que la taille est inférieure ou égale à un. Retournez la taille finale, pas le nombre d’étapes. Une limite de zéro réduction laisse le bloc inchangé. La taille nulle doit rester nulle.

### Fonction attendue

```python
def taille_apres_reductions(taille: int, maximum: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `taille_apres_reductions(13, 2)` renvoie `4`. Deux réductions transforment 13 en 7 puis en 4.

**Exemple 2.** `taille_apres_reductions(1, 1000000)` renvoie `1`. Le bloc d’un élément reste identique ; les nombreuses réductions demandées sont inutiles.

### Conditions sur les données

Vous pouvez supposer que `taille >= 0 and maximum >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Expliquez les deux motifs d’arrêt. Montrez que, pour une taille supérieure à un, la nouvelle taille est strictement plus petite. Les tests de résultat ne suffisent pas à prouver l’absence d’itérations inutiles.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.3, pages imprimées 69–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def taille_apres_reductions(taille: int, maximum: int) -> int:
    """Retournez la taille obtenue après les réductions utiles.
    Précondition : taille >= 0 and maximum >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S09 · 41 — Agrandir un espace de stockage

**Chapitre 4 · Série 09 — Auditer des simulations**

## Situation

Un système réserve un espace de stockage de capacité initiale connue. S’il ne suffit pas pour un fichier, il double sa capacité autant de fois que nécessaire. L’administrateur souhaite connaître l’espace qui restera inutilisé après avoir enregistré le fichier.

## Votre mission

Écrivez la fonction `espace_inutilise`. Retournez l’espace libre après les agrandissements nécessaires.

`capacite` et `besoin` sont exprimés dans la même unité entière. Doublez la capacité seulement tant qu’elle est strictement inférieure au besoin. Une capacité déjà suffisante ne doit pas être réduite. Retournez la capacité finale moins le besoin, et non la capacité elle-même. Un besoin nul laisse toute la capacité initiale inutilisée.

### Fonction attendue

```python
def espace_inutilise(capacite: int, besoin: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `espace_inutilise(3, 8)` renvoie `4`. La capacité passe de 3 à 6 puis à 12 ; le fichier de taille 8 laisse 4 unités libres.

**Exemple 2.** `espace_inutilise(10, 4)` renvoie `6`. Les 10 unités suffisent déjà pour 4 unités de données ; il en reste 6.

### Conditions sur les données

Vous pouvez supposer que `capacite >= 1 and besoin >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Montrez que la capacité reste un multiple de la capacité initiale. Pour la terminaison, justifiez qu’elle augmente au moins de un tant qu’elle reste sous le besoin. Ne choisissez pas la capacité croissante comme variant décroissant.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.3, pages imprimées 63–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def espace_inutilise(capacite: int, besoin: int) -> int:
    """Retournez l’espace libre après les agrandissements nécessaires.
    Précondition : capacite >= 1 and besoin >= 0
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S09 · 42 — Acheter des extensions successives

**Chapitre 4 · Série 09 — Auditer des simulations**

## Situation

Dans un simulateur, les extensions d’une base deviennent de plus en plus coûteuses. La première coûte un crédit, la deuxième deux, la troisième quatre ; le prix double après chaque achat. On ne peut pas sauter une extension pour acheter la suivante.

## Votre mission

Complétez la fonction fournie `achats_croissants`. Retournez le nombre d’extensions entièrement achetées.

`credits` est le budget disponible au départ. Achetez tant que le budget restant est supérieur ou égal au prix de la prochaine extension. Soustrayez le prix payé avant de le doubler. Retournez le nombre d’achats, pas le nombre de crédits dépensés. Un budget nul ne permet aucun achat ; une égalité entre prix et budget autorise l’achat.

### Fonction attendue

```python
def achats_croissants(credits: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `achats_croissants(7)` renvoie `3`. Les trois achats coûtent 1 + 2 + 4 = 7 crédits : trois extensions sont obtenues.

**Exemple 2.** `achats_croissants(6)` renvoie `2`. Avec 6 crédits, les prix 1 et 2 sont payés ; les 3 crédits restants ne paient pas 4.

### Conditions sur les données

Vous pouvez supposer que `credits >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Vérifiez que le reste ne devient pas négatif. Justifiez la terminaison malgré la croissance du prix, en donnant une quantité naturelle qui décroît.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.3, pages imprimées 63–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def achats_croissants(credits: int) -> int:
    """Retournez le nombre d’extensions entièrement achetées.
    Précondition : credits >= 0
    """
    reste: int = credits
    prix: int = 1
    compte: int = 0
    while reste >= prix:
        reste = reste - prix
        prix = prix * 2
        # Mémorisez cet achat.
    return compte
```

---

# S09 · 43 — Auditer une séquence de mesures

**Chapitre 4 · Série 09 — Auditer des simulations**

## Situation

Pour tester un logiciel sans brancher de capteur, le laboratoire fabrique une suite de mesures déterministes. Chaque mesure est calculée à partir de son numéro. Le compteur d’alertes doit analyser exactement la quantité demandée, sans inclure une mesure supplémentaire.

## Votre mission

Écrivez la fonction `alertes_capteur`. Comptez les mesures strictement supérieures au seuil.

Les mesures portent les numéros 1 à `nombre` inclus. La mesure de numéro i vaut `(7 * i) % 11`. Elle déclenche une alerte seulement si sa valeur est strictement supérieure à `seuil` ; une égalité ne déclenche rien. Retournez le nombre d’alertes. Avec zéro mesure, aucun calcul de mesure ni aucune alerte n’est nécessaire.

### Fonction attendue

```python
def alertes_capteur(nombre: int, seuil: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `alertes_capteur(4, 5)` renvoie `3`. Les quatre mesures sont 7, 3, 10 et 6 ; trois dépassent strictement 5.

**Exemple 2.** `alertes_capteur(4, 10)` renvoie `0`. Les mêmes mesures ne dépassent jamais strictement 10 : aucune alerte.

### Conditions sur les données

Vous pouvez supposer que `nombre >= 0 and 0 <= seuil <= 10`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Donnez un invariant liant le compteur d’alertes aux mesures déjà parcourues. Distinguez le nombre de mesures analysées et l’indice de la prochaine mesure.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.3, pages imprimées 63–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def alertes_capteur(nombre: int, seuil: int) -> int:
    """Comptez les mesures strictement supérieures au seuil.
    Précondition : nombre >= 0 and 0 <= seuil <= 10
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S09 · 44 — Garder la plus grande charge observée

**Chapitre 4 · Série 09 — Auditer des simulations**

## Situation

Un modèle de charge modifie sa valeur à chaque pas de simulation. Lorsque la charge est paire, elle est divisée par deux ; lorsqu’elle est impaire, trois unités sont ajoutées. Le responsable veut conserver le pic atteint, même si la charge baisse ensuite.

## Votre mission

Corrigez la fonction fournie `pic_charge`. Retournez la plus grande charge observée, état initial compris.

Partez de `initial` et appliquez exactement `tours` transformations. Le maximum recherché comprend la valeur initiale et toutes les valeurs obtenues après une transformation. Une charge paire utilise une division entière par deux. Avec zéro tour, retournez l’état initial. Corrigez le code qui retourne seulement la dernière charge au lieu de conserver la plus grande.

### Fonction attendue

```python
def pic_charge(initial: int, tours: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `pic_charge(5, 3)` renvoie `8`. Les états sont 5, 8, 4 et 2 ; la plus grande valeur observée est 8.

**Exemple 2.** `pic_charge(8, 2)` renvoie `8`. Les états 8, 4 et 2 ne dépassent jamais la charge initiale de 8.

### Conditions sur les données

Vous pouvez supposer que `initial >= 0 and tours >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

La charge peut monter ou descendre : elle ne constitue pas un variant de cette boucle. Expliquez le rôle du compteur de tours et l’invariant décrivant le pic.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.3, pages imprimées 63–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def pic_charge(initial: int, tours: int) -> int:
    """Retournez la plus grande charge observée, état initial compris.
    Précondition : initial >= 0 and tours >= 0
    """
    charge: int = initial
    i: int = 0
    while i < tours:
        if charge % 2 == 0:
            charge = charge // 2
        else:
            charge = charge + 3
        i = i + 1
    return charge
```

---

# S09 · 45 — Deux robots se rapprochent

**Chapitre 4 · Série 09 — Auditer des simulations**

## Situation

Deux robots se déplacent sur le même axe gradué. À chaque tour simultané, le robot situé initialement à gauche avance de deux unités et celui situé à droite recule de une unité. L’expérience s’arrête quand le premier rejoint ou dépasse le second.

## Votre mission

Écrivez la fonction `rencontre_robots`. Retournez le nombre de tours nécessaires pour que le robot gauche rejoigne ou dépasse l’autre.

`gauche` et `droite` sont les positions initiales et peuvent être négatives. Effectuez les deux déplacements avant de compter un tour terminé. Il n’est pas nécessaire que les robots occupent exactement la même position : un dépassement suffit. S’ils sont déjà ensemble, retournez zéro. Le résultat attendu est un nombre de tours, pas une position finale.

### Fonction attendue

```python
def rencontre_robots(gauche: int, droite: int) -> int:
```

### Exemples expliqués

**Exemple 1.** `rencontre_robots(0, 7)` renvoie `3`. Les positions passent de (0,7) à (2,6), puis (4,5), puis (6,4) : trois tours.

**Exemple 2.** `rencontre_robots(4, 4)` renvoie `0`. Les robots sont déjà au même endroit : aucun déplacement n’est demandé.

### Conditions sur les données

Vous pouvez supposer que `gauche <= droite`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Exprimez les deux positions après t tours. L’écart diminue de trois, mais peut devenir négatif : expliquez pourquoi le nombre de tours restant, obtenu en arrondissant l’écart positif divisé par trois vers le haut, justifie l’arrêt.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 4.1–4.3, pages imprimées 63–78 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def rencontre_robots(gauche: int, droite: int) -> int:
    """Retournez le nombre de tours nécessaires pour que le robot gauche rejoigne ou dépasse l’autre.
    Précondition : gauche <= droite
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S10 · 46 — Dessiner les graduations d’une règle

**Chapitre 5 · Série 10 — Fabriquer des étiquettes**

## Situation

Un logiciel dessine une règle graduée avec un caractère par position entière. Les grandes graduations apparaissent à intervalles réguliers ; les positions intermédiaires sont représentées par des points. La règle peut commencer avant zéro pour représenter une mesure signée.

## Votre mission

Écrivez la fonction `marquages_regle`. Construisez la ligne de graduations correspondant à l’intervalle demandé.

Parcourez les entiers de `debut` inclus à `fin` exclu. Pour chaque entier multiple de `pas`, ajoutez le caractère `|` ; pour les autres, ajoutez `.`. Les multiples négatifs et zéro suivent la même règle. Si debut est supérieur ou égal à fin, retournez une chaîne vide. N’ajoutez ni espace ni retour à la ligne.

### Fonction attendue

```python
def marquages_regle(debut: int, fin: int, pas: int) -> str:
```

### Exemples expliqués

**Exemple 1.** `marquages_regle(0, 7, 3)` renvoie `'|..|..|'`. Les positions 0, 3 et 6 reçoivent une barre ; les autres positions jusqu’à 6 reçoivent un point.

**Exemple 2.** `marquages_regle(-2, 3, 2)` renvoie `'|.|.|'`. Entre −2 inclus et 3 exclu, les multiples de deux sont −2, 0 et 2.

### Conditions sur les données

Vous pouvez supposer que `pas > 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez `for`, `range` et la concaténation. Attention à la borne finale exclue.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.1–5.2, pages imprimées 81–92 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def marquages_regle(debut: int, fin: int, pas: int) -> str:
    """Construisez la ligne de graduations correspondant à l’intervalle demandé.
    Précondition : pas > 0
    """
    # Écrivez votre programme ici.
    return ""
```

---

# S10 · 47 — Un badge quand un nom manque

**Chapitre 5 · Série 10 — Fabriquer des étiquettes**

## Situation

Un atelier imprime des badges abrégés à partir d’un prénom et d’un nom. Certains participants n’ont renseigné qu’un des deux champs. Le logiciel doit produire un badge correct dans tous les cas, sans tenter de lire le premier caractère d’une chaîne vide.

## Votre mission

Complétez la fonction fournie `initiales_badge`. Retournez les initiales disponibles, chacune suivie d’un point.

Pour chaque champ non vide, prenez exactement son premier caractère et ajoutez un point. Traitez le prénom avant le nom. Un champ vide ne produit rien, pas même un point. Conservez les caractères tels quels : aucune conversion en majuscule et aucune suppression d’espace ne sont demandées. Deux champs vides produisent une chaîne vide.

### Fonction attendue

```python
def initiales_badge(prenom: str, nom: str) -> str:
```

### Exemples expliqués

**Exemple 1.** `initiales_badge('Alice', 'Durand')` renvoie `'A.D.'`. Le premier caractère de chaque champ donne A. puis D., sans espace entre les deux.

**Exemple 2.** `initiales_badge('', 'Lee')` renvoie `'L.'`. Le prénom est absent : seule l’initiale L. du nom apparaît.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.1–5.2, pages imprimées 81–92 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def initiales_badge(prenom: str, nom: str) -> str:
    """Retournez les initiales disponibles, chacune suivie d’un point.
    """
    resultat: str = ""
    if len(prenom) > 0:
        resultat = resultat + prenom[0] + "."
    # Traitez maintenant le champ nom.
    return resultat
```

---

# S10 · 48 — Afficher seulement la fin d’une référence

**Chapitre 5 · Série 10 — Fabriquer des étiquettes**

## Situation

Une application affiche des références de réservation sur un écran public. Pour limiter les informations visibles, elle cache le début de chaque référence avec des étoiles et conserve seulement un nombre choisi de caractères à la fin. La longueur affichée doit rester identique.

## Votre mission

Écrivez la fonction `masquer_reference`. Retournez la référence dont seul le suffixe autorisé est visible.

`visibles` est le nombre maximal de caractères conservés à droite. Remplacez chacun des caractères précédents par une étoile `*`. Si visibles vaut zéro, masquez toute la référence. Si visibles dépasse sa longueur, conservez tout le texte. Une référence vide reste vide. Les espaces éventuels comptent comme des caractères et suivent exactement la même règle.

### Fonction attendue

```python
def masquer_reference(reference: str, visibles: int) -> str:
```

### Exemples expliqués

**Exemple 1.** `masquer_reference('AB1245', 3)` renvoie `'***245'`. Seuls les trois derniers caractères 245 restent visibles ; les trois premiers deviennent des étoiles.

**Exemple 2.** `masquer_reference('XY', 5)` renvoie `'XY'`. La référence compte deux caractères, moins que les cinq autorisés : elle reste entière.

### Conditions sur les données

Vous pouvez supposer que `visibles >= 0`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Parcourez les indices avec `range`. Évitez un découpage `[-visibles:]` non protégé : lorsque visibles vaut zéro, cet indice vaut aussi zéro.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.1–5.2, pages imprimées 81–92 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def masquer_reference(reference: str, visibles: int) -> str:
    """Retournez la référence dont seul le suffixe autorisé est visible.
    Précondition : visibles >= 0
    """
    # Écrivez votre programme ici.
    return ""
```

---

# S10 · 49 — Recaler le début d’une étiquette

**Chapitre 5 · Série 10 — Fabriquer des étiquettes**

## Situation

Une imprimante circulaire a commencé à lire une étiquette au mauvais endroit. Pour préparer une nouvelle impression, on souhaite déplacer un préfixe du texte vers la fin. Aucun caractère ne doit être perdu, dupliqué ou inversé pendant cette opération.

## Votre mission

Corrigez la fonction fournie `rotation_etiquette`. Déplacez les premiers caractères à la fin en conservant leur ordre.

`decalage` est le nombre de caractères à retirer du début puis à ajouter à la fin. Conservez l’ordre à l’intérieur des deux morceaux. Un décalage nul et un décalage égal à la longueur doivent rendre le texte original. Corrigez l’erreur de borne dans le découpage fourni. La chaîne vide est autorisée avec un décalage nul.

### Fonction attendue

```python
def rotation_etiquette(texte: str, decalage: int) -> str:
```

### Exemples expliqués

**Exemple 1.** `rotation_etiquette('ABCDE', 2)` renvoie `'CDEAB'`. Le préfixe AB passe après CDE : le résultat est CDEAB.

**Exemple 2.** `rotation_etiquette('abc', 0)` renvoie `'abc'`. Avec un décalage nul, aucun caractère ne change de place.

### Conditions sur les données

Vous pouvez supposer que `0 <= decalage <= len(texte)`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez deux découpages et une concaténation. Expliquez pourquoi le caractère d’indice decalage appartient uniquement au second morceau du texte initial.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.1–5.2, pages imprimées 81–92 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def rotation_etiquette(texte: str, decalage: int) -> str:
    """Déplacez les premiers caractères à la fin en conservant leur ordre.
    Précondition : 0 <= decalage <= len(texte)
    """
    return texte[decalage:len(texte)] + texte[0:decalage + 1]
```

---

# S10 · 50 — Remplir une cellule de largeur fixe

**Chapitre 5 · Série 10 — Fabriquer des étiquettes**

## Situation

Un petit terminal affiche des tableaux sans bibliothèque de mise en page. Chaque cellule doit occuper une largeur intérieure fixe pour que les séparateurs verticaux s’alignent. Les emplacements laissés libres après le texte sont rendus visibles par des traits de soulignement.

## Votre mission

Écrivez la fonction `ligne_tableau`. Retournez une cellule encadrée et complétée à droite.

Commencez par une barre `|`, ajoutez `texte`, complétez avec assez de caractères `_` pour atteindre `largeur` caractères à l’intérieur, puis ajoutez la barre finale. La largeur ne comprend pas les deux barres. Ne tronquez jamais le texte. Une largeur nulle avec un texte vide produit deux barres voisines. N’ajoutez aucun espace automatiquement.

### Fonction attendue

```python
def ligne_tableau(texte: str, largeur: int) -> str:
```

### Exemples expliqués

**Exemple 1.** `ligne_tableau('chat', 6)` renvoie `'|chat__|'`. Le mot chat occupe quatre des six positions intérieures ; deux soulignements complètent la cellule.

**Exemple 2.** `ligne_tableau('', 0)` renvoie `'||'`. La cellule de largeur zéro n’a pas de contenu entre ses deux barres.

### Conditions sur les données

Vous pouvez supposer que `largeur >= len(texte)`. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Construisez le remplissage avec une boucle for, sans méthode de formatage ni multiplication d’une chaîne.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.1–5.2, pages imprimées 81–92 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def ligne_tableau(texte: str, largeur: int) -> str:
    """Retournez une cellule encadrée et complétée à droite.
    Précondition : largeur >= len(texte)
    """
    # Écrivez votre programme ici.
    return ""
```

---

# S11 · 51 — Compter des blocs sans utiliser split

**Chapitre 5 · Série 11 — Analyser des journaux**

## Situation

Une messagerie reçoit parfois des textes contenant plusieurs espaces de suite ou des espaces aux extrémités. Pour son compteur simplifié, elle appelle mot toute suite non vide de caractères qui ne sont pas des espaces simples. La ponctuation ne coupe pas un mot.

## Votre mission

Écrivez la fonction `compter_mots_message`. Comptez les blocs non vides séparés par des espaces simples.

Seul le caractère espace `" "` sépare les mots. Plusieurs espaces consécutifs forment une seule séparation et ne créent pas de mots vides. Les espaces au début et à la fin sont ignorés pour le comptage. Une tabulation reste un caractère ordinaire. Retournez zéro pour une chaîne vide ou composée uniquement d’espaces, sans utiliser `split`.

### Fonction attendue

```python
def compter_mots_message(message: str) -> int:
```

### Exemples expliqués

**Exemple 1.** `compter_mots_message('  salut  tout le-monde ')` renvoie `3`. Les blocs salut, tout et le-monde sont les trois mots ; le tiret ne coupe pas le dernier.

**Exemple 2.** `compter_mots_message('   ')` renvoie `0`. Les trois espaces ne contiennent aucun bloc non vide.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez un booléen indiquant si le parcours est déjà dans un mot. Un nouveau mot est compté uniquement à son premier caractère.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.1, pages imprimées 93–101 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def compter_mots_message(message: str) -> int:
    """Comptez les blocs non vides séparés par des espaces simples.
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S11 · 52 — Repérer la plus longue période active

**Chapitre 5 · Série 11 — Analyser des journaux**

## Situation

Un appareil écrit un caractère à chaque relevé. Le caractère 1 indique qu’il est actif ; tout autre caractère signale une interruption de l’activité observée. Le technicien recherche la plus longue période active ininterrompue, même si elle se termine exactement à la fin du journal.

## Votre mission

Complétez la fonction fournie `plus_longue_activation`. Retournez la longueur du plus long bloc de caractères 1 consécutifs.

Comptez uniquement les caractères `"1"` consécutifs. Un zéro, un espace ou tout autre caractère remet la longueur courante à zéro. Retournez la plus grande longueur rencontrée, pas le nombre total de caractères 1. S’il n’y a aucune activation, le résultat vaut zéro. Complétez le programme pour mémoriser un maximum pendant le parcours.

### Fonction attendue

```python
def plus_longue_activation(journal: str) -> int:
```

### Exemples expliqués

**Exemple 1.** `plus_longue_activation('11011101')` renvoie `3`. Les blocs actifs ont pour longueurs 2, 3 et 1 ; le plus long mesure 3.

**Exemple 2.** `plus_longue_activation('001111')` renvoie `4`. La dernière séquence de quatre caractères 1 doit être entièrement prise en compte.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.1, pages imprimées 93–101 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def plus_longue_activation(journal: str) -> int:
    """Retournez la longueur du plus long bloc de caractères 1 consécutifs.
    """
    courant: int = 0
    maximum: int = 0
    c: str
    for c in journal:
        if c == "1":
            courant = courant + 1
            # Mettez à jour le maximum si nécessaire.
        else:
            courant = 0
    return maximum
```

---

# S11 · 53 — Retrouver le premier niveau qui redescend

**Chapitre 5 · Série 11 — Analyser des journaux**

## Situation

Un appareil enregistre des niveaux sous la forme de caractères comparables. Le responsable souhaite localiser la première baisse par rapport au relevé immédiatement précédent. Il a besoin de l’indice du nouveau relevé, afin de retrouver le moment où la baisse a été observée.

## Votre mission

Écrivez la fonction `premiere_baisse`. Retournez l’indice de la première baisse, ou None s’il n’y en a pas.

Comparez les caractères suivant l’ordre des chaînes Python, sensible à la casse. Pour un journal de chiffres, cet ordre coïncide avec celui des chiffres de zéro à neuf. Cherchez le premier indice i strictement positif tel que niveaux[i] soit inférieur à niveaux[i−1]. Une égalité n’est pas une baisse. Retournez None s’il n’existe pas, notamment pour zéro ou un caractère.

### Fonction attendue

```python
def premiere_baisse(niveaux: str) -> Optional[int]:
```

Import fourni dans le code de départ : `from typing import Optional`.

### Exemples expliqués

**Exemple 1.** `premiere_baisse('124355')` renvoie `3`. Le premier recul est de 4 vers 3 ; le caractère 3 se trouve à l’indice 3.

**Exemple 2.** `premiere_baisse('1229')` renvoie `None`. Les niveaux ne diminuent jamais ; l’égalité entre les deux caractères 2 est autorisée.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

`Optional[int]` signifie que la réponse peut être un entier ou la valeur `None`. Commencez le parcours à l’indice 1 pour pouvoir comparer au précédent, et sortez dès la première baisse.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.1, pages imprimées 93–101 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
from typing import Optional

def premiere_baisse(niveaux: str) -> Optional[int]:
    """Retournez l’indice de la première baisse, ou None s’il n’y en a pas.
    """
    # Écrivez votre programme ici.
    return None
```

---

# S11 · 54 — Vérifier les entrées et les sorties

**Chapitre 5 · Série 11 — Analyser des journaux**

## Situation

Une salle possède un compteur d’entrées et de sorties. Le journal utilise E pour une entrée et S pour une sortie ; les autres caractères sont des annotations. Avant de valider le journal, il faut vérifier qu’aucune personne ne sort d’une salle vide et que tout le monde est finalement sorti.

## Votre mission

Corrigez la fonction fournie `journal_coherent`. Indiquez si le journal décrit une salle initialement et finalement vide, sans sortie impossible.

Partez de zéro personne. Chaque `E` ajoute une personne et chaque `S` en retire une ; ignorez les autres caractères, y compris les lettres minuscules. Retournez False dès qu’une sortie rendrait l’effectif négatif. À la fin, l’effectif doit être exactement zéro. Le journal vide est cohérent. Corrigez le programme qui ne vérifie que le bilan final.

### Fonction attendue

```python
def journal_coherent(journal: str) -> bool:
```

### Exemples expliqués

**Exemple 1.** `journal_coherent('EESS')` renvoie `True`. Deux entrées précèdent les deux sorties : le journal est cohérent et la salle finit vide.

**Exemple 2.** `journal_coherent('SE')` renvoie `False`. Le bilan final est nul, mais la première sortie est impossible : le journal doit être refusé.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.1, pages imprimées 93–101 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def journal_coherent(journal: str) -> bool:
    """Indiquez si le journal décrit une salle initialement et finalement vide, sans sortie impossible.
    """
    effectif: int = 0
    c: str
    for c in journal:
        if c == "E":
            effectif = effectif + 1
        elif c == "S":
            effectif = effectif - 1
    return effectif == 0
```

---

# S11 · 55 — Compter les changements d’état

**Chapitre 5 · Série 11 — Analyser des journaux**

## Situation

Un système enregistre son mode de fonctionnement avec un caractère par relevé. Plusieurs relevés identiques peuvent se suivre lorsque rien ne change. Le responsable veut compter les transitions réelles et ne souhaite pas considérer le premier état comme un changement.

## Votre mission

Écrivez la fonction `changements_mode`. Retournez le nombre de changements entre deux relevés consécutifs.

Deux caractères consécutifs différents comptent pour un changement, même si l’appareil revient ensuite dans un état déjà rencontré. Les majuscules, minuscules et espaces sont des états distincts. Retournez zéro pour un journal vide ou réduit à un seul caractère. Ne comptez ni le nombre de modes distincts ni le nombre total de blocs de caractères.

### Fonction attendue

```python
def changements_mode(journal: str) -> int:
```

### Exemples expliqués

**Exemple 1.** `changements_mode('AAABBA')` renvoie `2`. Les transitions A vers B puis B vers A donnent deux changements.

**Exemple 2.** `changements_mode('xxxx')` renvoie `0`. Les quatre relevés montrent toujours le même état : aucun changement.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Parcourez les indices à partir de 1. Expliquez pourquoi un journal non vide avec b blocs consécutifs possède b−1 changements.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.1, pages imprimées 93–101 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def changements_mode(journal: str) -> int:
    """Retournez le nombre de changements entre deux relevés consécutifs.
    """
    # Écrivez votre programme ici.
    return 0
```

---

# S12 · 56 — Nettoyer une ligne saisie au clavier

**Chapitre 5 · Série 12 — Nettoyer et interpréter des messages**

## Situation

Un formulaire laisse parfois passer des espaces superflus dans une ligne de texte. Avant d’imprimer la ligne, on veut retirer les espaces au début et à la fin, puis réduire chaque suite intérieure d’espaces à une seule séparation. Les autres caractères doivent rester dans leur ordre initial.

## Votre mission

Écrivez la fonction `normaliser_espaces`. Retournez le texte sans espaces aux extrémités et avec un seul espace entre les blocs.

Traitez uniquement le caractère espace simple `" "` ; une tabulation doit rester intacte. Une chaîne vide ou faite uniquement d’espaces devient vide. Aucun espace ne doit apparaître dans le résultat avant le premier caractère utile ni après le dernier. Construisez une nouvelle chaîne par parcours, sans employer `strip`, `split`, `join` ni `replace`.

### Fonction attendue

```python
def normaliser_espaces(texte: str) -> str:
```

### Exemples expliqués

**Exemple 1.** `normaliser_espaces('  bon   jour  ')` renvoie `'bon jour'`. Les espaces extérieurs disparaissent et les trois espaces entre bon et jour deviennent un seul.

**Exemple 2.** `normaliser_espaces('   ')` renvoie `''`. Une ligne constituée uniquement d’espaces ne contient aucun caractère à conserver.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Vous pouvez retarder l’écriture d’un espace jusqu’à la rencontre du prochain caractère utile. Ainsi, les espaces finaux ne sont jamais écrits.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.2–5.3.3, pages imprimées 101–107 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def normaliser_espaces(texte: str) -> str:
    """Retournez le texte sans espaces aux extrémités et avec un seul espace entre les blocs.
    """
    # Écrivez votre programme ici.
    return ""
```

---

# S12 · 57 — Encoder les bits sans perdre les séparateurs

**Chapitre 5 · Série 12 — Nettoyer et interpréter des messages**

## Situation

Un dispositif de transmission représente chaque bit par deux caractères pour rendre ses transitions visibles. Les techniciens ajoutent parfois des espaces ou des tirets dans le signal pour séparer les groupes. Ces annotations doivent rester telles quelles dans le texte encodé.

## Votre mission

Complétez la fonction fournie `coder_signal`. Encodez chaque bit et conservez les autres caractères.

Remplacez chaque caractère `0` du signal d’origine par `01` et chaque `1` par `10`. Copiez tous les autres caractères une seule fois, sans modification. Ne réencodez pas les caractères que vous venez d’ajouter au résultat. Une chaîne vide reste vide. Complétez le traitement du bit un dans le parcours fourni.

### Fonction attendue

```python
def coder_signal(signal: str) -> str:
```

### Exemples expliqués

**Exemple 1.** `coder_signal('010')` renvoie `'011001'`. Les bits 0, 1 et 0 deviennent respectivement 01, 10 et 01, soit 011001.

**Exemple 2.** `coder_signal('1-0')` renvoie `'10-01'`. Le tiret reste unique entre le code 10 du bit 1 et le code 01 du bit 0.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.2–5.3.3, pages imprimées 101–107 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def coder_signal(signal: str) -> str:
    """Encodez chaque bit et conservez les autres caractères.
    """
    resultat: str = ""
    c: str
    for c in signal:
        if c == "0":
            resultat = resultat + "01"
        else:
            # Ajoutez une branche pour encoder le bit 1.
            resultat = resultat + c
    return resultat
```

---

# S12 · 58 — Extraire la partie utile d’une ligne

**Chapitre 5 · Série 12 — Nettoyer et interpréter des messages**

## Situation

Un fichier de configuration simplifié autorise un commentaire après un caractère dièse. Le programme qui lit ce fichier doit conserver la partie utile de chaque ligne et ignorer le reste. Dans ce format pédagogique, il n’existe ni guillemets protecteurs ni caractères d’échappement.

## Votre mission

Écrivez la fonction `couper_commentaire`. Retournez tout ce qui précède le premier marqueur de commentaire.

Le premier caractère `#` commence toujours un commentaire et n’appartient pas au résultat. Tout ce qui le suit est ignoré, même si d’autres dièses apparaissent. Si aucun dièse n’existe, retournez la ligne entière. Conservez exactement les espaces situés avant le marqueur. Un dièse en première position produit une chaîne vide ; une ligne vide aussi.

### Fonction attendue

```python
def couper_commentaire(ligne: str) -> str:
```

### Exemples expliqués

**Exemple 1.** `couper_commentaire('nom=Eva #élève')` renvoie `'nom=Eva '`. Les caractères nom=Eva et l’espace suivant sont conservés ; le commentaire est supprimé.

**Exemple 2.** `couper_commentaire('#tout ignorer')` renvoie `''`. Un commentaire qui commence dès le premier caractère ne laisse aucune partie utile.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez un parcours avec sortie anticipée. N’utilisez ni `split` ni `find`. Les guillemets éventuels sont des caractères ordinaires.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.2–5.3.3, pages imprimées 101–107 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def couper_commentaire(ligne: str) -> str:
    """Retournez tout ce qui précède le premier marqueur de commentaire.
    """
    # Écrivez votre programme ici.
    return ""
```

---

# S12 · 59 — Lire la première annotation entre crochets

**Chapitre 5 · Série 12 — Nettoyer et interpréter des messages**

## Situation

Un journal contient des annotations entourées de crochets au milieu du texte courant. On souhaite extraire le contenu qui suit la première ouverture et précède la première fermeture rencontrée ensuite. Le format est volontairement simple et ne gère pas les annotations imbriquées.

## Votre mission

Corrigez la fonction fournie `contenu_balise`. Retournez le contenu de la première annotation complète.

Ignorez tout ce qui précède le premier `[` ainsi que les `]` rencontrés avant cette ouverture. Après l’ouverture, le premier `]` termine l’annotation. Un nouveau `[` à l’intérieur est un caractère ordinaire. Si aucune ouverture ou aucune fermeture correspondante n’existe, retournez une chaîne vide. Les crochets extérieurs ne doivent jamais faire partie du résultat.

### Fonction attendue

```python
def contenu_balise(texte: str) -> str:
```

### Exemples expliqués

**Exemple 1.** `contenu_balise('avant[ok]apres[non]')` renvoie `'ok'`. Seul le contenu ok de la première annotation est extrait ; la seconde est ignorée.

**Exemple 2.** `contenu_balise('avant[incomplet')` renvoie `''`. L’ouverture n’est jamais suivie d’une fermeture : aucune annotation complète n’est disponible.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.2–5.3.3, pages imprimées 101–107 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def contenu_balise(texte: str) -> str:
    """Retournez le contenu de la première annotation complète.
    """
    ouvert: bool = False
    resultat: str = ""
    c: str
    for c in texte:
        if ouvert:
            if c == "]":
                return resultat
            resultat = resultat + c
        elif c == "[":
            ouvert = True
    return resultat
```

---

# S12 · 60 — Interpréter une touche de répétition

**Chapitre 5 · Série 12 — Nettoyer et interpréter des messages**

## Situation

Un clavier simplifié possède une touche plus qui répète le dernier caractère ordinaire tapé. Les autres caractères sont écrits normalement. Plusieurs pressions sur plus doivent continuer à répéter le même caractère ; elles ne remplacent pas la mémoire du dernier caractère ordinaire.

## Votre mission

Écrivez la fonction `executer_repetitions`. Construisez le texte produit par les caractères ordinaires et la commande plus.

Parcourez `commandes` de gauche à droite. Un caractère différent de `+` est ajouté au résultat et devient le caractère mémorisé, y compris s’il s’agit d’un espace. Un `+` ajoute une copie du caractère mémorisé ; sans caractère mémorisé, il est ignoré. Les plus ne sont jamais écrits eux-mêmes. Une commande vide produit un texte vide.

### Fonction attendue

```python
def executer_repetitions(commandes: str) -> str:
```

### Exemples expliqués

**Exemple 1.** `executer_repetitions('ab++c+')` renvoie `'abbbcc'`. Après ab, les deux plus ajoutent deux b ; après c, le dernier plus ajoute un c : abbbcc.

**Exemple 2.** `executer_repetitions('++x+')` renvoie `'xx'`. Les deux premiers plus sont ignorés ; x est ensuite écrit puis répété une fois.

### Conditions sur les données

Les paramètres respectent les types de la signature. Vous n’avez pas à demander de saisie au clavier ni à gérer d’autres types de données. Les règles ci-dessus précisent les situations limites à traiter.

### Méthode et justification

Utilisez une chaîne pour mémoriser le dernier caractère ordinaire. Sa valeur initiale peut être la chaîne vide : ajouter celle-ci n’a aucun effet.

Retournez le résultat avec `return` ; un affichage avec `print` ne remplace pas la valeur demandée. Conservez la signature et annotez les variables locales.

*Notions mobilisées : sections 5.3.2–5.3.3, pages imprimées 101–107 du cours fourni. Les tests portent sur les résultats ; les méthodes imposées et les justifications sont relues par le professeur.*

### Code de départ

```python
def executer_repetitions(commandes: str) -> str:
    """Construisez le texte produit par les caractères ordinaires et la commande plus.
    """
    # Écrivez votre programme ici.
    return ""
```
