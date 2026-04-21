# This is a simple Python script

#print statement 
# print ("Hello, World!")

#printing variables
# name = "Alice"
# age = 20
# print (name, age)
# print (f"{name} is {age} years old.")
# print ("Name:", name, "Age:", age)

#print with separators
# print ("Apple","Banana","Cherry", sep=" | ")

#end statement
# print ("Hello", end=" ")
# print ("World!")

# print ("hello\nworld")

#printing List 
# fruits = ["Apple", "Banana", "Cherry"]
# print (fruits)
# numbers = [1, 2, 3, 4, 5]
# print (numbers)

#print values 
# print (5+3)
# print ("sum", 5+3)


#print formatting  
#f - formatted string literals

#print(f"text {var}")

# name = "Alice"
# age = 23
# print (f"My name is, {name} and i am {age} years old.")
# a=5
# b=10
# print (f"The sum of {a} and {b} is {a+b}.")
# pi = 3.14159
# print (f"The value of pi is approximately {pi:.2f}.")
# num  = 7 
# print (f"The number is {num:03d}.")

# text = "Hi"
# print (f"{text:<10}") # left align
# print (f"{text:>10}") # right align
# print (f"{text:^10}") # center align

# score = 0.85
# print (f"Your score is {score:.2%}")
# print (f"Your score is {score:.0%}")

# age = 18
# print (f"Status: {'Adult' if age >= 18 else 'Minor'}")

# number = 1000000
# print (f"The number is {number:,}")
# print (f"The number is {number:,.2f}")

#dates 
from datetime import datetime
today = datetime.now()
#Y - 2026, y - 26
#m - 01
#b - Jan
#B - January
#d - 01
#j - 001
#a - Mon
#A - Monday
#print (f"Today's date is {today:%Y-%B-%d}")

print (f"Year: {today:%Y}")
print (f"Month: {today:%B}")
print (f"Day: {today:%d}")
print (f"Day of the year: {today:%j}")
print (f"Weekday: {today:%A}") 
print (f"Full date: {today:%Y-%B-%d}") 

#time 
#H - 00-23
#I - 01-12
#p - AM/PM
#M - 00-59
#S - 00-59
print (f"Current time is {today:%H:%M:%S%p}")

# single line comment
'''
multi line comment

'''