class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
   
    def describePhone(self):
        print(f"Brand: {self.brand} Model: {self.model}")
       

class Android (Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
       
selpun = Android("Samsong" ,"Abc123")
selpun.describePhone()