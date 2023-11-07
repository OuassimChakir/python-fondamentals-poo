from Point import Point


class Rectangle(Point):
    def __init__(self, x, y, longeur, largeur):
        super().__init__(x, y)
        self.__longeur = longeur
        self.__largeur = largeur

    def getLongeur(self):
        return self.__longeur
    def getLargeur(self):
        return self.__largeur
    def setLongeur(self,longeur):
        self.__longeur = longeur
    def setLargeur(self, largeur):
        self.__largeur = largeur

    def aire(self):
        return self.__largeur * self.__longeur

    def __str__(self):
        return "Rectangle: \n[X: {}, Y: {}, Largeur: {} , Longeur: {}]".format(Point.getX(self), Point.getY(self), self.__largeur,self.__longeur)