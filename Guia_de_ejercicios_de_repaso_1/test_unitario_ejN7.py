import unittest
import guiaDeEjerciciosRepaso_n7 as elementosAgrupados


class MyTestCase(unittest.TestCase):
    def test_listas_agrupadas_uno(self):
        listaUno = [1, 2, 4, 3]
        self.assertEqual(elementosAgrupados.ordernar_listas(listaUno), [1, 2, 3, 4])  # add assertion here

    def test_listas_agrupadas_dos(self):
        listaDos = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
        self.assertEqual(elementosAgrupados.ordernar_listas(listaDos), [1, 2, 3, 4])  # add assertion here


if __name__ == '__main__':
    unittest.main()
