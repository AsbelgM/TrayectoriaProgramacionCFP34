import unittest
import guiaDeEjerciciosDeRepaso_N1


class MyTestCase(unittest.TestCase):
    def test_listas(self):
        listaSinAgrupar = ["table", "table", "table"]
        resultado = guiaDeEjerciciosDeRepaso_N1.lista_resultado(listaSinAgrupar)
        self.assertEqual(resultado, {'tables'})  # add assertion here

    def test_listas_aux(self):
        listaSinAgruparDos = ["cow", "pig", "cow", "cow"]
        resultado = guiaDeEjerciciosDeRepaso_N1.lista_resultado(listaSinAgruparDos)
        self.assertEqual(resultado, {'pig', 'cows'})  # add assertion here


if __name__ == '__main__':
    unittest.main()
