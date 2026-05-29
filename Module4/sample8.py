#Using Arrays in Inheritance

class Vehicle:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

class Car(Vehicle):
    def show_parts(self):
        return f"Car parts: {', '.join(self.parts)}"

# User Interaction
car = Car()
while True:
    part = input("Add car part (or type 'done'): ")
    if part.lower() == 'done':
        break
    car.add_part(part)
print(car.show_parts())