"""
Objective: Instead of printing the values of our variables, print the type.

Additional Info:

In Python, variables have different types; in the first step, we use a String (str).

How does Python know it is string?

That is due to it being wrapped in double-quotes.
If it's just a number, it assumes an integer.
True or False, a boolean.
...and so on.

...but how do WE know it is a string? What if this variable is coming from a million lines of horror?

Python has a handy function for this called type.
If you pass in a variable like type(message), it will return the type of thing the variable is.

Let's get crazy and try putting the type function IN the print function :)
It will return the type, which will then be printed.

"""

message = "My custom message!"
my_favorite_number = 5
do_i_like_bread = True
nothing = None

print(message)
print(my_favorite_number)
print(do_i_like_bread)
print(nothing)
