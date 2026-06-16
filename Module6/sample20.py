try:
    grade = int(input("Enter grade: "))
except ValueError:
    print("Invalid grade.")
else:
    print("Your grade is", grade)
finally:
    print("End of program.")