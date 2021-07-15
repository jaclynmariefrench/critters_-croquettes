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
sassy = Llama("Sassy", "Llama", "morning", "Llama feed")
potato = Llama("Potato", "Llama", "evening", "Llama feed")

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
wolf = Dog("Wolf", "Husky", "evening", "Bacon bits")
queeny = Dog("Queeny", "Corgi", "Midday", "Princess Pebbles")


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
mikey = Monkey("Mikey", "Monkey", "morning", "fruits")
stacey = Monkey("Stacey", "Monkey", "Midday", "Strawberries")


