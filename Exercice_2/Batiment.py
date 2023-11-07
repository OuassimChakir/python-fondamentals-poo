class Batiment:
    def __init__(self, adresse):
        self.__adresse = adresse

    def __init__(self):
        self.__adresse = ""

    def getAdresse(self):
        return self.__adresse

    def setAdresse(self, adresse):
        self.__adresse = adresse

    def __str__(self):
        return "Adresse: {}".format(self.__adresse)