class Class1:
    def w(self):
        print("Method from Class 1")

class Class2(Class1):
    def w(self):
        print("Method from Class 2")

class Class3(Class1):
    def w(self):
        print("Method from Class 3")

class Class4(Class2, Class3):
    pass


print(Class4.__mro__)
obj = Class4()
obj.w()