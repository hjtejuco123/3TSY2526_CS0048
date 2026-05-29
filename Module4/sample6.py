class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def display(self):
        return f"{self.account_holder}'s balance: {self.balance}"

# User Interaction
accounts = []
for _ in range(2):
    name = input("Enter account holder name: ")
    accounts.append(BankAccount(name))

action = input("Enter 'deposit' or 'withdraw': ").lower()
if action == "deposit":
    for account in accounts:
        amount = float(input(f"Enter deposit amount for {account.account_holder}: "))
        account.deposit(amount)
elif action == "withdraw":
    for account in accounts:
        amount = float(input(f"Enter withdrawal amount for {account.account_holder}: "))
        print(account.withdraw(amount))

print("\nAccount Balances:")
for account in accounts:
    print(account.display())