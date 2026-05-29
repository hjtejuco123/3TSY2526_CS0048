class ShoppingCart:
    #constructor
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Cart Items:", ", ".join(self.items))

# User Interaction
cart = ShoppingCart()
while True:
    item = input("Add item to cart (or type 'exit'): ")
    if item.lower() == 'exit':
        break
    cart.add_item(item)
cart.show_cart()