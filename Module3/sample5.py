def factorial(n):
    """This function calculates factorial of a number iteratively"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input
num = int(input("Enter a positive integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = factorial(num)
    print(f"Factorial of {num} is {fact}")