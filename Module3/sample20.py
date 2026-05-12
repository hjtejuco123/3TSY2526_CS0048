def fibonacci(n):
    """Calculate nth Fibonacci number using recursion"""
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get user input
n = int(input("Enter which Fibonacci number to calculate (0-based index): "))
if n < 0:
    print("Please enter a non-negative integer")
else:
    result = fibonacci(n)
    print(f"Fibonacci number at position {n} is {result}")