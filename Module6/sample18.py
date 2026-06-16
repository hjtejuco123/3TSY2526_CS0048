try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    try:
        file.close()
    except NameError:
        print("No file to close.")