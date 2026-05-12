def validate_age(age):
    """Validate if age is within acceptable range"""
    if age < 0:
        return "Error: Age cannot be negative"
    elif age > 120:
        return "Error: Age seems unrealistically high"
    else:
        return "Age is valid"

# Get user input
age = int(input("Enter your age: "))
result = validate_age(age)
print(result)