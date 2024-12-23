class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power = atk_power
    def basic_atk(self, target):
        target.health -= self.atk_power
   
mahito = Player("Mahito",8000,5000)
nanami = Player("Nanami Kento",9000, 7000)

while mahito.health < 0:
    print("ded :p")