import unittest
from poo_ejercicio_N5 import Segmento
from poo_ejercicio_N4 import Punto


class Ejercicio5TestCase(unittest.TestCase):
    def test_longitud_segmento(self):
        punto_a = Punto(10, 10)
        punto_b = Punto(10, -10)
        segmento = Segmento(punto_a, punto_b)
        self.assertEqual(segmento.longitud_segmento(), 20.0)


if __name__ == '__main__':
    unittest.main()