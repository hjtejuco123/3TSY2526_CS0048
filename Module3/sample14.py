total = 0  # Global variable

def add_to_total(value):
    global total
    total += value
    print(f"Inside function, total = {total}")

# Get user input
print(f"Initial global total = {total}")
value1 = float(input("Enter first value to add: "))
add_to_total(value1)
value2 = float(input("Enter second value to add: "))
add_to_total(value2)
print(f"Final global total = {total}")