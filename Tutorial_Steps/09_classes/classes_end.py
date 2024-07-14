"""

You did it!

Now, the question you are probably not asking - what if we wanted a specific class for each species of animal?

To the next module!

"""


class Animal:

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def get_species(self):
        return self.species

    def get_name(self):
        return self.name


bilbo = Animal('Bilbo', 'Dog')
print(bilbo.get_species())

fritters = Animal('Fritters', 'Cat')
print(fritters.get_name())
print(fritters.get_species())

