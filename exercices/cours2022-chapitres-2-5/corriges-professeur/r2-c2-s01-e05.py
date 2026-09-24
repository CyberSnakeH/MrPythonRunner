# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S01 · 05 — Préparer les badges d’une rencontre

def budget_badges(participants: int, accompagnants: int, stock: int) -> int:
    """Calculez le budget d’achat en centimes pour les badges et leurs attaches.
    Précondition : participants >= 0 and accompagnants >= 0 and 0 <= stock <= participants + accompagnants
    """
    personnes: int = participants + accompagnants
    neufs: int = personnes - stock
    return neufs * 35 + personnes * 12

# Vérifications
assert budget_badges(10, 2, 4) == 424
assert budget_badges(3, 2, 5) == 60
assert budget_badges(0, 0, 0) == 0
assert budget_badges(1, 0, 0) == 47
assert budget_badges(0, 4, 1) == 153
assert budget_badges(20, 0, 10) == 590
