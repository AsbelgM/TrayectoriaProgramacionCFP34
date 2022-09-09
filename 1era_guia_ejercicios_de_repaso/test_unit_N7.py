import unittest
import guiaDeEjerciciosDeRepaso_N7 as ordenarListas


class MyTestCase(unittest.TestCase):
    def test_ordenar_lista_uno(self):
        resultado = ordenarListas.ordernar_listas(ordenarListas.listaUno)
        resultadoEsperado = [1, 2, 3, 4]
        self.assertEqual(resultado, resultadoEsperado)  # add assertion here

    def test_ordenar_lista_dos(self):
        resultado = ordenarListas.ordernar_listas(ordenarListas.listaTres)
        resultadoEsperado = [1, 2, 3, 6, 7]
        self.assertEqual(resultado, resultadoEsperado)  # add assertion here


if __name__ == '__main__':
    unittest.main()
