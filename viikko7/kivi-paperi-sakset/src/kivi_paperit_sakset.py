from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KiviPaperiSakset:
    def __init__(self) -> None:
        self.tuomari = Tuomari()

    def pelaa(self):

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


class KpsPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaaja siirto: ")


class KpsParempiTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto


class KpsTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
