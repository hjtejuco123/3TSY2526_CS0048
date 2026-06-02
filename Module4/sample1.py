class Car:
    #constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"{self.brand} {self.model}"

# User Input
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create Object
my_car = Car(brand, model)
print(my_car.display())

# User Input
brand = input("Enter car brand: ")
model = input("Enter car model: ")

my_car2 = Car(brand, model)
print(my_car2.display())