# ============================================================
# Sharleen Guerrero
# May 6, 2026
# Notes: User Input, Type Casting, and Format Specifiers
# ============================================================


# (Quick Check) -----------------------------------------------

# Write a Python program that accepts three numbers from a user
# and outputs the average of the three numbers with two decimal
# places. The program should also accept and display the user's
# name using f-string formatting.
# Use the inputs of 15, 25, and 5 for manual testing.

name = input("Enter your name: ") # input() always returns a string
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
num3 = eval(input("Enter third number: "))
# eval auto-detects the type (int, float, etc.) and conversts accordingly

average = (num1 + num2 + num3) / 3

print(f"Hello {name}! The average of {num1:.0f}, {num2:.0f} and {num3:.0f} is: {average:.2f}")

# Output (manual test: 15, 25, 5)
# Enter your name: Sharleen
# Enter first number: 15
# Enter second number: 25
# Enter third number: 5
# Hello Sharleen! The average of 15, 25 and 5 is: 15.00


# Type Casting Examples ------------------------------------------

# type casting = converting a value from one data type to another
# type() checks the current data type of a variable
# int(), float(), str() are the main casting functions

num1 = 10
print(type(num1))          # <class 'int'>
print(type(str(num1)))     # <class 'str'>  -- cast int to string

num2 = '25'
print(type(num2))          # <class 'str'>
print(type(int(num2)))     # <class 'int'>  -- cast string to int

print(type(float(num2)))   # <class 'float'> -- cast string to float
print(float(num2))         # 25.0

# round(value, decimal_places) changes the actual value (not just display)
num3 = 3.14569
print(round(num3, 2))      # 3.15


# Multiple Inputs on One Line --------------------------------------

# Write a program that accepts the length and width of a rectangle
# on one line and calculates the area and perimeter.

length, width = input("Enter the length and width of the rectangle: ").split()
length = float(length)
width = float(width)
# .split() separates one input string into multiple variables at once

area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle is {area:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")


# Discount Calculator ----------------------------------------

# Create a Python program that calculates the discounted price of an item.
# The program should:
# Prompt the user to enter the original price and the discount percentage
# Calculate the final price after applying the discount
# Display the result using an f-string, formatted to 2 decimal place

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

discount_amount = price * (discount_percent / 100) # Divide by 100 to convert percentage to decimal
final_price = price - discount_amount

print(f"Final Price = ${final_price:.2f}")


# Alignment with Format Specifiers ---------------------------

# Write a program that displays the following months and their
# values aligned in columns using format specifiers.

January  = 12345
February = 28123.678
March    = 3112323.8976
April    = 301234.678

print(f"{'January':<15}{January:>15,.2f}")
print(f"{'February':<15}{February:>15,.2f}")
print(f"{'March':<15}{March:>15,.2f}")
print(f"{'April':<15}{April:>15,.2f}")
# format specifiers go inside {} in an f-string after a colon
# two parts: alignment + width, and number format
# TEXT alignment:
# :<15  left-align the text, padded to 15 characters wide
# :>15  right-align the text, padded to 15 characters wide
# NUMBER format:
#  ,    adds comma separators (1000 -> 1,000)
# .2f   rounds to 2 decimal places and treats as float
# Combined: :>15,.2f
# right-align in 15-character space, with commas, 2 decimal places
# this makes columns line up neatly like a table

# output:
# January           12,345.00
# February          28,123.68
# March          3,112,323.90
# April            301,234.68


# Meal Cost Calculator ---------------------------------------
# Write a Python program that calculates the total cost of a meal.
# The program should:
# Prompt the user to enter the cost of the meal
# Calculate the tip as 20% of the meal cost
# Calculate the tax as 8.25% of the meal cost
# Compute the total cost (meal cost + tip + tax)
# Display all values using f-strings, formatted to 2 decimal places and properly aligned
# Use <15 to left-align labels and >6.2f to right-align numbers

meal_cost = float(input("Enter the cost of the meal: $ "))

tip = meal_cost * 0.20
tax = meal_cost * 0.0825
total_cost = meal_cost + tip + tax

print(f'---------------- Meal Cost Breakdown ------------------')
print(f"{'Meal Cost:':<15} ${meal_cost:>6.2f}")
print(f"{'Tip (20%):':<15} ${tip:>6.2f}")
print(f"{'Tax (8.25%):':<15} ${tax:>6.2f}")
print(f"{'Total Cost:':<15} ${total_cost:>6.2f}")
# :<15 left-aligns the labels, :>6.2f right-aligns the dollar amounts