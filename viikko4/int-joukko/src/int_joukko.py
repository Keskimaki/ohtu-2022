class IntJoukko:
    def __init__(self, kapasiteetti = 5, kasvatuskoko = 5):
        try:
            self.kapasiteetti = abs(int(kapasiteetti))
            self.kasvatuskoko = abs(int(kasvatuskoko))
        except:
            raise ValueError("Kapasiteetin ja kasvatuskoon on oltava kokonaislukuja.")

        self.lukujono = [0] * self.kapasiteetti
        self.alkiomaara = 0

    def kuuluu(self, n: int):
        for luku in self.lukujono:
            if luku == n:
                return True

        return False

    def lisaa(self, n: int):
        if self.kuuluu(n):
            return

        self.lukujono[self.alkiomaara] = n
        self.alkiomaara += 1

        if self.alkiomaara % len(self.lukujono) == 0:
            self.lukujono.append([0] * self.kasvatuskoko)

    def poista(self, n: int):
        loytyi = False

        for i, luku in enumerate(self.lukujono):
            if n == luku:
                loytyi = True
                self.lukujono[i] = 0
                self.alkiomaara = self.alkiomaara - 1
                break

        if loytyi:
            for j in range(i, self.alkiomaara):
                self.lukujono[j] = self.lukujono[j+1]

    def mahtavuus(self):
        return self.alkiomaara

    def to_int_list(self):
        tulos = []
        for i in range(self.alkiomaara):
            tulos.append(self.lukujono[i])

        return tulos

    @staticmethod
    def alusta(a: "IntJoukko", b: "IntJoukko"):
        tulos = IntJoukko()
        a = a.to_int_list()
        b = b.to_int_list()

        return tulos, a, b

    @staticmethod
    def yhdiste(a: "IntJoukko", b: "IntJoukko"):
        tulos, a, b = IntJoukko.alusta(a, b)

        for luku in a:
            tulos.lisaa(luku)

        for luku in b:
            tulos.lisaa(luku)

        return tulos

    @staticmethod
    def leikkaus(a: "IntJoukko", b: "IntJoukko"):
        tulos, a, b = IntJoukko.alusta(a, b)

        for aluku in a:
            for bluku in b:
                if aluku == bluku:
                    tulos.lisaa(aluku)

        return tulos

    @staticmethod
    def erotus(a: "IntJoukko", b: "IntJoukko"):
        tulos, a, b = IntJoukko.alusta(a, b)

        for luku in a:
            tulos.lisaa(luku)

        for luku in b:
            tulos.poista(luku)

        return tulos

    def __str__(self):
        tuloste = "{"

        if self.alkiomaara > 0:
            tuloste += str(self.lukujono[0])

        for i in range(1, self.alkiomaara):
            tuloste += f", {self.lukujono[i]}"

        tuloste += "}"

        return tuloste
