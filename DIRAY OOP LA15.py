class Dog():
    def __init__(self,name,):
        self.name = name 
    def speak(self):
        print(f"Dog: {self.name}")

class Cat():
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print(f"CAT: {self.name}")

class Bird():
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print(f"BIRD: {self.name}")

class Fish():
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print(f"FISH: {self.name}")

def animal_sounds(animal):
    animal.speak()

aso = Dog("Arf! Arf!")
puzzy = Cat("Meiow")
berd = Bird("twit twit")
pis = Fish(". . .")

for hayop in [aso,puzzy,berd,pis]:
    animal_sounds(hayop)