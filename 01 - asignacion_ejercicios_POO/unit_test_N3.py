import unittest
from poo_ejercicio_N3 import Calculadora

class Ejercicio3TestCase(unittest.TestCase):
    def test_sumar_2_5__7(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.sumar(2,5), 7)

    def test_dividir_10_5__2(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.dividir(10,5), 2)

    def test_restar_2_5__menos3(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.restar(2,5), -3)

    def test_multiplicar_2_5__10(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.multiplicar(2,5), 10)

if __name__ == '__main__':
    unittest.main()