class Eucaryote():
    def __init__(self):

        self.classification = "Domaine"
        self.caractere = "leurs cellules ont un noyau délimité par une double membrane ainsi que d'autres organites comme les mitochondries."

class Metazoaire(Eucaryote):
    def __init__(self):

        Eucaryote.__init__(self)

        self.classification = "Règne"
        self.caractere = "multicellulaires et hétérotrophes, qui se nourrissent de matière organique (Animalia)"


class Chordé(Metazoaire):
    def __init__(self):

        Metazoaire.__init__(self)

        self.classification = "Embranchement"
        self.caractere = "formé d’animaux à symétrie bilatérale (Bilatériens), qui possèdent une lamelle cartilagineuse située sur le côté dorsal de l'animal, forme la plus élémentaire d'un endosquelette (squelette interne)"


class Vertébré(Chordé):
    def __init__(self):

        Chordé.__init__(self)

        self.classification = "Sous-Embranchement"
        self.caractere = "possèdent un squelette interne composé d'un crâne ainsi que d'une colonne vertébrale"


class Tétrapode(Vertébré):
    def __init__(self):

        Vertébré.__init__(self)

        self.classification = "Super-classe"
        self.caractere = "animaux vertébrés gnathostomes dont le squelette comporte habituellement deux paires de membres et dont la respiration est normalement pulmonaire"

class Mammifère(Tétrapode):
    def __init__(self):

        Tétrapode.__init__(self)

        self.classification = "Classe"
        self.caractere = "présence de fourrures (excepté pour certains mammifères marins), d'une oreille moyenne comportant trois os, d'un néocortex et de glandes mammaires"


class Euthérien(Mammifère):
    def __init__(self):

        Mammifère.__init__(self)

        self.classification = "Infra-classe"
        self.caractere = "mammifères placentaires caractérisés par le fait qu'ils accouchent des juvéniles (grâce au placenta) par contraste avec les marsupiaux qui accouchent de larves ou les monotrèmes qui pondent des œufs."


