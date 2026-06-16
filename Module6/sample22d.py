try:
    name = input("Enter your name: ")

    if name.strip() == "":
        raise ValueError("Name cannot be empty.")

    print("Welcome,", name)

except ValueError as e:
    print("Error:", e)