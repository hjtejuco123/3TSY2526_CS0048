# Movie ticket pricing based on age Sample 14: Movie ticket pricing based on age
age = 12
if age <= 5:
    price = 0
    print(f"Child (age {age}): Free admission")
elif age <= 12:
    price = 8
    print(f"Child (age {age}): ${price} ticket")
elif age <= 18:
    price = 10
    print(f"Teen (age {age}): ${price} ticket")
elif age >= 65:
    price = 9
    print(f"Senior (age {age}): ${price} ticket")
else:
    price = 12
    print(f"Adult (age {age}): ${price} ticket")