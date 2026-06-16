try:
    with open("output.txt", "w") as file:
        file.write("Data saved successfully.")
except IOError:
    print("Writing failed.")
else:
    print("File written successfully.")