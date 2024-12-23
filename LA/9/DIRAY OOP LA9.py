class Car:
    def __init__(self,brand):
         self.brand = brand
    
    
    def __str__(self):
        return f"{self.brand} is fenk"
        
ror = Car ("Lambo")
del ror
print(ror)