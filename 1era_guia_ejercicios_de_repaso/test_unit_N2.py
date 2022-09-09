import unittest
import guiaDeEjerciciosDeRepaso_N2 as secuenciaNumeros


class MyTestCase(unittest.TestCase):
    def test_secuencia_uno_True(self):
        secuenciaUno = secuenciaNumeros.secuencia1
        resultado = secuenciaNumeros.numeros_consecutivos(secuenciaUno)
        self.assertEqual(True, resultado)  # add assertion here

    def test_secuencia_uno_False(self):
        secuenciaDos = secuenciaNumeros.secuencia2
        resultado = secuenciaNumeros.numeros_consecutivos(secuenciaDos)
        self.assertEqual(False, resultado)  # add assertion here


if __name__ == '__main__':
    unittest.main()
