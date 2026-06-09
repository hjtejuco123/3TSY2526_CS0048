student = {"name": "Bob", "age": 20, "grade": "A"}
print(student["name"])          # Bob
print(student.get("age"))       # 20
print(student.get("phone", "N/A"))  # N/A (avoids KeyError)