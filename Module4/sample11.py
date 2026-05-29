#Overloading Comparison Operators

class Product:
    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

# User Input
price1 = float(input("Enter price of product 1: "))
price2 = float(input("Enter price of product 2: "))

p1 = Product(price1)
p2 = Product(price2)
if p1 < p2:
    print("Product 1 is cheaper.")
else:
    print("Product 2 is cheaper or equal.")