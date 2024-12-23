class Spiderman():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print(f"ako si {self.name}, {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
n1 = Tobey("tobey", 49, "spiderman 1" )
print(n1.name.upper(), n1.movie_title)

class Andrew(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
n2 = Andrew("Andrew", 41, "spiderman 2" )
print(n2.name.upper(), n2.movie_title)

class Tom(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
n3= Tom("tom", 28, "spiderman no home")
print(n3.name.upper(),n3.movie_title) 