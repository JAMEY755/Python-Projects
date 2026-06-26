class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("A dog barks")

s = Dog()
s.sound()