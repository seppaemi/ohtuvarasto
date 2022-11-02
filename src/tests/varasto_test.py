import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 9)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_esitysmuoto(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
        self.varasto.lisaa_varastoon(8)
        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")
        self.varasto.ota_varastosta(2)
        self.assertEqual(str(self.varasto), "saldo = 6, vielä tilaa 4")
    
    def test_konstruktori_hukkaa_extra_saldo(self):
        self.testVarasto = Varasto(10,300)
        self.assertAlmostEqual(self.testVarasto.saldo, 10)
    
    def test_hukkaa_extra_lisatty_saldo(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_ohita_extra_ottaminen(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_nollataan_negatiivinen_tila(self):
        self.testVarasto = Varasto(8, -1)
        self.assertAlmostEqual(self.testVarasto.saldo, 0)
    
    def test_konstruktori_nollataan_negatiivinen_saldo(self):
        self.testVarasto = Varasto(-2)
        self.assertAlmostEqual(self.testVarasto.tilavuus, 0)
    
    def test_ohita_negatiivinen_lisäys(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_ohita_negatiivinen_otto(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(self.varasto.saldo, 8)
