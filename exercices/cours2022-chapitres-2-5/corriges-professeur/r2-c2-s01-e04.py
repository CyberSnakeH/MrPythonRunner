# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.
# S01 · 04 — Les octets oubliés par l’appareil photo

def taille_archive(nombre: int, largeur: int, hauteur: int) -> int:
    """Retournez la taille en octets d’une archive de photographies non compressées.
    Précondition : nombre >= 0 and largeur > 0 and hauteur > 0
    """
    image: int = largeur * hauteur * 3
    fiche_image: int = image + 16
    return 128 + nombre * fiche_image

# Vérifications
assert taille_archive(2, 2, 3) == 196
assert taille_archive(0, 10, 10) == 128
assert taille_archive(1, 1, 1) == 147
assert taille_archive(3, 4, 5) == 356
assert taille_archive(1, 10, 10) == 444
assert taille_archive(5, 2, 2) == 268
