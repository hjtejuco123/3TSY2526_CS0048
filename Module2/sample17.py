# Check eligibility for a competition Sample 17: Nested if statements for eligibility check
age = 22
has_qualification = False

if age >= 18:
    if has_qualification:
        print("You are eligible to participate!")
    else:
        print("You need the required qualification to participate.")
else:
    print("You must be at least 18 years old to participate.")