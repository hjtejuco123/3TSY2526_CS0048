import bank.account as account

def deposit(amount):
    account.balance += amount
    return account.balance

def withdraw(amount):
    if amount > account.balance:
        return "Insufficient balance"
    account.balance -= amount
    return account.balance