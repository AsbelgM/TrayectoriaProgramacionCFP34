import unittest
from poo_ejercicio_N4 import Punto


class Ejercicio4TestCase(unittest.TestCase):
    def test_cuadrante_1(self):
        punto = Punto(1, 1)
        self.assertEqual(punto.cuadrante(), 1)

    def test_cuadrante_2(self):
        punto = Punto(-1, 1)
        self.assertEqual(punto.cuadrante(), 2)

    def test_cuadrante_3(self):
        punto = Punto(-1, -1)
        self.assertEqual(punto.cuadrante(), 3)

    def test_cuadrante_4(self):
        punto = Punto(1, -1)
        self.assertEqual(punto.cuadrante(), 4)

    def test_distancia_al_centro(self):
        punto = Punto(2, 2)
        self.assertEqual(punto.distancia_al_centro(), 2.8284271247461903)

    def test_metodo_equal(self):
        punto_a = Punto(2, 2)
        punto_b = Punto(1, 1)
        punto_c = Punto(1, 1)
        self.assertEqual(punto_a == punto_b, False)
        self.assertEqual(punto_c == punto_b, True)

    def test_metodo_str(self):
        punto = Punto(1, 3)
        punto_to_string = punto.__str__()
        self.assertEqual(punto_to_string, "Punto en (1,3)")


if __name__ == '__main__':
    unittest.main()
