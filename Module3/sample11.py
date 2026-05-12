def square(x):
    """Return the square of x"""
    return x * x

def square_and_add_one(x):
    """Square x and then add one"""
    squared = square(x)
    return squared + 1

# Get user input
num = float(input("Enter a number: "))
result = square_and_add_one(num)
print(f"Square and add one result: {result}")