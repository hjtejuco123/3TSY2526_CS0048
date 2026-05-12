def factorial(n):
    """Calculate factorial using recursion"""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Get user input
num = int(input("Enter a non-negative integer to calculate factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = factorial(num)
    print(f"{num}! = {result}")