#user inputs 
#input() function
# name = input("Enter your name: ")
# print ("hello", name) 
# print (type(name)) #<class 'str'>
# number = input("Enter a number: ")
# print(type(number)) #<class 'str'>

# int, float, str, bool

# age = int(input("Enter your age: "))
# print ("Your age is:", age)
# print (type(age)) #<class 'int'>

#input with computation 

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sum = num1 + num2
# print("The sum is:", sum)

# a,b = map(int, input("Enter two numbers separated by space: ").split())
# print("The sum is:", a+b)

# #"10 20" -> ["10", "20"] -> [10, 20]

# name, age = input("Enter your name and age separated by space: ").split()
# age = int(age)
# print(f"Hello {name}, you are {age} years old.")
# print (type(name), type(age)) #<class 'str'> <class 'int'>

# name, age, height = input("Enter your name, age and height separated by space: ").split()
# age = int(age)
# height = float(height)
# print(f"Name: {name}, Age: {age}, Height: {height} cm")
# print (type(name), type(age), type(height)) #<class 'str'> <class 'int'> <class 'float'>


#eval() function
result =eval("2+3.3")
print (result) #5
print (type(result)) #<class 'int'>