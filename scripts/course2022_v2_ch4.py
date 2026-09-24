from course2022_v2_core import ex

ex(7,'reste_distribution','Distribuer des lots équitables','objets: int, equipes: int','int',
   'Retournez le nombre d’objets qui ne peuvent plus être distribués équitablement.','objets >= 0 and equipes > 0',
   'Un animateur distribue des objets à plusieurs équipes. Il procède par tournées complètes, en donnant exactement un objet à chaque équipe. Dès qu’il ne peut plus terminer une tournée, il conserve tous les objets restants pour une prochaine activité.',
   '`objets` est le stock initial et `equipes` le nombre d’équipes. Une tournée retire exactement autant d’objets qu’il y a d’équipes. Il est interdit de commencer une tournée incomplète. Retournez le stock restant, qui peut être nul. Programmez les soustractions successives sans utiliser `%` ni `//`, puis justifiez pourquoi toutes les équipes reçoivent autant d’objets.',
   ['Trois tournées distribuent 12 objets ; il en reste 2 sur les 14 disponibles.', 'Les 3 objets ne permettent aucune tournée auprès de 5 équipes.'],
   [('14, 4',2),('3, 5',3),('0, 3',0),('12, 4',0),('8, 1',0),('23, 6',5)],
   'reste: int = objets\nwhile reste >= equipes:\n    reste = reste - equipes\nreturn reste',
   method=r'Expliquez l’invariant $objets = reste + t \times equipes$, où $t$ est le nombre de tournées terminées. Justifiez que `reste` est un entier naturel qui diminue strictement à chaque tour, puis utilisez la condition d’arrêt pour encadrer le résultat.',
   notes='Après t tours, objets = reste + t*equipes ; reste reste naturel et décroît d’un entier strictement positif. À la sortie : 0 <= reste < equipes.',points=6)

ex(7,'pieces_caisse','Appliquer la règle de rendu de monnaie','montant: int','int',
   'Retournez le nombre de pièces distribuées par la règle imposée.','montant >= 0',
   'Une caisse pédagogique ne possède que des pièces de cinq, deux et une unités. Son mécanisme applique une règle précise : tant que possible, il choisit une pièce de cinq ; ensuite des pièces de deux ; enfin une pièce de une si nécessaire.',
   '`montant` est la somme entière à rendre. Comptez une pièce à chaque retrait, quel que soit son montant. Le stock de chaque pièce est illimité. Respectez l’ordre cinq, deux, un et retournez le nombre de pièces effectivement sorties. Un montant nul ne demande aucune pièce. Complétez les retraits dans une boucle qui conserve une somme restante non négative.',
   ['Douze unités sont rendues avec 5, 5 et 2 : trois pièces.', 'Huit unités sont rendues avec 5, 2 et 1 : trois pièces également.'],
   [('12',3),('8',3),('0',0),('1',1),('4',2),('10',2),('19',5)],
   'reste: int = montant\ncompte: int = 0\nwhile reste > 0:\n    if reste >= 5:\n        reste = reste - 5\n    elif reste >= 2:\n        reste = reste - 2\n    else:\n        reste = reste - 1\n    compte = compte + 1\nreturn compte',kind='complete',
   starter='reste: int = montant\ncompte: int = 0\nwhile reste > 0:\n    # Remplacez ce retrait par le choix de la pièce autorisée.\n    reste = reste - 1\n    compte = compte + 1\nreturn compte',
   method='Exprimez une relation entre le montant initial, le reste et la valeur déjà rendue. Le compteur de pièces seul ne donne pas la valeur rendue. Justifiez que chaque branche fait progresser la boucle.',points=6)

ex(7,'stock_controle','Une demande limitée par le stock','initial: int, arrivage: int, demande: int, tours: int','int',
   'Retournez le stock après tous les cycles d’approvisionnement et de vente.','initial >= 0 and arrivage >= 0 and demande >= 0 and tours >= 0',
   'Une petite boutique reçoit un arrivage régulier avant l’ouverture. Elle satisfait ensuite une demande fixe, mais ne vend jamais un article absent du stock. Les demandes non satisfaites sont abandonnées et ne sont pas reportées au jour suivant.',
   '`initial` est le stock avant le premier cycle. À chaque cycle, ajoutez `arrivage`, puis retirez `demande` si le stock suffit ; sinon, vendez tout ce qui reste et fixez le stock à zéro. Répétez exactement `tours` fois. Un nombre de cycles nul laisse le stock initial inchangé. Retournez le stock final, pas les ventes cumulées.',
   ['Les stocks après vente sont 1, puis 0 : la seconde demande ne peut être satisfaite entièrement.', 'Chaque cycle ajoute trois articles nets ; après deux cycles, le stock passe de 10 à 16.'],
   [('3, 2, 4, 2',0),('10, 5, 2, 2',16),('7, 1, 9, 0',7),('0, 0, 0, 4',0),('0, 3, 3, 2',0),('5, 0, 2, 2',1)],
   'stock: int = initial\nt: int = 0\nwhile t < tours:\n    stock = stock + arrivage\n    if stock >= demande:\n        stock = stock - demande\n    else:\n        stock = 0\n    t = t + 1\nreturn stock',
   method='Justifiez l’invariant `stock >= 0`. Proposez ensuite un variant lié au nombre de cycles restant à effectuer, même lorsque le stock ne change plus.',points=6)

ex(7,'distance_freinage','Ne pas oublier la dernière seconde','vitesse: int','int',
   'Retournez la distance parcourue jusqu’à l’arrêt dans ce modèle discret.','vitesse >= 0',
   'Un simulateur de freinage raisonne par secondes entières. Pendant une seconde, le véhicule avance de sa vitesse courante en mètres ; ensuite seulement, sa vitesse diminue de deux unités. La vitesse ne devient jamais négative. Le programme actuel oublie parfois le dernier déplacement.',
   '`vitesse` est la vitesse entière initiale. Tant qu’elle est positive, ajoutez sa valeur à la distance, puis diminuez-la de deux, en la ramenant à zéro si nécessaire. Le véhicule déjà immobile parcourt zéro mètre. Corrigez le code en traitant aussi les vitesses impaires, pour lesquelles une dernière seconde à vitesse un doit être comptée.',
   ['Les vitesses utilisées sont 5, 3 et 1 : la distance totale vaut 9.', 'Avec une vitesse initiale de 4, les déplacements valent 4 puis 2, soit 6 mètres.'],
   [('5',9),('4',6),('0',0),('1',1),('2',2),('7',16)],
   'v: int = vitesse\ndistance: int = 0\nwhile v > 0:\n    distance = distance + v\n    if v >= 2:\n        v = v - 2\n    else:\n        v = 0\nreturn distance',kind='debug',
   starter='v: int = vitesse\ndistance: int = 0\nwhile v > 1:\n    distance = distance + v\n    v = v - 2\nreturn distance',
   method='Indiquez ce que contient `distance` avant chaque tour. Montrez que la vitesse courante constitue un variant naturel, y compris lors du dernier tour.',points=6)

ex(7,'eau_debordee','Comptabiliser les pertes de la cuve','initial: int, apport: int, capacite: int, tours: int','int',
   'Retournez le volume cumulé qui a débordé de la cuve.','0 <= initial <= capacite and apport >= 0 and tours >= 0',
   'Une cuve reçoit régulièrement de l’eau de pluie. Elle possède une capacité fixe et ne se vide pas pendant l’observation. À chaque apport, seule la quantité qui tient encore dans la cuve est conservée ; le surplus part dans un bac de récupération.',
   'Tous les volumes sont des litres entiers. `initial` est le volume de départ, `apport` le volume reçu à chaque tour et `capacite` le volume maximal conservé. Simulez exactement `tours` apports et additionnez les débordements successifs. Retournez le volume du bac, pas celui de la cuve. Une capacité nulle est possible ; tout apport déborde alors.',
   ['La cuve passe de 3 à 7 puis à 10 ; seul un litre du second apport déborde.', 'Une cuve pleine perd les deux apports de 3 litres : le bac reçoit 6 litres.'],
   [('3, 4, 10, 2',1),('10, 3, 10, 2',6),('0, 4, 0, 3',12),('5, 8, 10, 0',0),('0, 5, 10, 2',0),('2, 0, 3, 8',0)],
   'stock: int = initial\npertes: int = 0\nt: int = 0\nwhile t < tours:\n    stock = stock + apport\n    if stock > capacite:\n        pertes = pertes + stock - capacite\n        stock = capacite\n    t = t + 1\nreturn pertes',
   method=r'Écrivez et expliquez l’invariant $initial + t \times apport = stock + pertes$, complété par $0 \leq stock \leq capacite$. Donnez un variant de boucle. La relation de conservation doit rester vraie après un débordement.',
   notes='Invariant : initial + t*apport = stock + pertes et 0 <= stock <= capacite. Variant tours-t. Le débordement change la répartition entre stock et pertes, jamais leur somme.',points=6)

ex(8,'prochaine_place','Trouver un numéro disponible','depart: int','int',
   'Retournez le premier numéro admissible supérieur ou égal au départ.','depart >= 1',
   'Un parking réserve les emplacements dont le numéro est multiple de trois aux véhicules techniques et ceux dont le numéro est multiple de cinq aux livraisons. Un visiteur ordinaire cherche le premier emplacement qu’il a le droit d’utiliser à partir d’un numéro donné.',
   '`depart` est un entier positif et peut lui-même convenir. Un emplacement est admissible seulement si son numéro n’est divisible ni par trois ni par cinq. Examinez les numéros croissants et arrêtez la recherche dès le premier numéro convenable. Retournez ce numéro, pas le nombre d’emplacements examinés. Le parking est supposé prolonger indéfiniment sa numérotation.',
   ['Les numéros 9 et 10 sont réservés ; 11 est le premier numéro admissible.', 'Le numéro 7 est déjà autorisé : aucune avancée n’est nécessaire.'],
   [('9',11),('7',7),('1',1),('15',16),('3',4),('5',7),('29',29)],
   'numero: int = depart\nwhile numero % 3 == 0 or numero % 5 == 0:\n    numero = numero + 1\nreturn numero',
   method='Expliquez pourquoi tous les numéros sautés sont interdits. Pour justifier l’existence d’un résultat, vous pouvez observer les numéros de la forme 15k+1.',points=6)

ex(8,'premier_creneau','Planifier hors d’une interruption','depart: int, periode: int, pause_debut: int, pause_fin: int','int',
   'Retournez la première minute de départ utilisable.','depart >= 0 and periode > 0 and 0 <= pause_debut <= pause_fin',
   'Une machine peut démarrer un nouveau cycle uniquement à des minutes multiples d’une période. Une intervention bloque temporairement les démarrages. Le responsable souhaite connaître le premier départ possible après la disponibilité de la commande, sans parcourir toutes les minutes intermédiaires.',
   'Le résultat doit être supérieur ou égal à `depart` et multiple de `periode`. Les minutes de `pause_debut` inclus à `pause_fin` exclu sont interdites. Une pause vide ne bloque rien. Complétez le programme en avançant directement d’un créneau au suivant pendant la pause. Un départ exactement à la fin de la pause est autorisé.',
   ['Le premier multiple de 5 après 7 est 10, mais il est bloqué ; 15 est autorisé.', 'La minute 12 est à la fin de la pause et constitue déjà un créneau.'],
   [('7, 5, 9, 14',15),('12, 3, 6, 12',12),('0, 4, 1, 9',0),('2, 2, 2, 2',2),('1, 4, 0, 13',16),('20, 3, 0, 10',21)],
   't: int = ((depart + periode - 1) // periode) * periode\nwhile pause_debut <= t and t < pause_fin:\n    t = t + periode\nreturn t',kind='complete',
   starter='t: int = ((depart + periode - 1) // periode) * periode\n# Avancez si ce premier créneau appartient à la pause.\nreturn t',
   method='Justifiez que le premier calcul donne le plus petit multiple admissible avant prise en compte de la pause. Dans la boucle, `pause_fin - t` diminue tant que le créneau reste bloqué.',points=6)

ex(8,'energie_veille','Regrouper les cycles identiques','duree: int, cycle: int','int',
   'Calculez l’énergie totale consommée pendant la durée demandée.','duree >= 0 and cycle >= 1',
   'Un capteur alterne une minute de réveil et plusieurs minutes de veille. Le même cycle recommence tant que l’appareil reste allumé. Pour prévoir de très longues durées, le technicien veut remplacer une simulation minute par minute par un calcul regroupant les cycles complets.',
   'Chaque cycle dure `cycle` minutes : sa première minute consomme 8 unités d’énergie, chacune des autres 2 unités. L’observation commence au début d’un cycle et dure exactement `duree` minutes. Calculez séparément les cycles complets et le cycle final éventuellement incomplet. Zéro minute ne consomme rien. Un cycle de durée un ne contient que des minutes de réveil.',
   ['Sept minutes avec des cycles de trois coûtent 12 + 12 + 8 = 32 unités.', 'Deux minutes du premier cycle coûtent 8 + 2 = 10 unités.'],
   [('7, 3',32),('2, 5',10),('0, 3',0),('4, 1',32),('6, 3',24),('1, 1',8),('1000000, 10',2600000)],
   'complets: int = duree // cycle\nreste: int = duree % cycle\ntotal: int = complets * (8 + 2 * (cycle - 1))\nif reste > 0:\n    total = total + 8 + 2 * (reste - 1)\nreturn total',
   method='N’utilisez aucune boucle. Expliquez pourquoi une fin vide ne doit pas ajouter les 8 unités d’un réveil. Comparez le nombre d’opérations avec une simulation de chaque minute.',points=6)

ex(8,'controles_avant_alerte','Interrompre le contrôle au bon moment','nombre: int, alerte: int','int',
   'Retournez le nombre de postes contrôlés avant l’arrêt de la tournée.','nombre >= 0 and 0 <= alerte <= nombre',
   'Un agent contrôle des postes dans l’ordre de leur numérotation. Une alerte impose d’arrêter immédiatement la tournée, après avoir contrôlé le poste concerné. Le journal de test indique à l’avance le numéro de ce poste, ou zéro si aucune alerte ne sera rencontrée.',
   'Les postes sont numérotés de 1 à `nombre`. `alerte` vaut zéro en l’absence d’incident ; sinon il donne le poste qui arrête la tournée. Le poste déclencheur compte parmi les contrôles effectués. Corrigez le code pour sortir dès sa rencontre. S’il n’y a aucun poste, le résultat vaut zéro ; sans alerte, tous les postes sont contrôlés.',
   ['Le contrôle s’arrête au poste 3, donc seuls trois postes sont examinés sur les huit.', 'Avec zéro comme indicateur d’alerte, les huit postes sont tous contrôlés.'],
   [('8, 3',3),('8, 0',8),('0, 0',0),('5, 1',1),('5, 5',5),('1, 1',1)],
   'poste: int = 1\ncompte: int = 0\nwhile poste <= nombre:\n    compte = compte + 1\n    if poste == alerte:\n        return compte\n    poste = poste + 1\nreturn compte',kind='debug',
   starter='poste: int = 1\ncompte: int = 0\nwhile poste <= nombre:\n    compte = compte + 1\n    poste = poste + 1\nreturn compte',
   method='Conservez une boucle pour travailler la sortie anticipée. Expliquez pourquoi le retour doit se placer après le comptage du poste courant. Le respect de cette méthode est vérifié par lecture du code.')

ex(8,'taille_apres_reductions','Arrêter quand le bloc est indivisible','taille: int, maximum: int','int',
   'Retournez la taille obtenue après les réductions utiles.','taille >= 0 and maximum >= 0',
   'Un outil réduit un bloc de données en ne conservant que sa moitié supérieure arrondie. Un utilisateur fixe un nombre maximal de réductions, mais poursuivre après avoir atteint zéro ou un élément serait inutile : la taille ne changerait plus.',
   'Une réduction remplace une taille T par `(T + 1) // 2`. Effectuez au plus `maximum` réductions et arrêtez-vous aussi dès que la taille est inférieure ou égale à un. Retournez la taille finale, pas le nombre d’étapes. Une limite de zéro réduction laisse le bloc inchangé. La taille nulle doit rester nulle.',
   ['Deux réductions transforment 13 en 7 puis en 4.', 'Le bloc d’un élément reste identique ; les nombreuses réductions demandées sont inutiles.'],
   [('13, 2',4),('1, 1000000',1),('0, 1000000',0),('9, 0',9),('3, 10',1),('8, 2',2)],
   'reste: int = taille\netape: int = 0\nwhile etape < maximum and reste > 1:\n    reste = (reste + 1) // 2\n    etape = etape + 1\nreturn reste',
   method='Expliquez les deux motifs d’arrêt. Montrez que, pour une taille supérieure à un, la nouvelle taille est strictement plus petite. Les tests de résultat ne suffisent pas à prouver l’absence d’itérations inutiles.',points=6)

ex(9,'espace_inutilise','Agrandir un espace de stockage','capacite: int, besoin: int','int',
   'Retournez l’espace libre après les agrandissements nécessaires.','capacite >= 1 and besoin >= 0',
   'Un système réserve un espace de stockage de capacité initiale connue. S’il ne suffit pas pour un fichier, il double sa capacité autant de fois que nécessaire. L’administrateur souhaite connaître l’espace qui restera inutilisé après avoir enregistré le fichier.',
   '`capacite` et `besoin` sont exprimés dans la même unité entière. Doublez la capacité seulement tant qu’elle est strictement inférieure au besoin. Une capacité déjà suffisante ne doit pas être réduite. Retournez la capacité finale moins le besoin, et non la capacité elle-même. Un besoin nul laisse toute la capacité initiale inutilisée.',
   ['La capacité passe de 3 à 6 puis à 12 ; le fichier de taille 8 laisse 4 unités libres.', 'Les 10 unités suffisent déjà pour 4 unités de données ; il en reste 6.'],
   [('3, 8',4),('10, 4',6),('1, 0',1),('4, 4',0),('2, 9',7),('5, 11',9)],
   'place: int = capacite\nwhile place < besoin:\n    place = 2 * place\nreturn place - besoin',
   method='Montrez que la capacité reste un multiple de la capacité initiale. Pour la terminaison, justifiez qu’elle augmente au moins de un tant qu’elle reste sous le besoin. Ne choisissez pas la capacité croissante comme variant décroissant.',points=6)

ex(9,'achats_croissants','Acheter des extensions successives','credits: int','int',
   'Retournez le nombre d’extensions entièrement achetées.','credits >= 0',
   'Dans un simulateur, les extensions d’une base deviennent de plus en plus coûteuses. La première coûte un crédit, la deuxième deux, la troisième quatre ; le prix double après chaque achat. On ne peut pas sauter une extension pour acheter la suivante.',
   '`credits` est le budget disponible au départ. Achetez tant que le budget restant est supérieur ou égal au prix de la prochaine extension. Soustrayez le prix payé avant de le doubler. Retournez le nombre d’achats, pas le nombre de crédits dépensés. Un budget nul ne permet aucun achat ; une égalité entre prix et budget autorise l’achat.',
   ['Les trois achats coûtent 1 + 2 + 4 = 7 crédits : trois extensions sont obtenues.', 'Avec 6 crédits, les prix 1 et 2 sont payés ; les 3 crédits restants ne paient pas 4.'],
   [('7',3),('6',2),('0',0),('1',1),('2',1),('15',4),('31',5)],
   'reste: int = credits\nprix: int = 1\ncompte: int = 0\nwhile reste >= prix:\n    reste = reste - prix\n    prix = prix * 2\n    compte = compte + 1\nreturn compte',kind='complete',
   starter='reste: int = credits\nprix: int = 1\ncompte: int = 0\nwhile reste >= prix:\n    reste = reste - prix\n    prix = prix * 2\n    # Mémorisez cet achat.\nreturn compte',
   method='Vérifiez que le reste ne devient pas négatif. Justifiez la terminaison malgré la croissance du prix, en donnant une quantité naturelle qui décroît.',points=6)

ex(9,'alertes_capteur','Auditer une séquence de mesures','nombre: int, seuil: int','int',
   'Comptez les mesures strictement supérieures au seuil.','nombre >= 0 and 0 <= seuil <= 10',
   'Pour tester un logiciel sans brancher de capteur, le laboratoire fabrique une suite de mesures déterministes. Chaque mesure est calculée à partir de son numéro. Le compteur d’alertes doit analyser exactement la quantité demandée, sans inclure une mesure supplémentaire.',
   'Les mesures portent les numéros 1 à `nombre` inclus. La mesure de numéro i vaut `(7 * i) % 11`. Elle déclenche une alerte seulement si sa valeur est strictement supérieure à `seuil` ; une égalité ne déclenche rien. Retournez le nombre d’alertes. Avec zéro mesure, aucun calcul de mesure ni aucune alerte n’est nécessaire.',
   ['Les quatre mesures sont 7, 3, 10 et 6 ; trois dépassent strictement 5.', 'Les mêmes mesures ne dépassent jamais strictement 10 : aucune alerte.'],
   [('4, 5',3),('4, 10',0),('0, 0',0),('1, 7',0),('1, 6',1),('11, 0',10)],
   'i: int = 1\ncompte: int = 0\nwhile i <= nombre:\n    if (7 * i) % 11 > seuil:\n        compte = compte + 1\n    i = i + 1\nreturn compte',
   method='Donnez un invariant liant le compteur d’alertes aux mesures déjà parcourues. Distinguez le nombre de mesures analysées et l’indice de la prochaine mesure.')

ex(9,'pic_charge','Garder la plus grande charge observée','initial: int, tours: int','int',
   'Retournez la plus grande charge observée, état initial compris.','initial >= 0 and tours >= 0',
   'Un modèle de charge modifie sa valeur à chaque pas de simulation. Lorsque la charge est paire, elle est divisée par deux ; lorsqu’elle est impaire, trois unités sont ajoutées. Le responsable veut conserver le pic atteint, même si la charge baisse ensuite.',
   'Partez de `initial` et appliquez exactement `tours` transformations. Le maximum recherché comprend la valeur initiale et toutes les valeurs obtenues après une transformation. Une charge paire utilise une division entière par deux. Avec zéro tour, retournez l’état initial. Corrigez le code qui retourne seulement la dernière charge au lieu de conserver la plus grande.',
   ['Les états sont 5, 8, 4 et 2 ; la plus grande valeur observée est 8.', 'Les états 8, 4 et 2 ne dépassent jamais la charge initiale de 8.'],
   [('5, 3',8),('8, 2',8),('7, 0',7),('0, 4',0),('1, 3',4),('9, 1',12)],
   'charge: int = initial\npic: int = initial\ni: int = 0\nwhile i < tours:\n    if charge % 2 == 0:\n        charge = charge // 2\n    else:\n        charge = charge + 3\n    if charge > pic:\n        pic = charge\n    i = i + 1\nreturn pic',kind='debug',
   starter='charge: int = initial\ni: int = 0\nwhile i < tours:\n    if charge % 2 == 0:\n        charge = charge // 2\n    else:\n        charge = charge + 3\n    i = i + 1\nreturn charge',
   method='La charge peut monter ou descendre : elle ne constitue pas un variant de cette boucle. Expliquez le rôle du compteur de tours et l’invariant décrivant le pic.',points=6)

ex(9,'rencontre_robots','Deux robots se rapprochent','gauche: int, droite: int','int',
   'Retournez le nombre de tours nécessaires pour que le robot gauche rejoigne ou dépasse l’autre.','gauche <= droite',
   'Deux robots se déplacent sur le même axe gradué. À chaque tour simultané, le robot situé initialement à gauche avance de deux unités et celui situé à droite recule de une unité. L’expérience s’arrête quand le premier rejoint ou dépasse le second.',
   '`gauche` et `droite` sont les positions initiales et peuvent être négatives. Effectuez les deux déplacements avant de compter un tour terminé. Il n’est pas nécessaire que les robots occupent exactement la même position : un dépassement suffit. S’ils sont déjà ensemble, retournez zéro. Le résultat attendu est un nombre de tours, pas une position finale.',
   ['Les positions passent de (0,7) à (2,6), puis (4,5), puis (6,4) : trois tours.', 'Les robots sont déjà au même endroit : aucun déplacement n’est demandé.'],
   [('0, 7',3),('4, 4',0),('-5, 1',2),('0, 1',1),('0, 3',1),('10, 14',2)],
   'a: int = gauche\nb: int = droite\ntours: int = 0\nwhile a < b:\n    a = a + 2\n    b = b - 1\n    tours = tours + 1\nreturn tours',
   method='Exprimez les deux positions après t tours. L’écart diminue de trois, mais peut devenir négatif : expliquez pourquoi le nombre de tours restant, obtenu en arrondissant l’écart positif divisé par trois vers le haut, justifie l’arrêt.',points=6)
