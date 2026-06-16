try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
     print("Please enter a valid number.")