"""

You have done it once again! This is one of those situations that takes forever to find, but one line fixes it.

Now that we are handling this error, what if someone messes with it? That's where Unit Tests come in and are a huge part
of programming, especially when it involves more than one person.

"""


def add_numbers(a, b):
    total = None
    try:
        total = a + b
    except TypeError:
        print("One of these is not a number, dude - {} and {}".format(a, b))
    finally:
        return total


print(add_numbers("x", 2))
print(add_numbers(3, 2))
