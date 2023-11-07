from Employe import Employe
class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heurs):
        super().__init__(nom, prenom)
        self.__retribution = retribution
        self.__heurs = heurs
    def getRetribution(self):
        return self.__retribution
    def getHeurs(self):
        return self.__heurs

    def setRetribution(self, retribution):
        self.__retribution = retribution
    def setHeurs(self, heurs):
        self.__heurs = heurs

    def __str__(self):
        return "TravailleurHoraire: \n\tNom Complet: {} {}\n\tRetribution: {}\n\tHeurs: {}".format(Employe.getPrenom(self), Employe.getNom(self), self.__retribution, self.__heurs)

    def gains(self):
        return self.__retribution * self.__heurs