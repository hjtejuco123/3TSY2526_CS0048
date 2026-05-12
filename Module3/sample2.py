def square(num):
    """This function returns the square of a number"""
    return num * num

# Get user input
number = float(input("Enter a number to square: "))
result = square(number)
print(f"The square of {number} is {result}")