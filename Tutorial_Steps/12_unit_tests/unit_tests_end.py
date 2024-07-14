"""

See? That was not so bad.

If you look down below, I tested for one more weird case - if one of the variables is None. There, if it is, the code
raises, or "throws" an error for the program.

One of coolest parts of unittest is that you can check to make sure these errors are happening using assertRaises.

"""
import unittest


class Calculator:
    def add_numbers(self, a, b):
        if a is None:
            raise ValueError("a is None")
        if b is None:
            raise ValueError("b is None")

        total = None
        try:
            total = a + b
        except TypeError:
            print("One of these is not a number, dude - {} and {}".format(a, b))
        return total


class TestCalculatorMethods(unittest.TestCase):
    calc = Calculator()

    def test_positive_numbers(self):
        self.assertEqual(5, self.calc.add_numbers(3, 2))

    def test_non_numbers(self):
        self.assertEqual(type(None), type(self.calc.add_numbers("x", 2)))

    def test_negative_numbers(self):
        self.assertEqual(-10, self.calc.add_numbers(-1, -9))

    def test_a_none(self):
        self.assertRaises(ValueError, self.calc.add_numbers, None, 5)

    def test_b_none(self):
        self.assertRaises(ValueError, self.calc.add_numbers,5, None)
