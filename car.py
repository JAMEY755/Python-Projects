class Car:
    def __init__(self, brand , model, price):
        self.brand=brand
        self._model=model
        self.__price=price

    def display_details(self):
        print(f"Brand (Public):     {self.brand}")
        print(f"Model (Protected):   {self._model}")
        print(f"Price (Private):     ${self.__price:,}")

car1=Car("Mazda", "T1", 30000)
car1.display_details()