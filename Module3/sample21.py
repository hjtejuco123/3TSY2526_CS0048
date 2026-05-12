def recursive_sum(n):
    """Calculate sum of numbers from 1 to n using recursion"""
    # Base case
    if n <= 0:
        return 0
    # Recursive case
    else:
        return n + recursive_sum(n - 1)

# Get user input
num = int(input("Enter a positive integer to calculate sum from 1 to n: "))
if num < 0:
    print("Please enter a positive integer")
else:
    result = recursive_sum(num)
    print(f"Sum from 1 to {num} is {result}")