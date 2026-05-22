from reservation import add_reservation, view_reservations

while True:
    print("\n===== RESERVATION SYSTEM =====")
    print("1. Add Reservation")
    print("2. View Reservations")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        date = input("Enter reservation date: ")
        print(add_reservation(name, date))

    elif choice == "2":
        records = view_reservations()

        if not records:
            print("No reservations yet.")
        else:
            for r in records:
                print(f"Name: {r['name']} | Date: {r['date']}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")