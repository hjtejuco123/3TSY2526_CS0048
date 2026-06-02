class Student:
    def __init__(self, name, course, grade):
        self.name = name        #Public 
        self._course = course   #Protected
        self.__grade = grade    #Private

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        self.__grade = grade
    
    def display(self):
        print(f"Name: {self.name}, Course: {self._course}, Grade: {self.__grade}")

student = Student("Hadji", "Math", "A")

print(student.name)          # Accessing public attribute
print(student._course)      # Accessing protected attribute (not recommended)
# print(student.__grade)    # This will raise an AttributeError
print(student.get_grade())  # Accessing private attribute via getter method


student.set_grade("A+")          # Accessing private attribute via method
print(student.get_grade())  # Accessing private attribute via getter method
