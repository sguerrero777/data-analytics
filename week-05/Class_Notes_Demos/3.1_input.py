# ============================================================
# Sharleen Guerrero
# May 5, 2026
# Notes: User Input in Python with Examples
# ============================================================


# input() always returns a string, no matter what the user types
# you must type cast if you need to do math with the input

name = input("Enter your name: ")
print(f"Hello {name}")


# Input with Two Numbers -------------------------------------

# Ask the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print(f'You have entered {num1} and {num2}')

# type() shows us what data type a variable is
print(type(num1))
print(type(num2))

# Type Casting: String to Float ------------------------------
# input() gives us strings, so we cast to float before doing math
# float() converts a string like "3" into a number like 3.0
num1 = float(num1)
num2 = float(num2)

print(f'The sum of {num1} and {num2} is {num1+num2}')
print(f'The product of {num1} and {num2} is {num1*num2}')
print(f'The product of 2 and {num2} is {2*num2}')

# Errors Explained -------------------------------------------
# 1. input() always returns a string, so type() shows <class 'str'>
# 2. The sum line: "3" + "4" = "34" is string concatenation, not addition
# 3. The product line: Python can't multiply two strings together
# 4. The last line: Python can't multiply an int by a string
# Fix: cast num1 and num2 to float() before doing any math
# use int() for whole numbers, float() for decimals


# Type Casting Demo ------------------------------------------

# Int to String
num1 = 10
print(type(num1))           
# output: <class 'int'>
print(type(str(num1)))      
# output: <class 'str'> -- converted int to string

# String to Int
num2 = '25'
print(type(num2))           # output: <class 'str'>
print(type(int(num2)))      # output: <class 'int'> -- converted string to int


# Mixed Type Expression --------------------------------------
# When an operation is performed on two int values, the result will be an int.
# When an operation is performed on two float values, the result will be a float.
# When an operation is performed on an int and a float, the int value will be
# temporarily converted to a float and the result of the operation will be a float.


# Multiple Inputs on One Line --------------------------------
# .split() cuts the input into pieces wherever it sees a space
# it returns a list of strings, so we still need to cast to float

length, width = input("Enter the length and width of the rectangle: ").split()

# .split() returns strings so we need to cast to float for math to work
length = float(length)
width = float(width)

area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle is {area:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")


# Temperature Conversion -------------------------------------
# Formula: F = (9/5) * C + 32

celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (9/5) * celsius + 32

print(f"Fahrenheit = {fahrenheit:.2f}")


# Discounted Price Calculator --------------------------------
# Formula: discount amount = (discount percent / 100) * price
# final price = price - discount amount

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

discount_amount = (discount_percent / 100) * price
final_price = price - discount_amount

print(f"Final Price = ${final_price:.2f}")