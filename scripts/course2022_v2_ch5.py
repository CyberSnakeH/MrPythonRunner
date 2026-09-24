from course2022_v2_core import ex

ex(10,'marquages_regle','Dessiner les graduations d’une règle','debut: int, fin: int, pas: int','str',
   'Construisez la ligne de graduations correspondant à l’intervalle demandé.','pas > 0',
   'Un logiciel dessine une règle graduée avec un caractère par position entière. Les grandes graduations apparaissent à intervalles réguliers ; les positions intermédiaires sont représentées par des points. La règle peut commencer avant zéro pour représenter une mesure signée.',
   'Parcourez les entiers de `debut` inclus à `fin` exclu. Pour chaque entier multiple de `pas`, ajoutez le caractère `|` ; pour les autres, ajoutez `.`. Les multiples négatifs et zéro suivent la même règle. Si debut est supérieur ou égal à fin, retournez une chaîne vide. N’ajoutez ni espace ni retour à la ligne.',
   ['Les positions 0, 3 et 6 reçoivent une barre ; les autres positions jusqu’à 6 reçoivent un point.', 'Entre −2 inclus et 3 exclu, les multiples de deux sont −2, 0 et 2.'],
   [('0, 7, 3','|..|..|'),('-2, 3, 2','|.|.|'),('3, 3, 2',''),('5, 2, 1',''),('1, 4, 5','...'),('1, 4, 1','|||')],
   'resultat: str = ""\ni: int\nfor i in range(debut, fin):\n    if i % pas == 0:\n        resultat = resultat + "|"\n    else:\n        resultat = resultat + "."\nreturn resultat',method='Utilisez `for`, `range` et la concaténation. Attention à la borne finale exclue.')

ex(10,'initiales_badge','Un badge quand un nom manque','prenom: str, nom: str','str',
   'Retournez les initiales disponibles, chacune suivie d’un point.','',
   'Un atelier imprime des badges abrégés à partir d’un prénom et d’un nom. Certains participants n’ont renseigné qu’un des deux champs. Le logiciel doit produire un badge correct dans tous les cas, sans tenter de lire le premier caractère d’une chaîne vide.',
   'Pour chaque champ non vide, prenez exactement son premier caractère et ajoutez un point. Traitez le prénom avant le nom. Un champ vide ne produit rien, pas même un point. Conservez les caractères tels quels : aucune conversion en majuscule et aucune suppression d’espace ne sont demandées. Deux champs vides produisent une chaîne vide.',
   ['Le premier caractère de chaque champ donne A. puis D., sans espace entre les deux.', 'Le prénom est absent : seule l’initiale L. du nom apparaît.'],
   [("'Alice', 'Durand'",'A.D.'),("'', 'Lee'",'L.'),("'', ''",''),("'Éva', ''",'É.'),("'bob', 'li'",'b.l.'),("'A', 'B'",'A.B.')],
   'resultat: str = ""\nif len(prenom) > 0:\n    resultat = resultat + prenom[0] + "."\nif len(nom) > 0:\n    resultat = resultat + nom[0] + "."\nreturn resultat',kind='complete',
   starter='resultat: str = ""\nif len(prenom) > 0:\n    resultat = resultat + prenom[0] + "."\n# Traitez maintenant le champ nom.\nreturn resultat')

ex(10,'masquer_reference','Afficher seulement la fin d’une référence','reference: str, visibles: int','str',
   'Retournez la référence dont seul le suffixe autorisé est visible.','visibles >= 0',
   'Une application affiche des références de réservation sur un écran public. Pour limiter les informations visibles, elle cache le début de chaque référence avec des étoiles et conserve seulement un nombre choisi de caractères à la fin. La longueur affichée doit rester identique.',
   '`visibles` est le nombre maximal de caractères conservés à droite. Remplacez chacun des caractères précédents par une étoile `*`. Si visibles vaut zéro, masquez toute la référence. Si visibles dépasse sa longueur, conservez tout le texte. Une référence vide reste vide. Les espaces éventuels comptent comme des caractères et suivent exactement la même règle.',
   ['Seuls les trois derniers caractères 245 restent visibles ; les trois premiers deviennent des étoiles.', 'La référence compte deux caractères, moins que les cinq autorisés : elle reste entière.'],
   [("'AB1245', 3",'***245'),("'XY', 5",'XY'),("'', 2",''),("'abc', 0",'***'),("'abc', 3",'abc'),("'A B', 1",'**B')],
   'resultat: str = ""\ni: int\nfor i in range(0, len(reference)):\n    if i < len(reference) - visibles:\n        resultat = resultat + "*"\n    else:\n        resultat = resultat + reference[i]\nreturn resultat',method='Parcourez les indices avec `range`. Évitez un découpage `[-visibles:]` non protégé : lorsque visibles vaut zéro, cet indice vaut aussi zéro.')

ex(10,'rotation_etiquette','Recaler le début d’une étiquette','texte: str, decalage: int','str',
   'Déplacez les premiers caractères à la fin en conservant leur ordre.','0 <= decalage <= len(texte)',
   'Une imprimante circulaire a commencé à lire une étiquette au mauvais endroit. Pour préparer une nouvelle impression, on souhaite déplacer un préfixe du texte vers la fin. Aucun caractère ne doit être perdu, dupliqué ou inversé pendant cette opération.',
   '`decalage` est le nombre de caractères à retirer du début puis à ajouter à la fin. Conservez l’ordre à l’intérieur des deux morceaux. Un décalage nul et un décalage égal à la longueur doivent rendre le texte original. Corrigez l’erreur de borne dans le découpage fourni. La chaîne vide est autorisée avec un décalage nul.',
   ['Le préfixe AB passe après CDE : le résultat est CDEAB.', 'Avec un décalage nul, aucun caractère ne change de place.'],
   [("'ABCDE', 2",'CDEAB'),("'abc', 0",'abc'),("'', 0",''),("'abc', 3",'abc'),("'abcd', 1",'bcda'),("'a b', 2",'ba ')],
   'return texte[decalage:len(texte)] + texte[0:decalage]',kind='debug',
   starter='return texte[decalage:len(texte)] + texte[0:decalage + 1]',method='Utilisez deux découpages et une concaténation. Expliquez pourquoi le caractère d’indice decalage appartient uniquement au second morceau du texte initial.')

ex(10,'ligne_tableau','Remplir une cellule de largeur fixe','texte: str, largeur: int','str',
   'Retournez une cellule encadrée et complétée à droite.','largeur >= len(texte)',
   'Un petit terminal affiche des tableaux sans bibliothèque de mise en page. Chaque cellule doit occuper une largeur intérieure fixe pour que les séparateurs verticaux s’alignent. Les emplacements laissés libres après le texte sont rendus visibles par des traits de soulignement.',
   'Commencez par une barre `|`, ajoutez `texte`, complétez avec assez de caractères `_` pour atteindre `largeur` caractères à l’intérieur, puis ajoutez la barre finale. La largeur ne comprend pas les deux barres. Ne tronquez jamais le texte. Une largeur nulle avec un texte vide produit deux barres voisines. N’ajoutez aucun espace automatiquement.',
   ['Le mot chat occupe quatre des six positions intérieures ; deux soulignements complètent la cellule.', 'La cellule de largeur zéro n’a pas de contenu entre ses deux barres.'],
   [("'chat', 6",'|chat__|'),("'', 0",'||'),("'abc', 3",'|abc|'),("'', 3",'|___|'),("'a b', 4",'|a b_|'),("'é', 2",'|é_|')],
   'resultat: str = "|" + texte\ni: int\nfor i in range(len(texte), largeur):\n    resultat = resultat + "_"\nreturn resultat + "|"',method='Construisez le remplissage avec une boucle for, sans méthode de formatage ni multiplication d’une chaîne.')

ex(11,'compter_mots_message','Compter des blocs sans utiliser split','message: str','int',
   'Comptez les blocs non vides séparés par des espaces simples.','',
   'Une messagerie reçoit parfois des textes contenant plusieurs espaces de suite ou des espaces aux extrémités. Pour son compteur simplifié, elle appelle mot toute suite non vide de caractères qui ne sont pas des espaces simples. La ponctuation ne coupe pas un mot.',
   'Seul le caractère espace `" "` sépare les mots. Plusieurs espaces consécutifs forment une seule séparation et ne créent pas de mots vides. Les espaces au début et à la fin sont ignorés pour le comptage. Une tabulation reste un caractère ordinaire. Retournez zéro pour une chaîne vide ou composée uniquement d’espaces, sans utiliser `split`.',
   ['Les blocs salut, tout et le-monde sont les trois mots ; le tiret ne coupe pas le dernier.', 'Les trois espaces ne contiennent aucun bloc non vide.'],
   [("'  salut  tout le-monde '",3),("'   '",0),("''",0),("'bonjour'",1),("'a\\tb c'",2),("'a,b'",1),("' a b '",2)],
   'compte: int = 0\ndans_mot: bool = False\nc: str\nfor c in message:\n    if c == " ":\n        dans_mot = False\n    else:\n        if not dans_mot:\n            compte = compte + 1\n        dans_mot = True\nreturn compte',method='Utilisez un booléen indiquant si le parcours est déjà dans un mot. Un nouveau mot est compté uniquement à son premier caractère.',points=6)

ex(11,'plus_longue_activation','Repérer la plus longue période active','journal: str','int',
   'Retournez la longueur du plus long bloc de caractères 1 consécutifs.','',
   'Un appareil écrit un caractère à chaque relevé. Le caractère 1 indique qu’il est actif ; tout autre caractère signale une interruption de l’activité observée. Le technicien recherche la plus longue période active ininterrompue, même si elle se termine exactement à la fin du journal.',
   'Comptez uniquement les caractères `"1"` consécutifs. Un zéro, un espace ou tout autre caractère remet la longueur courante à zéro. Retournez la plus grande longueur rencontrée, pas le nombre total de caractères 1. S’il n’y a aucune activation, le résultat vaut zéro. Complétez le programme pour mémoriser un maximum pendant le parcours.',
   ['Les blocs actifs ont pour longueurs 2, 3 et 1 ; le plus long mesure 3.', 'La dernière séquence de quatre caractères 1 doit être entièrement prise en compte.'],
   [("'11011101'",3),("'001111'",4),("''",0),("'000'",0),("'1'",1),("'11x111'",3),("'10101'",1)],
   'courant: int = 0\nmaximum: int = 0\nc: str\nfor c in journal:\n    if c == "1":\n        courant = courant + 1\n        if courant > maximum:\n            maximum = courant\n    else:\n        courant = 0\nreturn maximum',kind='complete',
   starter='courant: int = 0\nmaximum: int = 0\nc: str\nfor c in journal:\n    if c == "1":\n        courant = courant + 1\n        # Mettez à jour le maximum si nécessaire.\n    else:\n        courant = 0\nreturn maximum',points=6)

ex(11,'premiere_baisse','Retrouver le premier niveau qui redescend','niveaux: str','Optional[int]',
   'Retournez l’indice de la première baisse, ou None s’il n’y en a pas.','',
   'Un appareil enregistre des niveaux sous la forme de caractères comparables. Le responsable souhaite localiser la première baisse par rapport au relevé immédiatement précédent. Il a besoin de l’indice du nouveau relevé, afin de retrouver le moment où la baisse a été observée.',
   'Comparez les caractères suivant l’ordre des chaînes Python, sensible à la casse. Pour un journal de chiffres, cet ordre coïncide avec celui des chiffres de zéro à neuf. Cherchez le premier indice i strictement positif tel que niveaux[i] soit inférieur à niveaux[i−1]. Une égalité n’est pas une baisse. Retournez None s’il n’existe pas, notamment pour zéro ou un caractère.',
   ['Le premier recul est de 4 vers 3 ; le caractère 3 se trouve à l’indice 3.', 'Les niveaux ne diminuent jamais ; l’égalité entre les deux caractères 2 est autorisée.'],
   [("'124355'",3),("'1229'",None),("''",None),("'7'",None),("'91'",1),("'AAAB'",None),("'ACB'",2)],
   'i: int\nfor i in range(1, len(niveaux)):\n    if niveaux[i] < niveaux[i - 1]:\n        return i\nreturn None',imports='from typing import Optional',
   method='`Optional[int]` signifie que la réponse peut être un entier ou la valeur `None`. Commencez le parcours à l’indice 1 pour pouvoir comparer au précédent, et sortez dès la première baisse.',points=6)

ex(11,'journal_coherent','Vérifier les entrées et les sorties','journal: str','bool',
   'Indiquez si le journal décrit une salle initialement et finalement vide, sans sortie impossible.','',
   'Une salle possède un compteur d’entrées et de sorties. Le journal utilise E pour une entrée et S pour une sortie ; les autres caractères sont des annotations. Avant de valider le journal, il faut vérifier qu’aucune personne ne sort d’une salle vide et que tout le monde est finalement sorti.',
   'Partez de zéro personne. Chaque `E` ajoute une personne et chaque `S` en retire une ; ignorez les autres caractères, y compris les lettres minuscules. Retournez False dès qu’une sortie rendrait l’effectif négatif. À la fin, l’effectif doit être exactement zéro. Le journal vide est cohérent. Corrigez le programme qui ne vérifie que le bilan final.',
   ['Deux entrées précèdent les deux sorties : le journal est cohérent et la salle finit vide.', 'Le bilan final est nul, mais la première sortie est impossible : le journal doit être refusé.'],
   [("'EESS'",True),("'SE'",False),("''",True),("'E'",False),("'E-x-S'",True),("'ESSE'",False),("'notes'",True),("'ESES'",True)],
   'effectif: int = 0\nc: str\nfor c in journal:\n    if c == "E":\n        effectif = effectif + 1\n    elif c == "S":\n        effectif = effectif - 1\n        if effectif < 0:\n            return False\nreturn effectif == 0',kind='debug',
   starter='effectif: int = 0\nc: str\nfor c in journal:\n    if c == "E":\n        effectif = effectif + 1\n    elif c == "S":\n        effectif = effectif - 1\nreturn effectif == 0',points=6)

ex(11,'changements_mode','Compter les changements d’état','journal: str','int',
   'Retournez le nombre de changements entre deux relevés consécutifs.','',
   'Un système enregistre son mode de fonctionnement avec un caractère par relevé. Plusieurs relevés identiques peuvent se suivre lorsque rien ne change. Le responsable veut compter les transitions réelles et ne souhaite pas considérer le premier état comme un changement.',
   'Deux caractères consécutifs différents comptent pour un changement, même si l’appareil revient ensuite dans un état déjà rencontré. Les majuscules, minuscules et espaces sont des états distincts. Retournez zéro pour un journal vide ou réduit à un seul caractère. Ne comptez ni le nombre de modes distincts ni le nombre total de blocs de caractères.',
   ['Les transitions A vers B puis B vers A donnent deux changements.', 'Les quatre relevés montrent toujours le même état : aucun changement.'],
   [("'AAABBA'",2),("'xxxx'",0),("''",0),("'A'",0),("'ABAB'",3),("'Aa A'",3),("'  A  '",2)],
   'compte: int = 0\ni: int\nfor i in range(1, len(journal)):\n    if journal[i] != journal[i - 1]:\n        compte = compte + 1\nreturn compte',method='Parcourez les indices à partir de 1. Expliquez pourquoi un journal non vide avec b blocs consécutifs possède b−1 changements.')

ex(12,'normaliser_espaces','Nettoyer une ligne saisie au clavier','texte: str','str',
   'Retournez le texte sans espaces aux extrémités et avec un seul espace entre les blocs.','',
   'Un formulaire laisse parfois passer des espaces superflus dans une ligne de texte. Avant d’imprimer la ligne, on veut retirer les espaces au début et à la fin, puis réduire chaque suite intérieure d’espaces à une seule séparation. Les autres caractères doivent rester dans leur ordre initial.',
   'Traitez uniquement le caractère espace simple `" "` ; une tabulation doit rester intacte. Une chaîne vide ou faite uniquement d’espaces devient vide. Aucun espace ne doit apparaître dans le résultat avant le premier caractère utile ni après le dernier. Construisez une nouvelle chaîne par parcours, sans employer `strip`, `split`, `join` ni `replace`.',
   ['Les espaces extérieurs disparaissent et les trois espaces entre bon et jour deviennent un seul.', 'Une ligne constituée uniquement d’espaces ne contient aucun caractère à conserver.'],
   [("'  bon   jour  '",'bon jour'),("'   '",''),("''",''),("'abc'",'abc'),("' a '",'a'),("'a  b   c'",'a b c'),("' a\\tb  c '",'a\tb c')],
   'resultat: str = ""\nattente: bool = False\nc: str\nfor c in texte:\n    if c == " ":\n        if len(resultat) > 0:\n            attente = True\n    else:\n        if attente:\n            resultat = resultat + " "\n        resultat = resultat + c\n        attente = False\nreturn resultat',
   method='Vous pouvez retarder l’écriture d’un espace jusqu’à la rencontre du prochain caractère utile. Ainsi, les espaces finaux ne sont jamais écrits.',points=6)

ex(12,'coder_signal','Encoder les bits sans perdre les séparateurs','signal: str','str',
   'Encodez chaque bit et conservez les autres caractères.','',
   'Un dispositif de transmission représente chaque bit par deux caractères pour rendre ses transitions visibles. Les techniciens ajoutent parfois des espaces ou des tirets dans le signal pour séparer les groupes. Ces annotations doivent rester telles quelles dans le texte encodé.',
   'Remplacez chaque caractère `0` du signal d’origine par `01` et chaque `1` par `10`. Copiez tous les autres caractères une seule fois, sans modification. Ne réencodez pas les caractères que vous venez d’ajouter au résultat. Une chaîne vide reste vide. Complétez le traitement du bit un dans le parcours fourni.',
   ['Les bits 0, 1 et 0 deviennent respectivement 01, 10 et 01, soit 011001.', 'Le tiret reste unique entre le code 10 du bit 1 et le code 01 du bit 0.'],
   [("'010'",'011001'),("'1-0'",'10-01'),("''",''),("'0'",'01'),("'1'",'10'),("'abc'",'abc'),("'0 1'",'01 10')],
   'resultat: str = ""\nc: str\nfor c in signal:\n    if c == "0":\n        resultat = resultat + "01"\n    elif c == "1":\n        resultat = resultat + "10"\n    else:\n        resultat = resultat + c\nreturn resultat',kind='complete',
   starter='resultat: str = ""\nc: str\nfor c in signal:\n    if c == "0":\n        resultat = resultat + "01"\n    else:\n        # Ajoutez une branche pour encoder le bit 1.\n        resultat = resultat + c\nreturn resultat')

ex(12,'couper_commentaire','Extraire la partie utile d’une ligne','ligne: str','str',
   'Retournez tout ce qui précède le premier marqueur de commentaire.','',
   'Un fichier de configuration simplifié autorise un commentaire après un caractère dièse. Le programme qui lit ce fichier doit conserver la partie utile de chaque ligne et ignorer le reste. Dans ce format pédagogique, il n’existe ni guillemets protecteurs ni caractères d’échappement.',
   'Le premier caractère `#` commence toujours un commentaire et n’appartient pas au résultat. Tout ce qui le suit est ignoré, même si d’autres dièses apparaissent. Si aucun dièse n’existe, retournez la ligne entière. Conservez exactement les espaces situés avant le marqueur. Un dièse en première position produit une chaîne vide ; une ligne vide aussi.',
   ['Les caractères nom=Eva et l’espace suivant sont conservés ; le commentaire est supprimé.', 'Un commentaire qui commence dès le premier caractère ne laisse aucune partie utile.'],
   [("'nom=Eva #élève'",'nom=Eva '),("'#tout ignorer'",''),("''",''),("'abc'",'abc'),("'a#b#c'",'a'),("'a #'",'a '),("'"+'"#"'+"'",'"')],
   'resultat: str = ""\nc: str\nfor c in ligne:\n    if c == "#":\n        return resultat\n    resultat = resultat + c\nreturn resultat',method='Utilisez un parcours avec sortie anticipée. N’utilisez ni `split` ni `find`. Les guillemets éventuels sont des caractères ordinaires.')

ex(12,'contenu_balise','Lire la première annotation entre crochets','texte: str','str',
   'Retournez le contenu de la première annotation complète.','',
   'Un journal contient des annotations entourées de crochets au milieu du texte courant. On souhaite extraire le contenu qui suit la première ouverture et précède la première fermeture rencontrée ensuite. Le format est volontairement simple et ne gère pas les annotations imbriquées.',
   'Ignorez tout ce qui précède le premier `[` ainsi que les `]` rencontrés avant cette ouverture. Après l’ouverture, le premier `]` termine l’annotation. Un nouveau `[` à l’intérieur est un caractère ordinaire. Si aucune ouverture ou aucune fermeture correspondante n’existe, retournez une chaîne vide. Les crochets extérieurs ne doivent jamais faire partie du résultat.',
   ['Seul le contenu ok de la première annotation est extrait ; la seconde est ignorée.', 'L’ouverture n’est jamais suivie d’une fermeture : aucune annotation complète n’est disponible.'],
   [("'avant[ok]apres[non]'",'ok'),("'avant[incomplet'",''),("''",''),("'abc]def'",''),("'[]'",''),("']x[a[b]z'",'a[b'),("'[a b]'",'a b')],
   'ouvert: bool = False\nresultat: str = ""\nc: str\nfor c in texte:\n    if ouvert:\n        if c == "]":\n            return resultat\n        resultat = resultat + c\n    elif c == "[":\n        ouvert = True\nreturn ""',kind='debug',
   starter='ouvert: bool = False\nresultat: str = ""\nc: str\nfor c in texte:\n    if ouvert:\n        if c == "]":\n            return resultat\n        resultat = resultat + c\n    elif c == "[":\n        ouvert = True\nreturn resultat',points=6)

ex(12,'executer_repetitions','Interpréter une touche de répétition','commandes: str','str',
   'Construisez le texte produit par les caractères ordinaires et la commande plus.','',
   'Un clavier simplifié possède une touche plus qui répète le dernier caractère ordinaire tapé. Les autres caractères sont écrits normalement. Plusieurs pressions sur plus doivent continuer à répéter le même caractère ; elles ne remplacent pas la mémoire du dernier caractère ordinaire.',
   'Parcourez `commandes` de gauche à droite. Un caractère différent de `+` est ajouté au résultat et devient le caractère mémorisé, y compris s’il s’agit d’un espace. Un `+` ajoute une copie du caractère mémorisé ; sans caractère mémorisé, il est ignoré. Les plus ne sont jamais écrits eux-mêmes. Une commande vide produit un texte vide.',
   ['Après ab, les deux plus ajoutent deux b ; après c, le dernier plus ajoute un c : abbbcc.', 'Les deux premiers plus sont ignorés ; x est ensuite écrit puis répété une fois.'],
   [("'ab++c+'",'abbbcc'),("'++x+'",'xx'),("''",''),("'+++'",''),("'abc'",'abc'),("'a+b++'",'aabbb'),("'a +b'",'a  b')],
   'resultat: str = ""\ndernier: str = ""\nc: str\nfor c in commandes:\n    if c == "+":\n        resultat = resultat + dernier\n    else:\n        resultat = resultat + c\n        dernier = c\nreturn resultat',method='Utilisez une chaîne pour mémoriser le dernier caractère ordinaire. Sa valeur initiale peut être la chaîne vide : ajouter celle-ci n’a aucun effet.',points=6)
