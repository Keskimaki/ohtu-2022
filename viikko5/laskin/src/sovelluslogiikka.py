class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

class Summa:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        arvo = int(self._lue_syote())
        self._sovellus.plus(arvo)

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        arvo = int(self._lue_syote())
        self._sovellus.miinus(arvo)

class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self):
        self._sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, lue_syote):
        pass