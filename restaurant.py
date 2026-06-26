class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"{self.restaurant_name} serves {self.cuisine_type} meals."
    
    def open_restaurant(self):
        return f"{self.restaurant_name} is open now."
    

restaurant1 = Restaurant("Magnus Cafe", "Italian")
restaurant2 = Restaurant("Protea", "Mexican")
restaurant3 = Restaurant("Nice Bites", "American")

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
print(restaurant1.describe_restaurant())
print(restaurant1.open_restaurant())
print(restaurant2.restaurant_name)
print(restaurant2.cuisine_type)
print(restaurant2.describe_restaurant())
print(restaurant2.open_restaurant())
print(restaurant3.restaurant_name)
print(restaurant3.cuisine_type)
print(restaurant3.describe_restaurant())
print(restaurant3.open_restaurant())
