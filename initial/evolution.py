from classification import *

class Evolution():

    taxons = []
    classe = ""

    def __init__(self, groupe):

        self.groupe = eval(groupe + "()")
        self.classe = self.groupe.__class__.__name__
        self.taxons.append(self.classe)

    def classification(self):

        while self.classe != "object":

            self.groupe = self.__create_object()
            self.classe = self.groupe.__class__.__name__
            self.taxons.append(self.classe)

        self.taxons.reverse()
        for taxon in self.taxons:
            if (taxon != "object"):
                Object = eval(taxon + "()")
                print(Object.classification + " : " + taxon + " (" + Object.caractere + ")")

    def __create_object(self):

        for base in self.groupe.__class__.__bases__:

            Object = eval(base.__name__)()
            return Object

