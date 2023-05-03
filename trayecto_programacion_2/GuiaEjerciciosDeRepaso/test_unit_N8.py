import unittest
from guiaDeEjerciciosDeRepaso_N8 import verificar_orden

class MyTestCase(unittest.TestCase):
    def test_verificar_orden_uno(self):
        simon_says = ([1, 2], [5, 1])
        resultado = verificar_orden(simon_says)
        self.assertEqual(True, resultado)  # add assertion here

    def test_verificar_orden_two(self):
        simon_says_two = ([1, 2], [5, 5])
        resultado = verificar_orden(simon_says_two)
        self.assertEqual(False, resultado)  # add assertion here


if __name__ == '__main__':
    unittest.main()
