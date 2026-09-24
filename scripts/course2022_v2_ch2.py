from course2022_v2_core import ex

ex(1,'ruban_affiches','Découper un rouleau sans gaspillage','nombre: int, hauteur: float, separation: float','float',
   'Calculez la longueur de papier nécessaire pour imprimer une rangée d’affiches.','nombre >= 1 and hauteur > 0 and separation >= 0',
   'Un atelier imprime plusieurs affiches à la suite sur un même rouleau. Chaque affiche occupe une hauteur connue. Pour permettre la découpe, une bande de papier est laissée entre deux affiches voisines, mais aucune bande supplémentaire ne doit être prévue aux deux extrémités.',
   '`nombre` est le nombre d’affiches, `hauteur` leur hauteur en centimètres et `separation` la largeur de chaque bande, dans la même unité. Retournez une longueur en centimètres. Pour une seule affiche, aucune séparation n’est nécessaire. Une séparation nulle est autorisée. Décomposez votre calcul en papier imprimé et papier réservé à la découpe.',
   ['Les trois affiches occupent 90 cm et les deux séparations 4 cm : il faut 94 cm.', 'Une seule affiche occupe 12,5 cm ; la séparation de 4 cm ne sert pas.'],
   [('3, 30.0, 2.0',94.0),('1, 12.5, 4.0',12.5),('2, 10.0, 0.0',20.0),('4, 2.5, 0.5',11.5),('10, 1.0, 1.0',19.0),('2, 1.2, 0.1',2.5)],
   'impression: float = nombre * hauteur\ndecoupe: float = (nombre - 1) * separation\nreturn impression + decoupe',
   method='Utilisez deux variables locales pour les deux contributions. Aucune boucle n’est nécessaire.')

ex(1,'autonomie_robot','Une réserve à ne pas consommer','charge: float, reserve: float, consommation: float','float',
   'Retournez le nombre d’heures pendant lesquelles le robot peut travailler avant d’atteindre sa réserve.','0 <= reserve <= charge and consommation > 0',
   'Un robot d’inventaire doit conserver une partie de sa batterie pour rejoindre sa base. Le responsable connaît l’énergie actuellement disponible, la réserve à protéger et la consommation horaire pendant le travail. Il veut une durée prévisionnelle, pas une heure d’arrivée arrondie.',
   '`charge` et `reserve` sont des énergies en Wh ; `consommation` est une énergie consommée par heure, en Wh/h. Le robot peut utiliser exactement la différence entre charge et réserve. Retournez une durée réelle en heures. Si la charge est déjà égale à la réserve, le résultat vaut zéro. Ne convertissez pas la durée en minutes.',
   ['Il reste 90 Wh utilisables ; à 30 Wh/h, ils permettent 3 heures de travail.', 'Toute l’énergie est réservée au retour : aucune durée de travail n’est disponible.'],
   [('120.0, 30.0, 30.0',3.0),('50.0, 50.0, 8.0',0.0),('0.0, 0.0, 2.0',0.0),('25.0, 0.0, 10.0',2.5),('10.0, 4.0, 8.0',0.75),('100.0, 10.0, 20.0',4.5)],
   'utilisable: float = charge - reserve\nreturn utilisable / consommation',kind='complete',
   starter='utilisable: float = charge - reserve\n# Convertissez cette énergie en une durée de travail.\nreturn 0.0')

ex(1,'dalles_bordure','Compter les dalles du pourtour','largeur: int, longueur: int','int',
   'Calculez combien de dalles appartiennent au bord d’une terrasse rectangulaire.','largeur >= 2 and longueur >= 2',
   'Une terrasse est recouverte d’une grille rectangulaire de dalles identiques. Le jardinier souhaite peindre uniquement les dalles du pourtour. Une dalle d’angle appartient à deux côtés, mais elle ne sera peinte qu’une fois : la commande de peinture doit donc éviter de la compter deux fois.',
   '`largeur` et `longueur` donnent le nombre de dalles dans les deux directions, et non des longueurs en mètres. Comptez toute dalle située sur la première ou la dernière ligne, ou sur la première ou la dernière colonne. Si une dimension vaut 2, toutes les dalles sont sur le bord. Retournez un entier.',
   ['Une grille de 4 par 5 contient 20 dalles, dont 6 à l’intérieur : 14 sont au bord.', 'Une terrasse de deux dalles de large n’a pas de dalle intérieure : les 6 sont à peindre.'],
   [('4, 5',14),('2, 3',6),('2, 2',4),('3, 3',8),('10, 4',24),('7, 2',14)],
   'deux_lignes: int = 2 * largeur\ndeux_colonnes: int = 2 * (longueur - 2)\nreturn deux_lignes + deux_colonnes',
   method='Faites un calcul direct avec des variables intermédiaires, sans boucle.')

ex(1,'taille_archive','Les octets oubliés par l’appareil photo','nombre: int, largeur: int, hauteur: int','int',
   'Retournez la taille en octets d’une archive de photographies non compressées.','nombre >= 0 and largeur > 0 and hauteur > 0',
   'Un appareil de laboratoire regroupe ses photos dans une archive. Son logiciel de prévision ne compte actuellement que les pixels, ce qui sous-estime l’espace à réserver. Le format impose aussi un en-tête global et une petite fiche descriptive avant chaque photographie, même si toutes ont les mêmes dimensions.',
   'Chaque pixel occupe exactement 3 octets. Chaque photo possède en plus une fiche de 16 octets. L’archive possède toujours un en-tête de 128 octets, y compris lorsqu’elle contient zéro photo. `largeur` et `hauteur` sont des nombres de pixels. Corrigez le code pour retourner la taille totale, sans convertir en kilo-octets.',
   ['Chaque photo demande 2×3×3 + 16 = 34 octets. Deux photos et l’en-tête occupent 196 octets.', 'Sans photo, seul l’en-tête global de 128 octets est écrit.'],
   [('2, 2, 3',196),('0, 10, 10',128),('1, 1, 1',147),('3, 4, 5',356),('1, 10, 10',444),('5, 2, 2',268)],
   'image: int = largeur * hauteur * 3\nfiche_image: int = image + 16\nreturn 128 + nombre * fiche_image',kind='debug',
   starter='image: int = largeur * hauteur * 3\nreturn nombre * image')

ex(1,'budget_badges','Préparer les badges d’une rencontre','participants: int, accompagnants: int, stock: int','int',
   'Calculez le budget d’achat en centimes pour les badges et leurs attaches.','participants >= 0 and accompagnants >= 0 and 0 <= stock <= participants + accompagnants',
   'Une association prépare une rencontre. Chaque personne reçoit un badge et une attache. Il reste des badges vierges d’une rencontre précédente, mais aucune attache. Le trésorier veut connaître uniquement le montant des achats à effectuer cette fois, en tenant compte du stock déjà payé.',
   '`participants` et `accompagnants` sont les deux effectifs présents ; chaque personne compte de la même façon. `stock` est le nombre de badges réutilisables, jamais supérieur à l’effectif total. Un badge neuf coûte 35 centimes et une attache 12 centimes. Achetez une attache pour chaque personne, y compris lorsqu’elle reçoit un ancien badge. Retournez un nombre entier de centimes.',
   ['Il faut 12 attaches et seulement 8 badges neufs : 12×12 + 8×35 = 424 centimes.', 'Les cinq badges sont en stock, mais les cinq attaches coûtent encore 60 centimes.'],
   [('10, 2, 4',424),('3, 2, 5',60),('0, 0, 0',0),('1, 0, 0',47),('0, 4, 1',153),('20, 0, 10',590)],
   'personnes: int = participants + accompagnants\nneufs: int = personnes - stock\nreturn neufs * 35 + personnes * 12')

ex(2,'ouvrir_serre','Autoriser une visite de la serre','temperature: float, humidite: float, entretien: bool','bool',
   'Indiquez si une visite de la serre est autorisée.', '0 <= humidite <= 100',
   'La serre pédagogique ouvre aux visiteurs uniquement lorsque ses deux capteurs indiquent des conditions confortables. Pendant une intervention technique, les visites sont interdites quelles que soient les mesures. Le gardien souhaite que l’application rende une décision unique à partir des trois informations reçues.',
   '`temperature` est exprimée en degrés Celsius ; `humidite` est un pourcentage. La température doit être comprise entre 18 et 26 inclus et l’humidité entre 40 et 70 inclus. `entretien` vaut True lorsqu’une intervention est en cours. Retournez True seulement si les deux plages sont respectées et si aucune intervention n’a lieu.',
   ['22 °C et 55 % respectent les deux plages ; aucun entretien ne bloque la visite.', 'Les mesures sont bonnes mais l’intervention en cours interdit l’ouverture.'],
   [('22.0, 55.0, False',True),('22.0, 55.0, True',False),('18.0, 40.0, False',True),('26.0, 70.0, False',True),('17.9, 55.0, False',False),('22.0, 70.1, False',False)],
   'return 18 <= temperature <= 26 and 40 <= humidite <= 70 and not entretien')

ex(2,'demander_recharge','Une borne libre ne suffit pas','batterie: int, borne_libre: bool, mission_urgente: bool','bool',
   'Décidez si le robot doit demander la borne de recharge.','0 <= batterie <= 100',
   'Un robot partage une borne avec d’autres appareils. Il ne doit jamais demander une place déjà occupée. En temps normal, il attend que sa batterie soit faible ; avant une mission urgente, il demande une recharge préventive, même si sa batterie n’est pas encore faible.',
   '`batterie` est un pourcentage entier. Une batterie est faible lorsque ce nombre est strictement inférieur à 30. `borne_libre` indique si la borne est disponible et `mission_urgente` si une recharge préventive est souhaitée. La demande est acceptée uniquement si la borne est libre et si au moins un des deux motifs de recharge existe. À 30 %, la batterie n’est pas faible.',
   ['La batterie à 20 % suffit à motiver la demande et la borne est libre.', 'L’urgence motive une recharge, mais une borne occupée reste indisponible.'],
   [('20, True, False',True),('80, False, True',False),('30, True, False',False),('100, True, True',True),('0, False, False',False),('29, True, False',True),('80, True, False',False)],
   'motif: bool = batterie < 30 or mission_urgente\nreturn borne_libre and motif',kind='complete',
   starter='motif: bool = batterie < 30 or mission_urgente\n# Tenez également compte de la disponibilité.\nreturn False')

ex(2,'commande_partageable','Au moins deux colis identiques','articles: int, par_colis: int','bool',
   'Indiquez si une commande peut être répartie en au moins deux colis pleins et identiques.','articles >= 0 and par_colis >= 0',
   'Le service expédition souhaite séparer certaines commandes en plusieurs colis de même taille, sans reliquat. Un opérateur propose un nombre d’articles par colis. Il peut se tromper et saisir zéro : le logiciel doit refuser cette proposition proprement, sans déclencher une division par zéro.',
   '`articles` est la quantité totale et `par_colis` la capacité proposée. Une proposition est valide si la capacité est strictement positive, si tous les articles entrent dans des colis pleins et si au moins deux colis sont nécessaires. Une commande vide et une commande tenant dans un seul colis sont refusées. Retournez un booléen, sans lever d’erreur lorsque par_colis vaut zéro.',
   ['Les 12 articles forment trois colis de 4 : la répartition est valide.', 'Les 4 articles forment un seul colis ; la condition de deux colis n’est pas satisfaite.'],
   [('12, 4',True),('4, 4',False),('0, 4',False),('9, 0',False),('0, 0',False),('10, 4',False),('8, 4',True)],
   'return par_colis > 0 and articles % par_colis == 0 and articles // par_colis >= 2',
   method='Utilisez le court-circuit de `and` pour protéger le reste et la division entière.')

ex(2,'deux_capteurs_valides','L’alarme de désaccord','a: float, b: float, tolerance: float','bool',
   'Indiquez si deux mesures sont toutes deux recevables et suffisamment proches.','tolerance >= 0',
   'Deux capteurs mesurent simultanément un niveau de remplissage. Pour éviter qu’une valeur aberrante passe inaperçue, le système ne valide pas seulement leur proximité : chacun doit aussi fournir une mesure dans la plage physique autorisée. Deux capteurs en panne peuvent en effet donner la même mauvaise valeur.',
   '`a` et `b` sont des pourcentages qui doivent chacun appartenir à [0,100]. Leur différence doit être comprise entre -tolerance et +tolerance, bornes incluses. Une seule valeur hors de [0,100] invalide l’ensemble, même si l’écart est faible. Corrigez le programme qui ne contrôle actuellement que l’accord entre les mesures. Retournez True si toutes les conditions sont remplies.',
   ['L’écart vaut 2 points et les deux mesures sont physiques : la validation réussit.', 'Les capteurs s’accordent, mais 110 % est impossible : la validation doit échouer.'],
   [('48.0, 50.0, 2.0',True),('110.0, 110.0, 1.0',False),('0.0, 0.0, 0.0',True),('100.0, 100.0, 0.0',True),('10.0, 13.0, 2.0',False),('-1.0, 0.0, 5.0',False),('50.0, 48.0, 2.0',True)],
   'return 0 <= a <= 100 and 0 <= b <= 100 and -tolerance <= a - b <= tolerance',kind='debug',
   starter='return -tolerance <= a - b <= tolerance')

ex(2,'reservations_en_conflit','Deux réservations peuvent-elles coexister ?','debut1: int, fin1: int, debut2: int, fin2: int','bool',
   'Détectez si deux réservations occupent simultanément une salle.','0 <= debut1 < fin1 <= 1440 and 0 <= debut2 < fin2 <= 1440',
   'Une salle ne peut accueillir qu’un groupe à la fois. Les réservations sont enregistrées en minutes depuis minuit. Un groupe peut entrer exactement quand le précédent sort : le logiciel doit donc distinguer un véritable chevauchement d’un simple contact entre deux horaires.',
   'Chaque réservation occupe l’intervalle allant de son début inclus à sa fin exclue. Retournez True s’il existe une durée strictement positive pendant laquelle les deux groupes seraient présents. Les paramètres ne sont pas nécessairement fournis dans l’ordre chronologique. Une réservation entièrement contenue dans l’autre constitue un conflit ; deux réservations consécutives n’en constituent pas.',
   ['Les deux groupes seraient présents de la minute 90 à la minute 120.', 'Le premier groupe sort à 120, exactement quand le second entre : aucun conflit.'],
   [('60, 120, 90, 150',True),('60, 120, 120, 180',False),('120, 180, 60, 120',False),('0, 1440, 10, 20',True),('30, 40, 30, 40',True),('0, 10, 20, 30',False)],
   'return debut1 < fin2 and debut2 < fin1')

ex(3,'cout_consigne','Le prix d’un dépôt au vestiaire','volume: int, fragile: bool','int',
   'Retournez le prix d’un dépôt en euros entiers.','volume > 0',
   'Le vestiaire d’un festival classe les objets selon leur volume. Les objets fragiles nécessitent une protection supplémentaire, mais restent dans la même catégorie de taille. L’équipe souhaite une fonction unique qui applique correctement les seuils et ajoute la protection une seule fois.',
   '`volume` est un nombre entier de litres. Jusqu’à 10 litres inclus, le tarif de base vaut 2 euros ; de 11 à 30 litres inclus, il vaut 4 euros ; au-delà de 30 litres, il vaut 7 euros. Si `fragile` vaut True, ajoutez 3 euros quel que soit le volume. Retournez le total, sans afficher de texte.',
   ['Un objet de 8 litres coûte 2 euros ; la protection ajoute 3 euros, soit 5.', '30 litres appartiennent encore à la catégorie intermédiaire à 4 euros.'],
   [('8, True',5),('30, False',4),('10, False',2),('11, False',4),('31, False',7),('31, True',10),('1, False',2)],
   'prix: int = 0\nif volume <= 10:\n    prix = 2\nelif volume <= 30:\n    prix = 4\nelse:\n    prix = 7\nif fragile:\n    prix = prix + 3\nreturn prix')

ex(3,'quantite_a_expedier','Livrer ce qui est disponible','demande: int, stock: int, autoriser_partiel: bool','int',
   'Retournez le nombre d’articles à expédier immédiatement.','demande >= 0 and stock >= 0',
   'Une boutique prépare une commande avec un stock parfois insuffisant. Certains clients acceptent une livraison partielle ; d’autres veulent recevoir toute leur commande en une seule fois. La fonction doit choisir la quantité à envoyer maintenant sans dépasser ni la demande ni le stock disponible.',
   'Si le stock couvre la demande, expédiez exactement la quantité demandée, quelle que soit l’option. Si le stock est insuffisant et que `autoriser_partiel` vaut True, expédiez tout le stock. Dans le cas contraire, n’expédiez rien. Une demande nulle produit toujours zéro. Ne modifiez pas le stock : retournez seulement la quantité calculée.',
   ['Il manque trois articles, mais le client accepte de recevoir les cinq disponibles.', 'Sans autorisation de livraison partielle, les cinq articles restent en attente.'],
   [('8, 5, True',5),('8, 5, False',0),('5, 5, False',5),('3, 20, True',3),('0, 5, True',0),('5, 0, True',0),('2, 3, False',2)],
   'if stock >= demande:\n    return demande\nif autoriser_partiel:\n    return stock\nreturn 0',kind='complete',
   starter='if stock >= demande:\n    return demande\n# Traitez le stock insuffisant suivant le choix du client.\nreturn 0')

ex(3,'mode_ventilation','Donner priorité à l’alerte forte','temperature: int, co2: int','int',
   'Choisissez le mode 0, 1 ou 2 du ventilateur.','co2 >= 0',
   'Une salle possède trois modes de ventilation. Les règles de température et de qualité de l’air peuvent se déclencher en même temps. Le régulateur doit toujours retenir le mode le plus fort demandé par une des mesures, plutôt que de s’arrêter à la première alerte modérée.',
   'Le mode 2 est obligatoire si la température atteint 30 degrés ou si le CO₂ atteint 1500 ppm. Sinon, choisissez le mode 1 si la température atteint 24 degrés ou si le CO₂ atteint 1000 ppm. Si aucune condition n’est satisfaite, choisissez 0. Les valeurs seuils sont incluses et un seul dépassement suffit à activer un mode.',
   ['26 degrés déclenchent seulement le mode 1 ; le CO₂ reste bas.', 'Malgré une température modérée, les 1500 ppm imposent le mode 2.'],
   [('26, 800',1),('25, 1500',2),('23, 999',0),('24, 0',1),('0, 1000',1),('30, 0',2),('-5, 800',0)],
   'if temperature >= 30 or co2 >= 1500:\n    return 2\nelif temperature >= 24 or co2 >= 1000:\n    return 1\nreturn 0')

ex(3,'points_livraison','Un colis perdu ne marque aucun point','retard: int, perdu: bool','int',
   'Calculez le score de qualité d’une livraison.','',
   'Une coopérative évalue ses tournées avec un score simple. Le retard représente l’écart entre l’heure réelle et l’heure prévue : une valeur négative signifie une arrivée en avance. La perte d’un colis annule cependant tous les points, même si une heure de livraison a été enregistrée par erreur.',
   'Un colis perdu reçoit toujours 0 point. Pour les autres, un retard inférieur ou égal à 0 donne 100 points ; de 1 à 10 minutes incluses, 80 ; de 11 à 30 incluses, 50 ; au-delà, 0. Le programme fourni ne tient pas compte des pertes. Corrigez-le sans changer cette grille de retard ni la signature.',
   ['Six minutes de retard donnent 80 points lorsque le colis est bien arrivé.', 'Le colis est perdu : le score est nul, même avec une heure enregistrée en avance.'],
   [('6, False',80),('-3, True',0),('0, False',100),('10, False',80),('11, False',50),('30, False',50),('31, False',0),('12, True',0)],
   'if perdu:\n    return 0\nif retard <= 0:\n    return 100\nelif retard <= 10:\n    return 80\nelif retard <= 30:\n    return 50\nreturn 0',kind='debug',
   starter='if retard <= 0:\n    return 100\nelif retard <= 10:\n    return 80\nelif retard <= 30:\n    return 50\nreturn 0')

ex(3,'location_casier','Un plafond pour chaque journée','heures: int','int',
   'Retournez le prix d’une location de casier en euros.','heures >= 0',
   'La gare facture ses casiers par tranches de 24 heures à partir du début de la location. Une tranche complète coûte 12 euros. Pour la dernière tranche incomplète, la facturation est horaire mais ne peut jamais dépasser ce même forfait : il faut appliquer le plafond au bon endroit.',
   '`heures` est une durée entière déjà mesurée ; aucune heure supplémentaire ne doit être arrondie. Chaque bloc complet de 24 heures coûte 12 euros. Les heures restantes coûtent 2 euros chacune, avec un maximum de 12 euros pour ce reste. Une durée nulle coûte zéro. Retournez le total de tous les blocs et du dernier reste.',
   ['26 heures font un bloc de 24 heures à 12 euros et deux heures à 4 euros : total 16.', 'Huit heures coûteraient 16 euros à l’heure, mais le plafond ramène le prix à 12.'],
   [('26',16),('8',12),('0',0),('1',2),('6',12),('24',12),('48',24),('49',26)],
   'jours: int = heures // 24\nreste: int = heures % 24\nfin: int = reste * 2\nif fin > 12:\n    fin = 12\nreturn jours * 12 + fin',points=6)
