"""

You have done it once again! This is one of those situations that takes forever to find, but one line fixes it.

Now that we are handling this error, what if someone messes with it? That's where Unit Tests come in and are a huge part
of programming, especially when it involves more than one person.

"""


class Calculator:
    def add_numbers(self, a, b):
        total = None
        try:
            total = a + b
        except TypeError:
            print("One of these is not a number, dude - {} and {}".format(a, b))
        return total


calc = Calculator()
print(calc.add_numbers("x", 2))
print(calc.add_numbers(3, 2))

