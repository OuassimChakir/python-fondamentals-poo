class Employe:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def setNom(self, nom):
        self.__nom = nom
    def setPrenom(self, prenom):
        self.__prenom = prenom
    def __str__(self):
        return "Employe: \n\tNom Complet: {} {}".format(self.__prenom, self.__nom)
    def gains(self):
        pass