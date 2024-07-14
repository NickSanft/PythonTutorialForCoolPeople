"""

You did it, I am so proud of you!

At this point, you know all the basics of Python. All that remains is learning and an absurd amount of Google.

"""
import unittest
import wikipedia


class Machine:
    def __init__(self, name):
        self.runs_on_electricity = True
        self.name = name


class Calculator(Machine):
    calculator_brand = "ci"

    def add_numbers(self, a: int, b: int):
        if type(a) is not int:
            raise ValueError("a must be an integer")
        elif type(b) is not int:
            raise ValueError("b must be an integer")
        else:
            return a + b

    def subtract_numbers(self, a: int, b: int):
        result = a - b
        return result

    def multiply_numbers(self, a: int, b: int):
        return a * b

    def divide_numbers(self, a: int, b: int):
        try:
            return a / b
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")

    def get_wiki_page(self):
        result = wikipedia.page("Calculator")
        print(result.summary)


class TestCalculatorMethods(unittest.TestCase):
    calc = Calculator("Dave")

    # general tests
    def test_get_wiki_page_works(self):
        self.calc.get_wiki_page()

    def test_inherits_machine(self):
        self.assertEqual(True, self.calc.runs_on_electricity)

    def test_calculator_has_name(self):
        self.assertTrue(self.calc.name)

    def test_calculator_brand_equals_ci(self):
        self.assertEqual("ci", self.calc.calculator_brand)

    # add_numbers tests

    def test_add_returns_int(self):
        self.assertEqual(int, type(self.calc.add_numbers(3, 2)))

    def test_adding_positive_numbers(self):
        self.assertEqual(5, self.calc.add_numbers(3, 2))

    def test_adding_non_numbers(self):
        self.assertRaises(ValueError, self.calc.add_numbers, "Hello", 2)

    # subtract_numbers tests
    def test_subtract_returns_int(self):
        self.assertEqual(int, type(self.calc.subtract_numbers(3, 2)))

    def test_subtract_positive_numbers(self):
        self.assertEqual(1, self.calc.subtract_numbers(3, 2))

    # multiply_numbers tests

    def test_multiple_positive_numbers(self):
        self.assertEqual(6, self.calc.multiply_numbers(3, 2))

    # divide_numbers tests

    def test_dividing_positive_numbers(self):
        self.assertEqual(20, self.calc.divide_numbers(100, 5))

    def test_dividing_by_zero(self):
        self.assertRaises(ValueError, self.calc.divide_numbers, 10, 0)
