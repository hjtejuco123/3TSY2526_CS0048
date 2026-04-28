# Simple loan approval system Sample 19: Loan approval system with nested if statements
credit_score = 650
income = 60000
loan_amount = 200000

if credit_score >= 700:
    if income >= 50000:
        if loan_amount <= income * 4:
            print("Loan approved!")
        else:
            print("Loan amount too high relative to income")
    else:
        print("Income too low for loan approval")
else:
    print("Credit score too low for loan approval")