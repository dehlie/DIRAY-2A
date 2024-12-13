class Appliance():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating!")

class Washing_Machine(Appliance):
    def operate(self):
        print("wasing clothews")

class Refrigirator(Appliance):
    def operate(self):
        print("lamiig!")

class Microwave(Appliance):
    def operate(self):
        print("iniiit!")

wasingwasing = Washing_Machine("Samsung", "front load inverter")
rep = Refrigirator("LG","French oui oui")
microweyv = Microwave("Hanabishi","digital")

def callme(operating):
    operating.operate()

for appliance in [wasingwasing, rep, microweyv]:
    callme(appliance)