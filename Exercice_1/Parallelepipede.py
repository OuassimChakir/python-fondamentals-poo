from Point import Point
from Rectangle import Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, x, y, longeur, largeur, hauteur):
        super().__init__(x, y, longeur, largeur)
        self.__hauteur = hauteur
    def getHauteur(self):
        return self.__hauteur

    def setHauteur(self,hauteur):
        self.__hauteur = hauteur

    def aire(self):
        face1 = self.__hauteur * Rectangle.getLargeur(self)
        face2 = Rectangle.aire(self)
        face3 = self.__hauteur * Rectangle.getLongeur(self)
        return 2 * (face1 + face2 + face3)

    def volume(self):
        return self.__hauteur * Rectangle.getLongeur(self) * Rectangle.getLargeur(self)

    def __str__(self):
        return "Parallelepipede: \n[X: {}, Y: {}, Largeur: {}, Longeur: {}, Hauteur: {}]".format(Point.getX(self), Point.getY(self), Rectangle.getLargeur(self) ,Rectangle.getLongeur(self), self.__hauteur)