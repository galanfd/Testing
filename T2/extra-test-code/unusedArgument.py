class Fruit:

    def __init__(self, name, vitamins):
        self.name = name
        self.vitamins = vitamins

    def change_vitamins(self):
        self.vitamins = []

    def eat_fruit(self, vitamins):
        print("Eating fruit with vitamins: ", vitamins)

def test1(var1, z):
    print(var1)

def test2(var1,x, z):
    test1(var1, z)

def test3(var1, var2):
    test1(var1, var2)