# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S01 · 01 — Découper un rouleau sans gaspillage

def ruban_affiches(nombre: int, hauteur: float, separation: float) -> float:
    """Calculez la longueur de papier nécessaire pour imprimer une rangée d’affiches.
    Précondition : nombre >= 1 and hauteur > 0 and separation >= 0
    """
    impression: float = nombre * hauteur
    decoupe: float = (nombre - 1) * separation
    return impression + decoupe

# Vérifications
import math
assert math.isclose(ruban_affiches(3, 30.0, 2.0), 94.0, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(ruban_affiches(1, 12.5, 4.0), 12.5, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(ruban_affiches(2, 10.0, 0.0), 20.0, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(ruban_affiches(4, 2.5, 0.5), 11.5, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(ruban_affiches(10, 1.0, 1.0), 19.0, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(ruban_affiches(2, 1.2, 0.1), 2.5, rel_tol=1e-9, abs_tol=1e-9)
