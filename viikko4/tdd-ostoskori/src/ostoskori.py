from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = {}

    def tavaroita_korissa(self):
        summa = 0
        for ostos in self.ostokset.values():
            summa += ostos.lukumaara()

        return summa

    def hinta(self):
        summa = 0
        for ostos in self.ostokset.values():
            summa += ostos.hinta()

        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        nimi = lisattava.nimi()
        if nimi in self.ostokset:
            self.ostokset[nimi].muuta_lukumaaraa(1)
        else:
            ostos = Ostos(lisattava)
            self.ostokset[ostos.tuotteen_nimi()] = ostos

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
