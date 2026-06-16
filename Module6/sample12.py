try:
    file = open("missing.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File was not found.")