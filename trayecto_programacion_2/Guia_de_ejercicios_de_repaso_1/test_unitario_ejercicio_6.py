import unittest
import guiaDeEjerciciosDeRepaso_6 as ejercicio


class MyTestCase(unittest.TestCase):
    def numeros_al_cuadrado_9119(self):
        lista_de_numeros_uno = (9119)
        self.assertEqual(ejercicio.elevar_numeros_cuadrado(lista_de_numeros_uno), 811181)

    def numeros_al_cuadrado_2483(self):
        lista_de_numeros_dos = (2483)
        self.assertEqual(ejercicio.elevar_numeros_cuadrado(lista_de_numeros_dos), 416649)


if __name__ == '__main__':
    unittest.main()
