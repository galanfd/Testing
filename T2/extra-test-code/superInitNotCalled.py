class Mammal:
    def __init__(self, mammalName):
        self.name = mammalName

    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def __init__(self, wingedAnimalName):
        self.name = wingedAnimalName

    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    def __init__(self):
        super(Bat, self).__init__("Bat")

    def mammal_info(self):
        print("Bats are mammals.")

class FlyingSquirrel(Mammal, WingedAnimal):
    def __init__(self):
        self.name = "Flying Squirrel"