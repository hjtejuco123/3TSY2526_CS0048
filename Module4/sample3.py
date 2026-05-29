class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def evaluate(self):
        if self.grade >= 90:
            return f"{self.name} got an A!"
        elif self.grade >= 75:
            return f"{self.name} got a B."
        else:
            return f"{self.name} needs improvement."

# User Input
name = input("Enter student name: ")
grade = int(input("Enter student grade: "))

student = Student(name, grade)
print(student.evaluate())