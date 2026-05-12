
#default argument value
def greet(name, message="Hello"):
    """Greet someone with a customizable message"""
    print(f"{message}, {name}!")

# Get user input
name = input("Enter a name to greet: ")
use_default = input("Use default greeting? (yes/no): ").lower()

if use_default == "yes":
    greet(name)
else:
    message = input("Enter custom greeting: ")
    greet(name, message)