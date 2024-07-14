"""
Objective - make a Human class and add some functions for stuff only humans have

Inheritance is the nuttiest part of Python, but once you have the "click" moment everything makes sense.

We made an Animal class, but what if we wanted animals with their own specific functions like a dog barking?
We could just make our classes for each, but if we wanted the species and name we'd be copy/pasting a ton.

That's where inheritance comes in!

The syntax is pretty easy again:

class [ClassName]([ClassToInheritFrom]):
    [Functions and variables go here]

When you do this, think of it as a blueprint extending a blueprint. It will have the

If you want to call function from the class you are inheriting from, there is a function called super.
If you look at the 1st line of the __init__ method in Dog, you will see that we can actually call that function in
Animal.

Let's take a look specifically at the Dog class now. I have added a function called "bark", but we still have all of our
Animal functions too!

Now, trying making your own Human class that inherits from Animal and make your own cool functions.  
"""


class Animal:

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def get_species(self):
        return self.species

    def get_name(self):
        return self.name


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Dog")

    def bark(self):
        print("{} says - Bark!".format(self.name))


bilbo = Dog("Bilbo")
print(bilbo.get_species())
bilbo.bark()
