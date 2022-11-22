import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5
            elif tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "suklaa", 3)
            elif tuote_id == 3:
                return Tuote(3, "kahvi", 7)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock,
                             self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla argumentilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5)
        # return self._pankki.tilisiirto(nimi, viite, tili_numero, self._kaupan_tili, summa)

    def test_ostetaan_kaksi_varastossa_olevaa_eri_tuotetta(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 8)

    def test_ostetaan_kaksi_varastossa_olevaa_samaa_tuotetta(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 6)

    def test_yritetaan_ostaa_tuote_joka_ei_ole_varastossa(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 3)

    def test_uusi_asiointi_nollaa_edellisen_ostoskorin(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("paavo", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "paavo", 42, "54321", "33333-44455", 5)

    def test_jokaiselle_maksulle_annetaan_uusi_viite(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 1, ANY, ANY, ANY)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("paavo", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "paavo", 2, ANY, ANY, ANY)

    def test_tuotteen_poistaminen_tyhjentaa_ostoskorin(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, ANY, ANY, 0)
