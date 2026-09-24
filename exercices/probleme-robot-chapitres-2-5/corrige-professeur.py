# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.

def cout_action(action: str) -> int:
    """Retourne le coût d’une action reconnue, ou -1 pour une action inconnue.
    """
    if action == "A":
        return 2
    elif action == "R":
        return 1
    elif action == "P":
        return 0
    return -1


def action_possible(energie: int, action: str) -> bool:
    """Indique si une action est reconnue et peut être entièrement financée.
    Précondition : energie >= 0
    """
    cout: int = cout_action(action)
    return cout >= 0 and cout <= energie


def position_apres(position: int, action: str) -> int:
    """Retourne la position après une action, sans gérer la batterie.
    """
    if action == "A":
        return position + 1
    elif action == "R":
        return position - 1
    return position


def recharger(energie: int, capacite: int, gain: int) -> int:
    """Retourne l’énergie après une minute de recharge, sans dépasser la capacité.
    Précondition : 0 <= energie <= capacite and gain > 0
    """
    nouvelle: int = energie + gain
    if nouvelle > capacite:
        return capacite
    return nouvelle


def minutes_recharge(energie: int, capacite: int, gain: int, cible: int) -> int:
    """Retourne le nombre minimal de minutes pour atteindre au moins la charge cible.
    Précondition : 0 <= energie <= capacite and gain > 0 and 0 <= cible <= capacite
    """
    charge: int = energie
    minutes: int = 0
    while charge < cible:
        charge = recharger(charge, capacite, gain)
        minutes = minutes + 1
    return minutes


def avancer_au_maximum(energie: int, distance: int) -> int:
    """Retourne le nombre d’avances réalisables, dans la limite de la distance demandée.
    Précondition : energie >= 0 and distance >= 0
    """
    reste: int = energie
    pas: int = 0
    while pas < distance and action_possible(reste, "A"):
        reste = reste - cout_action("A")
        pas = pas + 1
    return pas


def programme_valide(programme: str) -> bool:
    """Indique si tous les caractères du programme sont des commandes reconnues.
    """
    action: str
    for action in programme:
        if cout_action(action) < 0:
            return False
    return True


def energie_programme(programme: str) -> int:
    """Retourne le coût total du programme, ou -1 s’il contient une commande inconnue.
    """
    total: int = 0
    action: str
    for action in programme:
        cout: int = cout_action(action)
        if cout < 0:
            return -1
        total = total + cout
    return total


def prefixe_executable(programme: str, energie: int) -> str:
    """Retourne le préfixe exécuté avant la première action impossible.
    Précondition : energie >= 0
    """
    resultat: str = ""
    reste: int = energie
    action: str
    for action in programme:
        if not action_possible(reste, action):
            return resultat
        resultat = resultat + action
        reste = reste - cout_action(action)
    return resultat


def position_finale(programme: str, energie: int, depart: int) -> int:
    """Retourne la position après les seules actions effectivement exécutables.
    Précondition : energie >= 0
    """
    execute: str = prefixe_executable(programme, energie)
    position: int = depart
    action: str
    for action in execute:
        position = position_apres(position, action)
    return position


def energie_restante(programme: str, energie: int) -> int:
    """Retourne l’énergie disponible après l’arrêt du robot.
    Précondition : energie >= 0
    """
    execute: str = prefixe_executable(programme, energie)
    return energie - energie_programme(execute)


def bilan_mission(programme: str, energie: int, depart: int) -> str:
    """Retourne le compte rendu textuel standardisé de la mission.
    Précondition : energie >= 0
    """
    if not programme_valide(programme):
        return "INVALIDE"
    execute: str = prefixe_executable(programme, energie)
    position: int = position_finale(programme, energie, depart)
    reste: int = energie_restante(programme, energie)
    etat: str = "BLOQUE"
    if len(execute) == len(programme):
        etat = "TERMINE"
    sens: str = "SUR_PLACE"
    if position > depart:
        sens = "AVANT"
    elif position < depart:
        sens = "ARRIERE"
    batterie: str = "RESTE"
    if reste == 0:
        batterie = "VIDE"
    return etat + ";" + sens + ";" + batterie


# Vérifications
assert cout_action('A') == 2
assert cout_action('a') == -1
assert cout_action('R') == 1
assert cout_action('P') == 0
assert action_possible(2, 'A') == True
assert action_possible(0, 'P') == True
assert action_possible(1, 'A') == False
assert action_possible(100, 'X') == False
assert position_apres(-2, 'A') == -1
assert position_apres(0, 'R') == -1
assert position_apres(7, 'P') == 7
assert position_apres(3, 'AA') == 3
assert recharger(8, 10, 3) == 10
assert recharger(2, 10, 3) == 5
assert recharger(10, 10, 3) == 10
assert recharger(0, 0, 4) == 0
assert minutes_recharge(2, 10, 3, 8) == 2
assert minutes_recharge(9, 10, 3, 8) == 0
assert minutes_recharge(0, 10, 4, 10) == 3
assert minutes_recharge(0, 0, 1, 0) == 0
assert avancer_au_maximum(5, 4) == 2
assert avancer_au_maximum(10, 2) == 2
assert avancer_au_maximum(9, 0) == 0
assert avancer_au_maximum(6, 3) == 3
assert programme_valide('APRA') == True
assert programme_valide('A R') == False
assert programme_valide('') == True
assert programme_valide('Ar') == False
assert energie_programme('APRA') == 5
assert energie_programme('AAX') == -1
assert energie_programme('') == 0
assert energie_programme('PPP') == 0
assert prefixe_executable('APAR', 3) == 'AP'
assert prefixe_executable('PXAR', 9) == 'P'
assert prefixe_executable('PPA', 0) == 'PP'
assert prefixe_executable('ARP', 3) == 'ARP'
assert position_finale('APAR', 3, 10) == 11
assert position_finale('RR', 2, 0) == -2
assert position_finale('XA', 9, 4) == 4
assert position_finale('ARP', 3, -2) == -2
assert energie_restante('APAR', 3) == 1
assert energie_restante('XA', 5) == 5
assert energie_restante('ARP', 3) == 0
assert energie_restante('', 7) == 7
assert bilan_mission('ARP', 3, 0) == 'TERMINE;SUR_PLACE;VIDE'
assert bilan_mission('APAR', 3, 10) == 'BLOQUE;AVANT;RESTE'
assert bilan_mission('AAX', 0, 0) == 'INVALIDE'
assert bilan_mission('RR', 5, 7) == 'TERMINE;ARRIERE;RESTE'
