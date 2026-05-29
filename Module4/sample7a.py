#Basic Inheritance
class Animal:
    def __init__(self,species):
        self.species = species

    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def speak(self):
        return super().speak() + " - Woof!"

#create object 
dog = Dog("Mammal", "Labrador")
print(dog.species)
print(dog.breed)
print(dog.speak())