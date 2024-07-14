"""
Objectives
    1) Add name to the __init__ function as an argument and "set" it.
    2) Create a new instance of Animal with a name and species and print them both.

Ah, classes, the bread and butter of Object-Oriented programming.

You can think of a class as a blueprint for... something. A calculator, an animal, etc.
You can then use this blueprint to create multiple "instances" of this object with different variables.

The syntax is pretty simple -

class [className]:
    [Functions and variables go here]

...and the syntax to use this blueprint to make an "instance" is also pretty straightforward:

VariableName = ClassName(WhateverArgumentsYouPutInHere)

For the arguments that you pass inside these parentheses, these are based on a function called __init__.
In programming, this is what we call a "Constructor", where you can initialize anything an instance of the class
is going to need.

By default, the only argument is the instance itself, which is not something you have to pass in.
However, in the example below, you will see that we have added two additional variables - name and species.

After that, you can use it however you see fit.

Why is this useful, though?

As you saw in the last module, we used an instance of BeautifulSoup to parse a webpage's HTML and make it pretty.
Do you know how to do that by hand in Python? I definitely do not, but someone wrote a class for it, and I'm using it.
Besides Python's built-in functions like print and type, most Python code revolves around this pattern.

"""


class Animal:

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def get_species(self):
        return self.species


bilbo = Animal('Bilbo', 'Dog')
print(bilbo.get_species())
