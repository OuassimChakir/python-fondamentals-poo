from Batiment import Batiment
class Maison(Batiment):
    def __init__(self,adresse, nbPieces):
        super().__init__(adresse)
        self.__nbPieces = nbPieces

    def getNbPieces(self):
        return self.__nbPieces
    def setNbPieces(self,nbPieces):
        self.__nbPieces = nbPieces

    def __str__(self):
        return "Maison: \n\tAdresse: {}\n\tNbPieces: {}".format(Batiment.getAdresse(self), self.__nbPieces)