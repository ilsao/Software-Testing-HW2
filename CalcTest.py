import unittest

from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_sub(self):
        calc = Calculator()
        result = calc.sub(3, 2)
        self.assertEqual(result, 1)
        
    def test_mul(self):
        calc = Calculator()
        result = calc.mul(2, 3)
        self.assertEqual(result, 6)
        
    def test_div(self):
        calc = Calculator()
        result = calc.div(3, 2)
        self.assertEqual(result, 1.5)

    def test_modulo_negative_dividend(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(-7, 3), 2)

    def test_modulo_zero(self):
        calc = Calculator()
        with self.assertRaisesRegex(ValueError, "Cannot modulo by zero"):
            calc.modulo(7, 0)

    def test_power_zero_to_zero(self):
        calc = Calculator()
        self.assertEqual(calc.power(0, 0), 1)

    def test_power_negative_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, -3), 0.125)

    def test_div_zero(self):
        calc = Calculator()
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            calc.div(3, 0)

if __name__ == "__main__":
    unittest.main()
