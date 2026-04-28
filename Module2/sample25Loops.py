# Print numbers from 0 to 4  Basic for loop
# for i in range(5):
#     print(i)


# Print numbers from 0 to 4 using while  Basic while loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# Iterate through a list of fruits
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"I like {fruit}")

# Print even numbers from 0 to 10 Using range() with step
# for num in range(0, 11, 2):
#     print(num)


#WHILE LOOPS
# Simple infinite loop with break condition  Infinite loop with break
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# Simple countdown While Loops
# count = 5
# while count > 0:
#     print(count)
#     count -= 1
# print("Blast off!")

# Keep asking until valid input
password = ""
while password != "python":
    password = input("Enter password: ")
    if password != "python":
        print("Incorrect password, try again")
print("Access granted!")


# Calculate sum of numbers from 1 to n
# n = 10
# total = 0
# i = 1
# while i <= n:
#     total += i
#     i += 1
# print(f"Sum of numbers from 1 to {n} is {total}")


# Calculate factorial of a number
# num = 5
# result = 1
# i = 1
# while i <= num:
#     result *= i
#     i += 1
# print(f"{num}! = {result}")


# While Loops with Else Clause

# Simple while-else example
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print("Loop completed normally")


# While-else with break 
# count = 0
# while count < 5:
#     print(count)
#     if count == 3:
#         print("Breaking the loop")
#         break
#     count += 1
# else:
#     print("This will not be printed")


# Check if a number is prime
# num = 17
# i = 2
# while i * i <= num:
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
#     i += 1
# else:
#     print(f"{num} is a prime number")


# For Loops
# Print each character in a string
# text = "Python"
# for char in text:
#     print(char)


# Print numbers from 5 to 9
# for i in range(5, 10):
#     print(i)


 # Iterate through dictionary items
# student = {"name": "Hadji", "age": 20, "major": "Computer Science"}
# for key, value in student.items():
#     print(f"{key}: {value}")   


# Print list items with their indices List with index using enumerate
# colors = ["red", "green", "blue"]
# for index, color in enumerate(colors):
#     print(f"Color #{index+1}: {color}")


# Create a multiplication table  Nested for loop for multiplication table
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} x {j} = {i*j}", end="\t")
#     print()  # Move to next line after inner loop


# Simple for-else example
# for i in range(5):
#     print(i)
# else:
#     print("Loop completed normally")


# For-else with break (else won't execute)
# for i in range(5):
#     print(i)
#     if i == 3:
#         print("Breaking the loop")
#         break
# else:
#     print("This will not be printed")


# Search for a value in a list
# numbers = [1, 3, 5, 7, 9]
# target = 6

# for num in numbers:
#     if num == target:
#         print(f"Found {target} in the list")
#         break
# else:
#     print(f"{target} not found in the list")


# Check if all numbers are positive
# numbers = [2, 4, 6, 8, 10]

# for num in numbers:
#     if num <= 0:
#         print("Not all numbers are positive")
#         break
# else:
#     print("All numbers are positive")


# Process items until a negative number is found
# numbers = [10, 20, 30, -5, 40, 50]

# for num in numbers:
#     if num < 0:
#         print(f"Negative number {num} found. Stopping processing.")
#         break
#     print(f"Processing {num}")
# else:
#     print("All numbers processed successfully")


# BREAK statement 
# Stop loop when number 5 is found
# for i in range(1, 10):
#     if i == 5:
#         print("Breaking the loop at 5")
#         break
#     print(i)


# Stop while loop when condition met
# count = 1
# while count <= 10:
#     print(count)
#     if count == 7:
#         print("Stopping at 7")
#         break
#     count += 1

# Find first occurrence of letter 'a' in string
# text = "programming"
# for index, char in enumerate(text):
#     if char == 'a':
#         print(f"'a' found at position {index}")
#         break

# Break from inner loop only Nested loops with break

# for i in range(3):
#     print(f"Outer loop {i}")
#     for j in range(3):
#         if j == 1:
#             print("Breaking inner loop")
#             break
#         print(f"  Inner loop {j}")

# Continue Statement

# Print only odd numbers Skip even numbers
# for i in range(1, 10):
#     if i % 2 == 0:  # If even
#         continue
#     print(i)

# Process only positive numbers Skip negative numbers
# numbers = [5, -3, 10, -7, 8, 0, 4]
# for num in numbers:
#     if num <= 0:
#         continue
#     print(f"Processing positive number: {num}")

# Print only consonants Skip vowels in text
# text = "Hello World"
# for char in text:
#     if char.lower() in "aeiou":
#         continue
#     print(char, end="")
# print()  # New line

# Skip processing certain items Skip specific items in list
# items = ["apple", "banana", "orange", "banana", "grape"]
# for item in items:
#     if item == "banana":
#         print(f"Skipping {item}")
#         continue
#     print(f"Processing {item}")


# Pass Statement
# Function to be implemented later  Empty function placeholder
# def process_data(): 
#     pass  #  Implement this function later

# process_data()  # This won't cause an error


# Conditional with placeholder
# user_role = "admin"

# if user_role == "admin":
#     print("Admin access granted")
# elif user_role == "editor":
   
#     pass
# else:
#     print("Guest access")