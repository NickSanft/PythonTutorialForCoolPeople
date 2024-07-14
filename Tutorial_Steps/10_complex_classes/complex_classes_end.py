"""

You did it!

Do you see how we can abstract away some of the fluff from the Animal class?

Taking that further, there is a lot of Python code you will use that's one line for you, but thousands of lines from
other people.

"""


class Animal:

    def __init__(self, name: str, species: str, tail: bool):
        self.name = name
        self.species = species
        self.tail = tail

    def get_species(self):
        return self.species

    def get_name(self):
        return self.name

    def has_tail(self):
        return self.tail


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Dog", True)

    def bark(self):
        print("{} says - Bark!".format(self.name))


class Human(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Human", False)

    def talk(self, message: str):
        print("My name is {} - {}".format(self.name, message))


bilbo = Dog("Bilbo")
print(bilbo.get_species())
bilbo.bark()
print(bilbo.has_tail())

alex = Human("Alex")
print(alex.has_tail())
alex.talk("Hey guys, I can talk")
