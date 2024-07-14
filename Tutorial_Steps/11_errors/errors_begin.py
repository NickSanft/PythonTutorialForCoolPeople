"""
Objective - update the add_numbers function to catch the error when this is run.

You have made it past the hardest parts of Python, let's slow down and look at errors.

As you saw way back in the debug module, when you do something wrong, you get an error and Python exits.
What if we simply do not want that to happen, though?

That's where try-except comes in! (try-catch in a lot of other languages).

In the try statement, you can attempt to do something, and in the except you can pass in a specific type of error to
"catch". Instead of Python throwing an error and unraveling all reality, you can handle it yourself however you want.

Lastly, in the "finally" statement, this will always happen whether you have an error or not. It is useful if you need
to make sure something is ALWAYS done.

Alright, go for the objective. Make sure to read the error type that is being printed in the console, it's a huge help.

***Disclaimer***
USE THIS SPARINGLY. If you use this to cover issues you don't want to deal with, you will cause future pain on others.
Usually, this will end up being you many years later.

"""


def add_numbers(a, b):
    total = None
    try:
        total = a + b
    except IOError:
        print("One of these is not a number, dude - {} and {}".format(a, b))
    finally:
        return total


print(add_numbers("x", 2))
print(add_numbers(3, 2))
