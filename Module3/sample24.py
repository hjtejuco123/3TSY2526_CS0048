# Get user input
num = float(input("Enter a number: "))
is_positive = (lambda x: x > 0)(num)

print(f"\nIs {num} positive? {is_positive}")

# Another example with if-else
result = (lambda x: "Positive" if x > 0 else "Non-positive")(num)
print(f"{num} is {result.lower()}")