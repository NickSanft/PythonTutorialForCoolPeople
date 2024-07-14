"""

Objective - Add unit tests for negative numbers and anything else you want.

Alright, Unit Tests! These are essential for making sure you do not break stuff important.
If you take a look at our TestCalculatorMethods class, you will see it is inheriting from a TestCase class.

In PyCharm, do you see the green arrow near the class and functions? You can click that to run all or a specific test.
Try running it, then try changing the TypeError back to a ValueError and try running the unit tests again :)

In real applications, a ton of these unit tests are run every time to build code. This will make sure that you have not
broken anything, especially if you have an application being used by customers.

Onto the objective, add some more functions - test negative numbers, maybe even some crazy scenarios.

"""
import unittest


class Calculator:
    def add_numbers(self, a, b):
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
