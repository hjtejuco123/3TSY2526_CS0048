def find_max(a, b):
    """This function returns the maximum of two numbers"""
    if a > b:
        return a
    else:
        return b

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
max_value = find_max(num1, num2)
print(f"The maximum number is: {max_value}")