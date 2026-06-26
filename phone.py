class Phone:

 name ="Samsung"
 model="S23 Ultra"

 def __init__(self, storage, camerapixels):
    self.storage=storage
    self.camerapixels=camerapixels

 def display_specs(self):
        return f"{self.name} is {self.model} with {self.storage}GB storage"

 def take_photo(self):
        return f"The photo was taken with {self.camerapixels}MP camera."

phone1=Phone( 256, 200)
print(phone1.storage)
print(phone1.name)
print(phone1.model)
print(phone1.display_specs())
print(phone1.take_photo())