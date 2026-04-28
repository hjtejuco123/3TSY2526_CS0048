# Assign value based on condition in one line
# Sample 24: Using nested ternary operators to determine weather status (Conditional assignment)
temperature = 19
status = "hot" if temperature > 30 else "warm" if temperature > 20 else "cool"
print(f"Today's weather is {status}")