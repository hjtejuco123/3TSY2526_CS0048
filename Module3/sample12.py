def power(base, exponent):
    """Calculate base raised to the power of exponent"""
    return base ** exponent

# Get user input
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
result = power(base, exponent)
print(f"{base} raised to {exponent} is {result}")