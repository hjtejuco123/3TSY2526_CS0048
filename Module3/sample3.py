def check_even_odd(num):
    """This function checks if a number is even or odd"""
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Get user input
number = int(input("Enter an integer: "))
result = check_even_odd(number)
print(f"{number} is an {result} number")