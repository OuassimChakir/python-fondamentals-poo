from Employe import Employe
class Patron(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.__salaire = salaire
    def getSalaire(self):
        return self.__salaire
    def setSalaire(self, salaire):
        self.__salaire = salaire
    def __str__(self):
        return "Patron: \n\tNom Complet: {} {}\n\tSalaire: {}".format(Employe.getPrenom(self), Employe.getNom(self), self.__salaire)

    def gains(self):
        return self.__salaire