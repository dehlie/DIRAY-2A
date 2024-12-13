class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
         
    def describeToy(self):
        print(f'''Toy: {self.name} Price: {self.price}''')
       
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

raruan = Car("Bullet Egg", "900" )
raruan.describeToy()