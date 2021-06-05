class Pet:
    def __init__(self, name, type, tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=100
        self.energy=100
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
    def play(self):
        self.health+=5
        return self
    def noise(self):
        print('Moo')

class Cow(Pet):
    def __init__(self, name):
        self.name=name
        self.type="Cow"
        self.tricks="Flying Over The Moon"
        self.health=100
        self.energy=100
    def play(self):
        self.health-=50
        print("Silly Ninja, you can't play with a cow")
        return self

class Turtle(Pet):
    def __init__(self, name):
        self.name=name
        self.type="Turtle"
        self.tricks="Spin in Circles"
        self.health=100
        self.energy=100
    def play(self):
        self.health-=10
        print("Chase that turtle ninja")
        return self