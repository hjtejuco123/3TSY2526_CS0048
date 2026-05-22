from bank import check_balance, deposit, withdraw

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", check_balance())

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        print("New Balance:", deposit(amount))

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        print("Result:", withdraw(amount))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")