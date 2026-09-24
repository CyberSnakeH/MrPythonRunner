# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S01 · 02 — Une réserve à ne pas consommer

def autonomie_robot(charge: float, reserve: float, consommation: float) -> float:
    """Retournez le nombre d’heures pendant lesquelles le robot peut travailler avant d’atteindre sa réserve.
    Précondition : 0 <= reserve <= charge and consommation > 0
    """
    utilisable: float = charge - reserve
    return utilisable / consommation

# Vérifications
import math
assert math.isclose(autonomie_robot(120.0, 30.0, 30.0), 3.0, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(autonomie_robot(50.0, 50.0, 8.0), 0.0, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(autonomie_robot(0.0, 0.0, 2.0), 0.0, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(autonomie_robot(25.0, 0.0, 10.0), 2.5, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(autonomie_robot(10.0, 4.0, 8.0), 0.75, rel_tol=1e-9, abs_tol=1e-9)
import math
assert math.isclose(autonomie_robot(100.0, 10.0, 20.0), 4.5, rel_tol=1e-9, abs_tol=1e-9)
