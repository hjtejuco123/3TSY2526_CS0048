#if with open() is used, the file will be automatically 
# closed after the block of code is executed, even if an error occurs.
# This ensures that resources are properly managed and prevents 
# potential issues with file handling.
with open("notes2.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("This file was created using with open().")

print("File created successfully.")