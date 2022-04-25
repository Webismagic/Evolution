from xml.dom import minidom
#https://www.guru99.com/manipulating-xml-with-python.html

class XML_Data():

    def __init__(self, fichier):

        self.file = minidom.parse(fichier)

    def selectNodes(self, taxon, taxon_nom):

        XMLdata = self.file.getElementsByTagName(taxon)
        XMLdata.sort(key=lambda x: int(x.attributes['niveau'].value), reverse=True)

        taxons = {}

        for node in XMLdata:

            nom = node.getAttribute('nom')
            parent_nom = node.getAttribute('parent')

            taxon = {nom:{}}
            taxon[nom]["parent"] = parent_nom
            taxon[nom]["classification"] = node.getAttribute('classification')
            taxon[nom]["niveau"] = node.getAttribute('niveau')
            taxon[nom]["caractere"] = node.firstChild.data

            if (nom == taxon_nom):
                taxons.update(taxon)
                taxon_nom =  parent_nom

        taxons = sorted(taxons.items(), key=lambda x: x[1]['niveau'])

        return taxons





