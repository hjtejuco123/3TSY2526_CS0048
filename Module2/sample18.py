# Restaurant seating arrangement Sample 18: Restaurant seating arrangement using nested if statements
party_size = 5
is_reservation = True
is_weekend = True
 
if is_reservation:
    if party_size <= 4:
        print(f"Your table for {party_size} is ready in section A")
    elif party_size <= 6:
        print(f"Your table for {party_size} is ready in section B")
    else:
        print("We'll need to check for larger tables")
elif is_weekend:
    print("We're fully booked for walk-ins today")
else:
    print("We can seat you in 15 minutes")