import unittest
from main_at01 import add, subtract, divide, multiply, check

from main_at01 import remainder


class TestMath(unittest.TestCase):
    def test_remainder(self):  # ДЗ
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(210, 2), 0)

        self.assertNotEqual(remainder(10, 3), 2)
        self.assertNotEqual(remainder(21, 8), 0)

        self.assertRaises(ValueError, remainder, 5, 0)

    def test_add(self):
        self.assertEqual(add(2, 5,), 7)
        self.assertNotEqual(add(10, 12), 20)

    def test_subtruct(self):
        self.assertEqual(subtract(10, 1), 9)
        self.assertNotEqual(subtract(5, 2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertNotEqual(multiply(14, 2), 20)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertNotEqual(divide(28, 2), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 5, 0)

    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(20))

        self.assertTrue(not check(21))
        self.assertFalse(check(321))


if __name__ == '__main__':
    unittest.main()
