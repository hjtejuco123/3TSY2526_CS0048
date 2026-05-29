class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Sales:
    def sell(self, item):
        return f"Selling {item}."

class Store(Inventory, Sales):
    def show_inventory(self):
        return f"Inventory: {', '.join(self.items)}"

# User Interaction
store = Store()
while True:
    action = input("Enter 'add', 'sell', or 'show': ").lower()
    if action == "add":
        item = input("Enter item to add: ")
        store.add_item(item)
    elif action == "sell":
        item = input("Enter item to sell: ")
        print(store.sell(item))
    elif action == "show":
        print(store.show_inventory())
    else:
        break