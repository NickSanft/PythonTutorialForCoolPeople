"""

Objectives:
    1) Import any missing modules.
    2) Update Calculator to inherit from Machine and call the init method (look at complex_classes_end.py for a hint)
    3) Add a multiply_numbers function to Calculator.
    4) Fix the Calculator code so that all tests pass. Please do not update the tests themselves.
    5) Add tests for negative numbers for add, subtract, multiply, and divide.

We have made it to the end of our beginner's Python tutorial!!! This will be a culmination of everything you have
learned throughout this course. Go slowly, execute the tests, and Google the crap out of everything you can.

***Disclaimer***
Please DO NOT change the tests, these should all work. The Calculator code is all that needs to change

"""
import unittest
import wikipedia


class Machine:
    def __init__(self, name):
        self.runs_on_electricity = True
        self.name = name


class Calculator:
    calculator_brand = 2

    def add_numbers(self, a: int, b: int):
        return a + b

    def subtract_numbers(self, a: int, b: int):
        result = str(a - b)
        return result

    # multiply numbers should go here

    def divide_numbers(self, a: int, b: int):
        return a / b

    def get_wiki_page(self):
        result = wikipedia.page("Calculator")
        print(result.summary)


class TestCalculatorMethods(unittest.TestCase):
    calc = Calculator()

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
