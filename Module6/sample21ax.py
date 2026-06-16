
try:
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative.")
        #print ("Age cannot be negative.")  
except ValueError as e:
    print(e)


