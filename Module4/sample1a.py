class Car:
    #brand, model, year, color, price
    def __init__(self, brand, model,year, color, price):
        self.brand = brand
        self.model = model
        self.year = year 
        self.color = color
        self.price = price

    def display(self):
        return f"{self.year} {self.brand} {self.model} ({self.color}) - ${self.price:.2f}"

    def is_expensive(self):
        return self.price > 50000

# User Input
brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = int(input("Enter car year: "))
color = input("Enter car color: ")
price = float(input("Enter car price: "))


# Create Object
my_car = Car(brand, model, year, color, price)
print(my_car.display())

if my_car.is_expensive():
    print("This car is expensive.")
else:    
    print("This car is affordable.")

# User Input
brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = int(input("Enter car year: "))
color = input("Enter car color: ")
price = float(input("Enter car price: "))

my_car2 = Car(brand, model, year, color, price)
print(my_car2.display())

if my_car2.is_expensive():
    print("This car is expensive.")
else:    
    print("This car is affordable.")