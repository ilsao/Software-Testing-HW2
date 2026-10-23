import random
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
        self.assertIsInstance(result, float)

    def test_div_zero(self):
        calc = Calculator()
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            calc.div(3, 0)
            
class TestCalculatorMetamorphic(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        # A fixed seed makes generated failures reproducible.
        rng = random.Random(20261024)
        self.values = [-10000, -1, 0, 1, 10000]
        self.values.extend(rng.randint(-10000, 10000) for _ in range(100))
        self.triples = [tuple(rng.sample(self.values, 3)) for _ in range(100)]

    def test_add_and_mul_commute(self):
        for a, b, _ in self.triples:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))
                self.assertEqual(self.calc.mul(a, b), self.calc.mul(b, a))

    def test_add_and_mul_associate(self):
        for a, b, c in self.triples:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(
                    self.calc.add(self.calc.add(a, b), c),
                    self.calc.add(a, self.calc.add(b, c)),
                )
                self.assertEqual(
                    self.calc.mul(self.calc.mul(a, b), c),
                    self.calc.mul(a, self.calc.mul(b, c)),
                )

    def test_add_and_sub_are_inverses(self):
        for a, b, _ in self.triples:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.sub(self.calc.add(a, b), b), a)
                self.assertEqual(self.calc.add(self.calc.sub(a, b), b), a)

    def test_subtraction_is_antisymmetric(self):
        for a, b, _ in self.triples:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.sub(a, b), -self.calc.sub(b, a))

    def test_multiplication_distributes_over_addition(self):
        for a, b, c in self.triples:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(
                    self.calc.mul(a, self.calc.add(b, c)),
                    self.calc.add(self.calc.mul(a, b), self.calc.mul(a, c)),
                )

    def test_mul_and_div_are_inverses(self):
        for a in self.values:
            for b in self.values:
                if b == 0:
                    continue
                with self.subTest(a=a, b=b):
                    self.assertAlmostEqual(self.calc.div(self.calc.mul(a, b), b), a)
                    self.assertAlmostEqual(self.calc.mul(self.calc.div(a, b), b), a)

    def test_division_is_invariant_under_common_scaling(self):
        for a, b, scale in self.triples:
            if b == 0 or scale == 0:
                continue
            with self.subTest(a=a, b=b, scale=scale):
                self.assertAlmostEqual(
                    self.calc.div(a, b),
                    self.calc.div(self.calc.mul(a, scale), self.calc.mul(b, scale)),
                )


if __name__ == "__main__":
    unittest.main()
