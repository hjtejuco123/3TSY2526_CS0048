#Polymorphism
class Bird:
    def fly(self):
        return "Bird can fly."

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly."

def flying_test(bird):
    print(bird.fly())

# User Input
choice = input("Enter 'bird' or 'penguin': ").lower()
if choice == "bird":
    obj = Bird()
elif choice == "penguin":
    obj = Penguin()
else:
    obj = None

if obj:
    flying_test(obj)
else:
    print("Invalid choice.")