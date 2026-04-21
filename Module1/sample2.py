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

a,b = map(int, input("Enter two numbers separated by space: ").split())
print("The sum is:", a+b)

#"10 20" -> ["10", "20"] -> [10, 20]