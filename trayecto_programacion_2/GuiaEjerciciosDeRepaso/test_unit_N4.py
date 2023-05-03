import unittest
import guiaDeEjerciciosDeRepaso_N4


class MyTestCase(unittest.TestCase):
    def test_pokerColor(self):
        tablero = ["3_S", "10_H", "10_D", "10_C", "10_S"]
        cartasEnMano = ["3_S", "4_D"]
        resultado = guiaDeEjerciciosDeRepaso_N4.existeColorEnPoker(tablero, cartasEnMano)
        self.assertEqual(resultado, False)  # add assertion here

    def test_pokerColor_dos(self):
        tablero = ["A_S", "J_H", "7_D", "8_D", "10_D"]
        cartasEnMano = ["J_D", "3_D"]
        resultado = guiaDeEjerciciosDeRepaso_N4.existeColorEnPoker(tablero, cartasEnMano)
        self.assertEqual(resultado, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
