import unittest
from poo_ejercicio_N2 import Lampara

class Ejercicio2TestCase(unittest.TestCase):
    def test_prender(self):
        lampara = Lampara()
        lampara.prender()
        self.assertEqual(lampara.get_esta_prendida(), True)
    def test_apagar(self):
        lampara = Lampara()
        lampara.apagar()
        self.assertEqual(lampara.get_esta_prendida(), False)

    def test_alternar(self):
        lampara = Lampara()
        lampara.prender()
        lampara.alternar()
        self.assertEqual(lampara.get_esta_prendida(), False)
        lampara.alternar()
        self.assertEqual(lampara.get_esta_prendida(), True)

    def test_get_esta_prendida_str(self):
        lampara = Lampara()
        lampara.prender()
        self.assertEqual(lampara.get_esta_prendida_str(), "APAGADA")
        lampara.apagar()
        self.assertEqual(lampara.get_esta_prendida_str(), "PRENDIDA")

if __name__ == '__main__':
    unittest.main()