# Simple login system with username and password check Nested If Statements
# Sample 16: Simple login system with nested if statements
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful! Welcome admin.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")