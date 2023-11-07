from Employe import Employe
class TravailleurCommission(Employe):
    def __init__(self, nom, prenom, salaire, commission, qte):
        super().__init__(nom, prenom)
        self.__salaire = salaire
        self.__commission = commission
        self.__qte = qte

    def getSalaire(self):
        return self.__salaire
    def getCommission(self):
        return self.__commission
    def getQuantite(self):
        return self.__qte

    def setSalaire(self, salaire):
        self.__salaire = salaire
    def setCommission(self, commission):
        self.__commission = commission
    def setQuantite(self, qte):
        self.__qte = qte

    def __str__(self):
        return "TravailleurCommission: \n\tNom Complet: {} {}\n\tSalaire: {}\n\tCommission: {}\n\tQuantite: {}".format(Employe.getPrenom(self), Employe.getNom(self), self.__salaire, self.__commission, self.__qte)

    def gains(self):
        return self.__salaire + (self.__commission * self.__qte)