from math import pi


class Cercle(object):
    "Construit des cercles de tailles variées"

    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return pi * self.rayon ** 2


class Cylindre(Cercle):
    "Construit des cylindres"

    def __init__(self, rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur = hauteur

    def surface(self):
        return (Cercle.surface(self) * 2) + (2 * pi * self.rayon * self.hauteur)

    def volume(self):
        return Cercle.surface(self) * self.hauteur


class Cone(Cylindre):
    def __int__(self, rayon, hauteur):
        Cylindre.__init__(self, rayon, hauteur)

    def volume(self):
        return Cylindre.volume(self) / 3


def addition(a, b):
    return a + b

def exposant(a, b):
    return a**b


if __name__ == "__main__":
    print(addition(2, 7))
    print(exposant(2, 3))
