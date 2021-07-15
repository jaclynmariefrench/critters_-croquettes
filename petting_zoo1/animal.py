# import the python datetime module to help us create a timestamp
from datetime import date


class Llama:
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"


miss_fuzz = Llama("Mary", "Llama", "midday", "Llama feed")

print(miss_fuzz.feed())


class Dog:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"


barky = Dog("Barky", "Cocker Spaniel", "morning", "Kibbles and bits")


class Monkey:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"


bananas = Monkey("Bananas", "Spider Monkey", "evening", "Bananas and nuts")


print(
    f"{barky.name} has a shift during the {barky.shift} today. She is an energetic {barky.species}!"
)
