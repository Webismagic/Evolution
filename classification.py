#https://www.geeksforgeeks.org/create-classes-dynamically-in-python/
#https://ent1c3d.github.io/Python-Synopsis/site/advanced/Python_Metaclasses/

from lecteurXML import XML_Data

Parser = XML_Data('taxons.xml')
Objects = {}
Classes = {}
Parents = {}

class classification():

    def __init__(self, nom):

        taxons = Parser.selectNodes("taxon",nom)
        self.getClassification(taxons)

    def getClassification(self,taxons):

        newClass = object
        for taxon,infos_taxon in taxons:

            # creating class dynamically
            nom = taxon
            parent = infos_taxon['parent']
            classification = infos_taxon['classification']
            caractere = infos_taxon['caractere']

            classe_parente = newClass

            newClass = type(nom, (classe_parente,), {
                'nom' : nom,
                'parent' : parent,
                'classification' : classification,
                'caractere' : caractere,
            })

            Objects[nom] = newClass()
            Classes[nom] = newClass
            Parents[nom] = newClass.__base__

        for cle,valeur in Classes.items():

            print(valeur.classification + " : " + valeur.nom)
            print(valeur.caractere)
            #print(valeur.mro())
