import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_paivittyy(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_kokonaishinta_tasmaa(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        self.assertEqual(self.kori.hinta(), 7)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_kokonaishinta_tasmaa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_eri_ostosta(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    # 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos_jonka_nimi_tasmaa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos_jonka_lukumaara_tasmaa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].lukumaara(), 2)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")

    def test_korissa_on_kaksi_tuotetta_joista_poistetaan_yksi_ostoksen_lukumaara_tasmaa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_kori_on_tyhja_ainoa_tuotteen_poiston_jalkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostosten_lkm = len(self.kori.ostokset())

        self.assertEqual(ostosten_lkm, 0)

    def test_korin_tyhjennys_onnistuu(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        self.kori.tyhjenna()
        ostosten_lkm = len(self.kori.ostokset())

        self.assertEqual(ostosten_lkm, 0)
