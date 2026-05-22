from .records import students

def add_student(name, grade):
    students.append({"name": name, "grade": grade})
    return "Student added successfully"

def view_students():
    return students

def get_status(grade):
    if grade >= 75:
        return "Passed"
    else:
        return "Failed"