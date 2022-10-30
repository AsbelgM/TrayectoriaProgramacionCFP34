import unittest
from poo_ejercicio_N1 import Rectangulo

class Ejercicio1TestCase(unittest.TestCase):
    def test_area_5base_2altura_10(self):
        rectangulo = Rectangulo(base=5,altura=2)
        area = rectangulo.get_area()
        self.assertEqual(area, 10)

    def test_perimetro_5base_2altura_14(self):
        rectangulo = Rectangulo(base=5,altura=2)
        perimetro = rectangulo.get_perimetro()
        self.assertEqual(perimetro, 14)

if __name__ == '__main__':
    unittest.main()