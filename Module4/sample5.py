class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} works as a {self.role}."

# User Input
employees = []
while len(employees) < 3:
    name = input("Enter employee name: ")
    role = input("Enter employee role (Manager/Developer): ").capitalize()
    if role not in ["Manager", "Developer"]:
        print("Invalid role. Try again.")
        continue
    employees.append(Employee(name, role))

print("\nEmployee Details:")
for emp in employees:
    print(emp.describe())