import unittest
from guiaDeEjerciciosDeRepaso_N5 import is_disarium

class IsDisariumTestCase(unittest.TestCase):
    def test_is_disarium_75(self):
        self.assertEqual(is_disarium(75), False)

    def test_is_disarium_135(self):
        self.assertEqual(is_disarium(135), True)

    def test_is_disarium_544(self):
        self.assertEqual(is_disarium(544), False)

    def test_is_disarium_518(self):
        self.assertEqual(is_disarium(518), True)

    def test_is_disarium_466(self):
        self.assertEqual(is_disarium(466), False)

    def test_is_disarium_8(self):
        self.assertEqual(is_disarium(8), True)


if __name__ == '__main__':
    unittest.main()
