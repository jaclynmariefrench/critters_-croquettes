# import the python datetime module to help us create a timestamp
from datetime import date


class Llama:
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


miss_fuzz = Llama("Mary", "Llama", "midday")


class Dog:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

barky = Dog("Barky", "Cocker Spaniel", "morning")

class Monkey:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

bananas = Monkey("Bananas", "Spider Monkey", "evening")


print(f'{barky.name} has a shift during the {barky.shift} today. She is an energetic {barky.species}!') 