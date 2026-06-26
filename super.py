class Vehicle:

    def __init__(self, name):
        self.name = name

    def info(self):
        print("Vehicle name:", self.name)

class Car(Vehicle):
    
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def details(self):
        print(self.name, "is a", self.model, "car")

        self.model = model

    def details(self):
        print(self.name, "is a", self.model, "car")
        print(f"{self.name} is a {self.model} car")


z = Car("Toyota", "Harrier")
z.info()  
z.details()  