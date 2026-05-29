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

class Cat(Animal):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

    def speak(self):
        return super().speak() + " - Meow!"

#create object 
dog = Dog("Mammal", "Labrador")
cat = Cat("Mammal", "Orange")

print(dog.species)
print(dog.breed)
print(dog.speak())

print(cat.species)
print(cat.color)
print(cat.speak())