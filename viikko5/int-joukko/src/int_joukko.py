

class IntJoukko:
    def __init__(self, kapasiteetti: int = 5, kasvatuskoko: int = 5):
        self.kasvatuskoko = max(0, kasvatuskoko)
        self.lukujono = [0] * kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujono

    def paivita_kapasiteetti(self):
        if self.alkioiden_lkm == len(self.lukujono):
            self.lukujono = [*self.lukujono, *
                             [0 for i in range(self.kasvatuskoko)]]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.paivita_kapasiteetti()
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdistejoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in [*a_taulu, *b_taulu]:
            yhdistejoukko.lisaa(i)

        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        leikkaus = filter(lambda x: x in b_taulu, a_taulu)
        for number in leikkaus:
            leikkausjoukko.lisaa(number)

        return leikkausjoukko

    @staticmethod
    def erotus(a, b):
        erotusjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        erotus = filter(lambda x: x not in b_taulu, a_taulu)
        for numero in erotus:
            erotusjoukko.lisaa(numero)
        return erotusjoukko

    def __str__(self):
        alkiot_merkkijonona = ", ".join(
            map(lambda x: str(x), self.lukujono[:self.alkioiden_lkm]))
        return f"{{{alkiot_merkkijonona}}}"
