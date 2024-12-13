class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
       
    def describeVehicle(self):
        print(f"Is a {self.brand} and a {self.model}, with {self.fuel_type}")
       
class Car(Vehicle):
    pass
car = Car("Lamborghini", "Volkswagen","premium 93 octane fuel")
car.describeVehicle()

class Motorcycle(Vehicle):
    pass
mutur = Motorcycle("Ducati","Panigale V2","Gasoline Manual")
mutur.describeVehicle()