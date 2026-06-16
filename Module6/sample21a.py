try:
    age = 20

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age is valid.")

except ValueError as e:
    print("Error:", e)