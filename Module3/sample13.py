
x = 10  # Global variable

def modify_variable():
    x = 20  # Local variable, different from the global x
    print(f"Inside function, x = {x}")

# Get user input
print(f"Before function call, global x = {x}")
user_input = input("Press Enter to call the function...")
modify_variable()
print(f"After function call, global x = {x}")