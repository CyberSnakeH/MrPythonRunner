from course2022_v2_core import ex

ex(4,'places_gradins','Installer des rangées de chaises','premier: int, supplement: int, rangees: int','int',
   'Retournez le nombre total de chaises à installer.','premier >= 0 and supplement >= 0 and rangees >= 0',
   'La salle d’un festival s’élargit à mesure que l’on s’éloigne de la scène. Les bénévoles installent une première rangée, puis ajoutent toujours le même nombre de chaises à chaque nouvelle rangée. Ils doivent préparer le stock total avant de commencer.',
   '`premier` est le nombre de chaises de la première rangée ; `supplement` est le nombre ajouté pour passer à la suivante. `rangees` est le nombre de rangées effectivement installées. Une installation sans rangée demande zéro chaise. Une augmentation nulle donne des rangées identiques. Simulez les rangées une à une avec une boucle while.',
   ['Les rangées contiennent 4, 6 et 8 chaises : leur total vaut 18.', 'Aucune rangée n’est installée ; le stock nécessaire est nul.'],
   [('4, 2, 3',18),('4, 2, 0',0),('5, 0, 4',20),('0, 3, 3',9),('7, 2, 1',7),('1, 1, 5',15)],
   'total: int = 0\ntaille: int = premier\ni: int = 0\nwhile i < rangees:\n    total = total + taille\n    taille = taille + supplement\n    i = i + 1\nreturn total',
   method='Indiquez dans un commentaire ce que représentent le compteur, la taille courante et le total avant chaque tour.')

ex(4,'batterie_missions','Des missions de plus en plus coûteuses','charge: int, missions: int','int',
   'Retournez la charge restante après toutes les missions.','missions >= 0 and charge >= missions * (missions + 1) // 2',
   'Un robot d’essai effectue des missions numérotées à partir de un. La première consomme une unité de batterie, la deuxième deux unités, et ainsi de suite. Le laboratoire fournit assez d’énergie pour toutes les missions prévues et veut simuler leur consommation successive.',
   '`charge` désigne la quantité initiale d’énergie et `missions` le nombre de missions à effectuer. La mission de numéro k retire exactement k unités. Complétez la boucle pour retirer chaque consommation une seule fois. Retournez l’énergie restante, pas l’énergie consommée. Avec zéro mission, toute la charge initiale reste disponible.',
   ['Les trois missions retirent 1 + 2 + 3 = 6 unités ; il en reste 14.', 'Aucune mission n’est effectuée, donc les 8 unités sont conservées.'],
   [('20, 3',14),('8, 0',8),('0, 0',0),('10, 4',0),('7, 1',6),('100, 5',85)],
   'reste: int = charge\nk: int = 1\nwhile k <= missions:\n    reste = reste - k\n    k = k + 1\nreturn reste',kind='complete',
   starter='reste: int = charge\nk: int = 1\nwhile k <= missions:\n    # Ajoutez ici la consommation de cette mission.\n    k = k + 1\nreturn reste')

ex(4,'epargne_alternee','Deux montants de versement','semaines: int, petit: int, grand: int','int',
   'Calculez le montant déposé après le nombre de semaines indiqué.','semaines >= 0 and petit >= 0 and grand >= 0',
   'Une classe finance une sortie grâce à des versements hebdomadaires. Les deux groupes d’élèves contribuent à tour de rôle : le premier verse un montant fixé, puis le second un autre montant. Le compte est vide avant la première semaine.',
   '`petit` est le versement des semaines impaires, en euros, et `grand` celui des semaines paires ; ces noms n’imposent pas un ordre entre les montants. La première semaine utilise donc `petit`. Retournez le cumul après `semaines` versements, en utilisant une boucle while. Zéro semaine signifie qu’aucun versement n’a encore eu lieu.',
   ['Les versements sont 2, 5, 2, 5, 2 : le compte contient 16 euros.', 'Une seule semaine apporte uniquement le premier montant, soit 7 euros.'],
   [('5, 2, 5',16),('1, 7, 3',7),('0, 4, 8',0),('4, 0, 3',6),('3, 5, 5',15),('2, 9, 1',10)],
   'total: int = 0\ns: int = 1\nwhile s <= semaines:\n    if s % 2 == 1:\n        total = total + petit\n    else:\n        total = total + grand\n    s = s + 1\nreturn total')

ex(4,'position_balancier','Le robot change de direction','mouvements: int','int',
   'Retournez la position finale du robot sur son axe.','mouvements >= 0',
   'Un robot de démonstration part de l’origine d’un axe gradué. Pour tester son moteur, il avance d’une unité, recule de deux, avance de trois, puis recule de quatre. Le programme fourni oublie les changements de direction et doit être corrigé.',
   'Les mouvements sont numérotés de 1 à `mouvements`. Un numéro impair ajoute ce numéro à la position ; un numéro pair le soustrait. Les positions négatives sont autorisées. Retournez la position signée et non la distance parcourue. Sans mouvement, le robot reste à zéro. Conservez une simulation avec une boucle while.',
   ['Les positions successives sont 1, −1, 2 et −2 ; le résultat est −2.', 'Les trois déplacements donnent 1 − 2 + 3 = 2.'],
   [('4',-2),('3',2),('0',0),('1',1),('2',-1),('9',5)],
   'position: int = 0\nk: int = 1\nwhile k <= mouvements:\n    if k % 2 == 1:\n        position = position + k\n    else:\n        position = position - k\n    k = k + 1\nreturn position',kind='debug',
   starter='position: int = 0\nk: int = 1\nwhile k <= mouvements:\n    position = position + k\n    k = k + 1\nreturn position')

ex(4,'stock_apres_tri','Retirer les pièces à contrôler','stock: int, jours: int','int',
   'Retournez le stock restant après les opérations de tri.','stock >= 0 and jours >= 0',
   'Un atelier conserve un lot de pièces dans une réserve. Chaque matin, il prélève pour contrôle un tiers entier des pièces actuellement présentes. Les pièces prélevées ne reviennent pas dans la réserve et aucun nouvel arrivage n’a lieu pendant la période étudiée.',
   'À chaque journée, retirez `stock_courant // 3` pièces du stock courant. Le calcul doit être refait après chaque prélèvement : il ne porte pas toujours sur le stock initial. `jours` peut être nul. Un stock inférieur à trois reste inchangé puisque son tiers entier vaut zéro. Retournez le nombre de pièces encore présentes.',
   ['On retire 3 pièces sur 10, puis 2 sur 7 : il reste 5 pièces.', 'Avec deux pièces, chaque prélèvement vaut zéro ; le stock reste égal à 2.'],
   [('10, 2',5),('2, 8',2),('0, 5',0),('12, 0',12),('9, 1',6),('27, 3',8)],
   'reste: int = stock\nj: int = 0\nwhile j < jours:\n    reste = reste - reste // 3\n    j = j + 1\nreturn reste')

ex(5,'jours_collecte','Atteindre le financement de la sortie','initial: int, objectif: int, premier_gain: int','int',
   'Retournez le premier nombre de jours permettant d’atteindre l’objectif.','initial >= 0 and objectif >= 0 and premier_gain > 0',
   'Une collecte dispose déjà d’une somme de départ. La campagne attire progressivement davantage de personnes : elle rapporte un montant connu le premier jour, puis un euro de plus à chaque nouveau jour. L’organisateur veut annoncer quand le financement sera suffisant.',
   '`initial` et `objectif` sont des sommes en euros ; `premier_gain` est le gain du jour 1. Le jour suivant rapporte un euro supplémentaire par rapport au précédent. Arrêtez-vous dès que la somme cumulée est supérieure ou égale à l’objectif. Si la somme initiale suffit déjà, retournez zéro. Ne poursuivez pas jusqu’à une égalité exacte.',
   ['Les gains 3, 4 et 5 portent le total de 10 à 13, 17 puis 22 : trois jours suffisent.', 'Les 30 euros de départ dépassent déjà l’objectif de 20 euros.'],
   [('10, 20, 3',3),('30, 20, 2',0),('0, 1, 1',1),('0, 6, 1',3),('2, 2, 5',0),('1, 12, 4',3)],
   'somme: int = initial\ngain: int = premier_gain\njours: int = 0\nwhile somme < objectif:\n    somme = somme + gain\n    gain = gain + 1\n    jours = jours + 1\nreturn jours')

ex(5,'pliages_format','Faire entrer une bande dans son étui','longueur: int, limite: int','int',
   'Retournez le nombre minimal de pliages nécessaires.','longueur >= 1 and limite >= 1',
   'Une machine plie une bande de carton pour la faire entrer dans un étui. Les longueurs sont mesurées en unités entières. Lorsqu’une longueur est impaire, la moitié la plus longue détermine l’encombrement final : il faut donc arrondir la moitié vers le haut.',
   '`longueur` est l’encombrement initial et `limite` l’encombrement maximal accepté par l’étui. Un pliage remplace une longueur L par `(L + 1) // 2`. Comptez les pliages jusqu’à obtenir une longueur inférieure ou égale à la limite. Si elle est déjà acceptable, retournez zéro. Complétez le comptage sans changer la règle d’arrondi.',
   ['La longueur passe de 9 à 5, puis à 3 : deux pliages suffisent.', 'Une bande de longueur 4 entre déjà dans l’étui de limite 4.'],
   [('9, 3',2),('4, 4',0),('1, 1',0),('3, 1',2),('8, 1',3),('17, 2',4)],
   'reste: int = longueur\ncompte: int = 0\nwhile reste > limite:\n    reste = (reste + 1) // 2\n    compte = compte + 1\nreturn compte',kind='complete',
   starter='reste: int = longueur\ncompte: int = 0\nwhile reste > limite:\n    reste = (reste + 1) // 2\n    # Mémorisez le pliage effectué.\nreturn compte')

ex(5,'dechets_retires','Mesurer ce que le filtre a capturé','pollution: int, seuil: int','int',
   'Retournez la quantité totale de déchets retirés.','pollution >= 0 and seuil >= 0',
   'Un dispositif filtre un liquide en plusieurs passages. Après chaque passage, il ne reste que la moitié entière des particules présentes auparavant. Le technicien arrête le dispositif lorsque la quantité restante respecte le seuil, puis pèse tous les déchets capturés.',
   '`pollution` est le nombre initial de particules et `seuil` le maximum autorisé après traitement. Chaque passage remplace le nombre courant par sa division entière par deux. Retournez le nombre de particules retirées au total, et non le nombre de passages ni le reste. Si le liquide respecte déjà le seuil, aucun déchet n’est retiré.',
   ['Les restes sont 5 puis 2 ; sur 11 particules initiales, 9 ont été retirées.', 'Le seuil de 5 accepte déjà les 4 particules : aucun filtrage n’a lieu.'],
   [('11, 3',9),('4, 5',0),('0, 0',0),('1, 0',1),('8, 2',6),('7, 7',0)],
   'reste: int = pollution\nwhile reste > seuil:\n    reste = reste // 2\nreturn pollution - reste')

ex(5,'jours_reserve','Financer des journées complètes','stock: int, cout_initial: int','int',
   'Retournez le nombre de journées que la réserve peut financer entièrement.','stock >= 0 and cout_initial > 0',
   'Un chantier utilise une réserve de crédits pour ses frais quotidiens. Le premier jour a un coût connu ; chaque jour suivant coûte un crédit de plus. Une journée ne commence que si la réserve permet de payer son coût entier, sans emprunt.',
   '`stock` est le nombre initial de crédits disponibles. Les coûts successifs sont `cout_initial`, puis ce montant augmenté de un, de deux, et ainsi de suite. Il est permis de vider exactement la réserve. Dès que la prochaine journée coûte plus que le reste, arrêtez le comptage. Le programme fourni compte à tort une journée non finançable.',
   ['Les coûts 3 puis 4 laissent 3 crédits ; les 5 crédits du troisième jour manquent.', 'Les 3 crédits paient exactement une journée, puis la réserve est vide.'],
   [('10, 3',2),('3, 3',1),('0, 1',0),('2, 3',0),('15, 1',5),('7, 3',2)],
   'reste: int = stock\ncout: int = cout_initial\njours: int = 0\nwhile reste >= cout:\n    reste = reste - cout\n    cout = cout + 1\n    jours = jours + 1\nreturn jours',kind='debug',
   starter='reste: int = stock\ncout: int = cout_initial\njours: int = 0\nwhile reste > 0:\n    reste = reste - cout\n    cout = cout + 1\n    jours = jours + 1\nreturn jours')

ex(5,'ascension_sonde','Atteindre la sortie du puits','hauteur: int, montee: int, glissade: int','int',
   'Retournez le nombre de journées nécessaires pour sortir du puits.','hauteur >= 0 and montee > glissade >= 0',
   'Une sonde remonte un conduit vertical. Pendant la journée elle gagne une hauteur fixe ; la nuit elle glisse légèrement. Dès qu’elle atteint la sortie pendant une journée, elle est récupérée : elle ne subit donc pas la glissade de cette dernière nuit.',
   'La sonde part de la hauteur zéro. `hauteur` est la hauteur de sortie ; `montee` le gain diurne et `glissade` la perte nocturne, dans la même unité. Comptez une journée pour chaque montée effectuée. Testez la sortie avant de soustraire la glissade. Une sortie de hauteur zéro est déjà atteinte et demande zéro journée.',
   ['Les fins de nuit sont à 1 puis 2 ; la troisième montée atteint 5 et permet la sortie.', 'La première montée de 3 dépasse la sortie située à 2 : une journée suffit.'],
   [('5, 3, 2',3),('2, 3, 2',1),('0, 3, 2',0),('10, 4, 1',3),('6, 2, 0',3),('3, 3, 2',1)],
   'position: int = 0\njours: int = 0\nwhile position < hauteur:\n    position = position + montee\n    jours = jours + 1\n    if position < hauteur:\n        position = position - glissade\nreturn jours',points=6)

ex(6,'formules_visite','Comparer les compositions d’un groupe','adultes_max: int, enfants_max: int, budget: int','int',
   'Comptez les compositions de groupe admissibles.','adultes_max >= 0 and enfants_max >= 0 and budget >= 0',
   'Un musée cherche les différentes compositions possibles pour une visite familiale. Il ne distingue pas les personnes individuellement : un groupe est défini uniquement par son nombre d’adultes et son nombre d’enfants. Chaque composition doit respecter le budget disponible pour les billets.',
   'Un adulte paie 3 euros et un enfant 2 euros. Comptez les couples d’effectifs contenant au moins un adulte et un enfant, sans dépasser `adultes_max`, `enfants_max` et `budget`. Les bornes maximales sont incluses. Deux groupes ayant les mêmes effectifs ne comptent qu’une fois. Si un effectif maximal vaut zéro, aucune composition n’est possible.',
   ['Avec un budget de 8, les effectifs possibles sont (1,1), (1,2) et (2,1).', 'Même le groupe minimal coûte 5 euros : un budget de 4 ne suffit pas.'],
   [('2, 2, 8',3),('3, 3, 4',0),('0, 4, 20',0),('1, 1, 5',1),('2, 2, 10',4),('1, 3, 7',2)],
   'total: int = 0\na: int = 1\nwhile a <= adultes_max:\n    e: int = 1\n    while e <= enfants_max:\n        if 3 * a + 2 * e <= budget:\n            total = total + 1\n        e = e + 1\n    a = a + 1\nreturn total',method='Utilisez deux boucles while imbriquées ; réinitialisez le compteur intérieur pour chaque adulte possible.',points=6)

ex(6,'cases_balisees','Installer les balises d’une grille','largeur: int, hauteur: int','int',
   'Comptez les cases qui reçoivent une balise.','largeur >= 0 and hauteur >= 0',
   'Une équipe quadrille une zone rectangulaire pour un exercice d’orientation. Les cases sont repérées par deux coordonnées entières commençant à zéro. Pour répartir régulièrement les balises, elle choisit uniquement les cases dont la somme des coordonnées est un multiple de trois.',
   '`largeur` donne le nombre de colonnes et `hauteur` le nombre de lignes. Les coordonnées x vont de zéro à largeur moins un ; les coordonnées y de zéro à hauteur moins un. La case (0,0) reçoit une balise lorsqu’elle existe. Une dimension nulle définit une grille vide. Complétez le test dans les deux boucles fournies.',
   ['Dans une grille 3 par 2, les cases (0,0) et (2,1) sont retenues.', 'Sans colonne, aucune case n’existe, même avec quatre lignes.'],
   [('3, 2',2),('0, 4',0),('1, 1',1),('2, 2',1),('3, 3',3),('4, 4',6)],
   'total: int = 0\nx: int = 0\nwhile x < largeur:\n    y: int = 0\n    while y < hauteur:\n        if (x + y) % 3 == 0:\n            total = total + 1\n        y = y + 1\n    x = x + 1\nreturn total',kind='complete',
   starter='total: int = 0\nx: int = 0\nwhile x < largeur:\n    y: int = 0\n    while y < hauteur:\n        # Décidez si cette case reçoit une balise.\n        y = y + 1\n    x = x + 1\nreturn total',points=6)

ex(6,'passages_communs','Deux navettes au même arrêt','periode_a: int, periode_b: int, fin: int','int',
   'Comptez les instants où les deux navettes passent ensemble.','periode_a > 0 and periode_b > 0 and fin >= 0',
   'Deux navettes partent ensemble à l’ouverture d’un parc puis repassent à intervalles réguliers. Le responsable veut prévoir les encombrements sur une période donnée. Le départ initial n’est pas compté, car les visiteurs ne sont pas encore admis à cet instant.',
   'Les périodes sont exprimées en minutes entières. La navette A passe aux multiples positifs de `periode_a`, et B aux multiples positifs de `periode_b`. Comptez les minutes communes entre 1 et `fin`, borne finale incluse. Une durée nulle donne zéro passage commun. Parcourez les minutes et vérifiez les deux conditions de passage.',
   ['Les passages communs ont lieu aux minutes 6 et 12 : il y en a deux.', 'La première rencontre serait à la minute 6, après la fin fixée à 5.'],
   [('2, 3, 12',2),('2, 3, 5',0),('1, 1, 0',0),('4, 4, 12',3),('1, 3, 10',3),('5, 7, 35',1)],
   'minute: int = 1\ncompte: int = 0\nwhile minute <= fin:\n    if minute % periode_a == 0 and minute % periode_b == 0:\n        compte = compte + 1\n    minute = minute + 1\nreturn compte')

ex(6,'charge_tournees','Alterner les zones à contrôler','jours: int, zones: int','int',
   'Retournez le nombre total de minutes de contrôle.','jours >= 0 and zones >= 0',
   'Une équipe inspecte plusieurs zones pendant une campagne de contrôle. La zone numéro z demande z minutes. Pour répartir la charge, une zone n’est inspectée que les jours où la somme de son numéro et du numéro du jour est paire.',
   'Les jours vont de 1 à `jours` et les zones de 1 à `zones`, bornes incluses. Pour chaque couple jour-zone dont la somme est paire, ajoutez le numéro de la zone au total. Comptez du temps, pas seulement des inspections. Aucune zone ou aucune journée donne zéro. Corrigez le compteur de zone qui n’est pas réinitialisé dans le programme.',
   ['Le jour 1 coûte 1 + 3 = 4 minutes et le jour 2 coûte 2 minutes : total 6.', 'Le seul jour inspecte la zone 1 pour une minute.'],
   [('2, 3',6),('1, 1',1),('0, 4',0),('4, 0',0),('3, 3',10),('2, 2',3)],
   'total: int = 0\nj: int = 1\nwhile j <= jours:\n    z: int = 1\n    while z <= zones:\n        if (j + z) % 2 == 0:\n            total = total + z\n        z = z + 1\n    j = j + 1\nreturn total',kind='debug',
   starter='total: int = 0\nj: int = 1\nz: int = 1\nwhile j <= jours:\n    while z <= zones:\n        if (j + z) % 2 == 0:\n            total = total + z\n        z = z + 1\n    j = j + 1\nreturn total',points=6)

ex(6,'assemblages_boites','Préparer une commande sans boîte incomplète','articles: int','int',
   'Comptez les répartitions exactes en boîtes de deux et de cinq articles.','articles >= 0',
   'Un fabricant dispose de deux formats de boîtes, contenant respectivement deux et cinq articles. Il souhaite connaître le nombre de façons de préparer une commande sans article restant et sans boîte incomplète. L’ordre des boîtes dans le carton n’a aucune importance.',
   'Une répartition est définie par un nombre de boîtes de deux et un nombre de boîtes de cinq, tous deux éventuellement nuls. Comptez chaque couple une seule fois. Pour zéro article, le couple sans aucune boîte est une répartition valable : le résultat vaut un. Parcourez les nombres de boîtes possibles avec deux boucles while imbriquées.',
   ['Dix articles permettent cinq boîtes de deux ou deux boîtes de cinq : deux répartitions.', 'Une commande vide possède exactement la répartition sans boîte.'],
   [('10',2),('0',1),('1',0),('2',1),('7',1),('20',3),('11',1)],
   'total: int = 0\na: int = 0\nwhile 2 * a <= articles:\n    b: int = 0\n    while 2 * a + 5 * b <= articles:\n        if 2 * a + 5 * b == articles:\n            total = total + 1\n        b = b + 1\n    a = a + 1\nreturn total',points=6)
