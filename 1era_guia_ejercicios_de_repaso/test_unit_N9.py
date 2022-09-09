import unittest
import guiaDeEjerciciosDeRepaso_N9 as presupuestos


class MyTestCase(unittest.TestCase):
    def test_totales_presupuestos(self):
        presupuesto_uno = presupuestos.presupuesto_uno
        self.assertEqual(presupuestos.calcular_totales(presupuesto_uno), 65700)

    def test_dos_totales_presupuestos(self):
        presupuesto_dos = presupuestos.presupuesto_dos
        self.assertEqual(presupuestos.calcular_totales(presupuesto_dos), 62600)


if __name__ == '__main__':
    unittest.main()
