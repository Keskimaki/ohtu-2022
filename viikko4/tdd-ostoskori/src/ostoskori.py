from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        summa = 0
        for ostos in self._ostokset.values():
            summa += ostos.lukumaara()

        return summa

    def hinta(self):
        summa = 0
        for ostos in self._ostokset.values():
            summa += ostos.hinta()

        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        nimi = lisattava.nimi()

        if nimi in self._ostokset:
            self._ostokset[nimi].muuta_lukumaaraa(1)
        else:
            ostos = Ostos(lisattava)
            self._ostokset[ostos.tuotteen_nimi()] = ostos

    def poista_tuote(self, poistettava: Tuote):
        nimi = poistettava.nimi()

        if self._ostokset[nimi].lukumaara == 1:
            del self._ostokset[nimi]
        else:
            self._ostokset[nimi].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
