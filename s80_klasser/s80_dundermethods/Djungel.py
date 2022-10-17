class Djungel:
    pass

class Apa(Djungel):
    
    def __str__(self):
        return "Apan äter banan"


class Elefant(Djungel):

    def __str__(self):
        return "Dricker vatten"

class Gorilla(Djungel):

    def __str__(self, weight):
        return "slåss"

print()