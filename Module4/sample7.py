#Basic Inheritance
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# User Input
choice = input("Enter 'animal' or 'dog': ").lower()
if choice == "animal":
    obj = Animal()
elif choice == "dog":
    obj = Dog()
else:
    obj = None

if obj:
    print(obj.speak())
else:
    print("Invalid choice.")