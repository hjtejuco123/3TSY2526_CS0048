student_name = input("Enter Student Name: ")
course = input("Enter Course: ")

with open("student_info.txt", "w") as file:
    file.write("Student Information\n")
    file.write("-------------------\n")
    file.write("Name: " + student_name + "\n")
    file.write("Course: " + course)

print("Student information saved successfully!")