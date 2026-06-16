try:
    with open("student1.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'student1.txt' does not exist.")

