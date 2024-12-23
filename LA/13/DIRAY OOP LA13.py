class Animal():
    def __init__(self,name,type):
        self.name = name
        self.type = type
   
class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = True
       
pis = Fish("Sunfish","Saltwater","True")
print(pis.can_swim)