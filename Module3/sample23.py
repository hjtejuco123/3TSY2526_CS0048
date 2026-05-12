# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Lambda function to add two numbers
add = lambda a, b: a + b

result = add(num1, num2)
print(f"{num1} + {num2} = {result}")