#syntax

# lambda arg:expression

# Get user input
num = float(input("Enter a number to square: "))

# Lambda function to square a number
square = lambda x: x * x

result = square(num)
print(f"The square of {num} is {result}")