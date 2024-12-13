class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("lambo","fenk")
print(car1.brand, car1.color)
car1.color = "mlu"
print(car1.brand, car1.color)

car2 = Car("BMW","porpol")
print(car2.brand, car2.color)