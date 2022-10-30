import unittest
import guiaDeEjerciciosDeRepaso_N3

class MyTestCase(unittest.TestCase):
    def test_operaciones_aritmeticas(self):
        resultadoEsperado = (1, 1, 0, 'No es posible dividir entre 0')
        resultado = guiaDeEjerciciosDeRepaso_N3.operacion_sumar(1,0)
        self.assertEqual(resultado, resultadoEsperado)  # add assertion here

    def test_operaciones_aritmeticas_dos(self):
        resultadoEsperado = (24, 0, 144, 1)
        resultado = guiaDeEjerciciosDeRepaso_N3.operacion_sumar(12,12)
        self.assertEqual(resultado, resultadoEsperado)  # add assertion here

if __name__ == '__main__':
    unittest.main()
