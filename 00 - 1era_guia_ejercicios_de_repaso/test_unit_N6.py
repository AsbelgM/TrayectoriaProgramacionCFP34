import unittest
import guiaDeEjerciciosDeRepaso_N6 as elevarDigitosCuadrado


class MyTestCase(unittest.TestCase):
    def test_potencia_uno(self):
        resultado = elevarDigitosCuadrado.elevar_numeros_cuadrado(elevarDigitosCuadrado.lista_de_numeros_uno)
        resultadoEsperado = 811181
        self.assertEqual(resultado, resultadoEsperado)  # add assertion here

    def test_potencia_dos(self):
        resultado = elevarDigitosCuadrado.elevar_numeros_cuadrado(elevarDigitosCuadrado.lista_de_numeros_dos)
        resultadoEsperado = 416649
        self.assertEqual(resultado, resultadoEsperado)  # add assertion here


if __name__ == '__main__':
    unittest.main()
