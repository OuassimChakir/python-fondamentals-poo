from Batiment import Batiment
class Immeuble(Batiment):
    def __init__(self,adresse, nbAppart):
        super().__init__(adresse)
        self.nbAppart = nbAppart

    def getNbPieces(self):
        return self.nbAppart
    def setNbPieces(self,nbAppart):
        self.nbAppart = nbAppart

    def __str__(self):
        return "Immauble: \n\tAdresse: {}\n\tNombres D'appartements: {}".format(Batiment.getAdresse(self), self.nbAppart)