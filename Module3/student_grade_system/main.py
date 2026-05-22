from grades import add_student, view_students, get_status

while True:
    print("\n===== STUDENT GRADE SYSTEM =====")
    print("1. Add Student Grade")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        print(add_student(name, grade))

    elif choice == "2":
        students = view_students()

        if not students:
            print("No student records yet.")
        else:
            for s in students:
                status = get_status(s["grade"])
                print(f"Name: {s['name']} | Grade: {s['grade']} | Status: {status}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")