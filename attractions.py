from .petting_zoo1 import Llama, Dog, Monkey

class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

varmint_village = PettingZoo("Varmint Village")


class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithery friends to smile at"
        self.animals = list()

class Wetlands:
    
    def __init__(self, name):
        self.attraction_name = name
        self.description = "swimmy friends to stare at"
        self.animals = list()


