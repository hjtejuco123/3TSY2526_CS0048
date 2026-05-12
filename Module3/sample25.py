# Get user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Lambda with multiple arguments
calculate = lambda x, y, z: x * y + z

result = calculate(a, b, c)
print(f"\nCalculation result ({a} * {b} + {c}): {result}")

# Another example: find maximum of three numbers
max_three = lambda x, y, z: max(x, max(y, z))
maximum = max_three(a, b, c)
print(f"Maximum of the three numbers: {maximum}")