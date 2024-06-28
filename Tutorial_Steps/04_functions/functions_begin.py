"""
Objective: Create a function that receives an int and adds one to it.

So, let's talk about functions. Generally, Python runs code from top to bottom.
However, there are many exceptions, like a function.

A function is a block of code that when called... does something.
Additionally, it can:
1) Receive variables (like message in our function below).
2) Return variables (using the word return like below)

The syntax is the following:

def [Function Name]([Optional Variables to pass in, either [name] or [name]:[type]):
[Indent] [Code]

Example:

def adds_numbers(number_one:int, number_two:int):
    sum = number_one + number_two
    return sum

OR

def adds_numbers(number_one, number_two):
    sum = number_one + number_two
    return sum

Always try to specify the type if you can though, or you will put others through a nightmare.

Now try the objective!
"""


def print_and_return_stuff(message: str):
    print("I am printing a string!")
    print(message)
    return message


print_and_return_stuff("Hi Mom!")
