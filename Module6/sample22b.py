try:
    name = input("Enter your name: ")

    if name.strip() == "":
        raise Exception("Name cannot be empty.")

    print("Welcome,", name)

except Exception as e:
    print("Error:", e)