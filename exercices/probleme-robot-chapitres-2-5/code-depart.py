def cout_action(action: str) -> int:
    """Retourne le coût d’une action reconnue, ou -1 pour une action inconnue.
    """
    # Question 1 : remplacez ce retour provisoire.
    return 0


def action_possible(energie: int, action: str) -> bool:
    """Indique si une action est reconnue et peut être entièrement financée.
    Précondition : energie >= 0
    """
    # Question 2 : remplacez ce retour provisoire.
    return False


def position_apres(position: int, action: str) -> int:
    """Retourne la position après une action, sans gérer la batterie.
    """
    # Question 3 : remplacez ce retour provisoire.
    return 0


def recharger(energie: int, capacite: int, gain: int) -> int:
    """Retourne l’énergie après une minute de recharge, sans dépasser la capacité.
    Précondition : 0 <= energie <= capacite and gain > 0
    """
    # Question 4 : remplacez ce retour provisoire.
    return 0


def minutes_recharge(energie: int, capacite: int, gain: int, cible: int) -> int:
    """Retourne le nombre minimal de minutes pour atteindre au moins la charge cible.
    Précondition : 0 <= energie <= capacite and gain > 0 and 0 <= cible <= capacite
    """
    # Question 5 : remplacez ce retour provisoire.
    return 0


def avancer_au_maximum(energie: int, distance: int) -> int:
    """Retourne le nombre d’avances réalisables, dans la limite de la distance demandée.
    Précondition : energie >= 0 and distance >= 0
    """
    # Question 6 : remplacez ce retour provisoire.
    return 0


def programme_valide(programme: str) -> bool:
    """Indique si tous les caractères du programme sont des commandes reconnues.
    """
    # Question 7 : remplacez ce retour provisoire.
    return False


def energie_programme(programme: str) -> int:
    """Retourne le coût total du programme, ou -1 s’il contient une commande inconnue.
    """
    # Question 8 : remplacez ce retour provisoire.
    return 0


def prefixe_executable(programme: str, energie: int) -> str:
    """Retourne le préfixe exécuté avant la première action impossible.
    Précondition : energie >= 0
    """
    # Question 9 : remplacez ce retour provisoire.
    return ""


def position_finale(programme: str, energie: int, depart: int) -> int:
    """Retourne la position après les seules actions effectivement exécutables.
    Précondition : energie >= 0
    """
    # Question 10 : remplacez ce retour provisoire.
    return 0


def energie_restante(programme: str, energie: int) -> int:
    """Retourne l’énergie disponible après l’arrêt du robot.
    Précondition : energie >= 0
    """
    # Question 11 : remplacez ce retour provisoire.
    return 0


def bilan_mission(programme: str, energie: int, depart: int) -> str:
    """Retourne le compte rendu textuel standardisé de la mission.
    Précondition : energie >= 0
    """
    # Question 12 : remplacez ce retour provisoire.
    return ""
