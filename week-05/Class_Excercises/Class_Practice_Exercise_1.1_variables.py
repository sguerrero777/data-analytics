# =======================================================
# Python Fundamentals
# Variables, Arithmetic Operators & Reflection Exercises
# Sharleen Guerrero
# =======================================================

# =============================================================
# PART 2 — GUIDED EXERCISES
# =============================================================

# ---------------------------------------------------------------
# Exercise 1 — Declaring Variables & Basic Addition
# ---------------------------------------------------------------

number1 = 12
number2 = 8
sum_result = number1 + number2

print(sum_result)
print(type(sum_result))

# Output:
# 20
# <class 'int'>

# Reflection:
# What value was displayed? Is it what you expected?
# The value displayed was 20. It was expected because 12 + 8 = 20.

# What does type() tell you about sum_result? Why does that matter?
# Type() tells me that the result is an integer. It matters because it can
# help avoid unexpected results. For instance, if Python sees two numbers as 
# strings, instead of performing math, it'd just concatenate them.

# What happens if you change number1 = 12.0? Does the output change?
# If you change number1 to 12.0, the output changes to a float.

# ---------------------------------------------------------------
# Exercise 2 — Subtraction & Updating Variables
# ---------------------------------------------------------------

initial_value = 25
reduction = 11
difference = initial_value - reduction
print(difference)

initial_value -= 5 
print(initial_value)

initial_value += 10 
print(initial_value)

counter = 50

counter += 8
print(counter)

counter -= 3
print(counter)

# Output:
# 14
# 20
# 30
# 58
# 55

# Reflection:
# What is the difference between initial_value = initial_value - 5 and initial_value -= 5?
# Although they achieve the same result, the difference is that initial_value -= 5 is a 
# more concise way of formatting.

# In what real-life programs might you need to increment or decrement a variable repeatedly?
# Scenarios in where I might need to increment or decrement a variable repeatedly are during
# calculating a students gpa, it can go up or down.

# What happens if you try: 25 - 'five'? What error appears, and why?
# If I try 25 - 'five', I'll get and error that says unsupported operand type
# because 25 is an integer and 'five' is a string. To perform math, I'd have to
# convert 'five' to an integer.

# ---------------------------------------------------------------
# Exercise 3 — Multiplication & Order of Operations
# ---------------------------------------------------------------

x = 5
y = 2
z = 3

result_a = x * y + z
print(result_a)

result_b = x * (y + z)
print(result_b)

multiplier = 7
multiplicand = 9
product = multiplier * multiplicand
print(product)

item_price = 3.75
quantity = 5
total_cost = item_price * quantity
print(total_cost)

# Output:
# 13
# 25
# 63
# 18.75

# Reflection:
# Why are result_a and result_b different even though they use the same values?
# The result for result_a and result_b is different because of the precedence of
# the operations. Although in result_a multiplication takes precedence, in result_b
# the addition of y + z takes precedence because it's inside of parentheses.

# In a real shopping app, why is it important that multiplication happens before addition?
# In a shopping app, it's important that multiplication happens before addition to ensure that
# the appropiate items are calculated to their corresponding price before being added to the 
# subtotal.

# What would happen if Python evaluated operators strictly left-to-right with no precedence rules?
# If Python evaluated operators strictly left-to-right with no precedence rules, there would be errors
# in calculating data, because precedence is law in mathematics. 

# ---------------------------------------------------------------
# Exercise 4 — Division, Integer Division & Modulo
# ---------------------------------------------------------------

numerator = 30
denominator = 6

print(numerator / denominator)
print(numerator // denominator)

denominator = 7

value = 19
modulus = 4

remainder_val = value % modulus
print(remainder_val)

print(20 % 2)
print(21 % 2)

print(100 // 60)
print(100 % 60)

# Output:
# 5.0
# 5
# 3
# 0
# 1
# 1
# 40

# Reflection:
# When would you choose // over /? Give a concrete programming example.
# I would choose // over / when I need to do floor division, or in other 
# words when I need a rounded result with no decimals. For example, if 
# I wanted to calculate how many vans I need to fit a group of people.

# How could you use % to check if a number is even or odd in a program?
# I could use % to check if a number is even or odd in a program by diving by two.
# If the result gives no remainder, its even and if it gives a remainder, it's
# add. 

# What result does 0 % 5 give? What about 5 % 5? Can you form a rule?
# # 0 % 5 = 0 because 0 divided by 5 has no remainder.
# 5 % 5 = 0 because 5 divided by 5 = 1 exactly with no remainder.
# The rule is that, when a number divides evenly, the remainder is always 0.

# ---------------------------------------------------------------
# Exercise 5 — Exponents & Geometric Calculations
# ---------------------------------------------------------------

base_num = 3
power_num = 3
exponent_result = base_num ** power_num
print(exponent_result)

length = 15
width = 8
rectangle_area = length * width
print(rectangle_area)

rectangle_perimeter = 2 * (length + width)
print(rectangle_perimeter)

radius = 7
pi = 3.14159
circle_area = pi * radius ** 2
print(circle_area)

radius = 5
circle_area = pi * radius ** 2
print(circle_area)

area_difference = rectangle_area - circle_area
print(area_difference)

# Output:
# 27
# 120
# 46
# 153.938...
# 78.53975
# 41.46...

# Reflection:
# Why do we store pi as a variable instead of typing 3.14159 every time?
# We store pi as a variable to avoid redundancy

# What does radius ** 2 compute? Why is the exponent applied before the multiplication by pi?
# If radius = 7, radius ** 2 computes 49. The exponenet is applied before the multiplication
# because of precedence ruling.

# How could you modify the circle formula to compute circumference instead of area?
# To computer circumference instead of area, I can modify the formula by removing the
# exponentation and instead multiplying the product of pi and radius by 2.

# ---------------------------------------------------------------
# Exercise 6 — Combining All Operators — Challenge
# ---------------------------------------------------------------

print(2 + 3 * 4 - 1)
print((2 + 3) * (4 - 1))
print(17 // 3 + 17 % 3)
print(2 ** 4 / 4 + 1)

base_amount = 10
final_amount = base_amount * 2 - 7
print(final_amount)

# Output:
# 13
# 15
# 7
# 5.0
# 13

# Reflection:
# Describe in plain English what 17 // 3 + 17 % 3 is actually calculating.
# 17 // 3 divides 17 by 3 and returns the quotient (5)
# 17 % 3 divides 17 by 3 and returns the remainder (2)
# added together: 5 + 2 = 7
# it is adding the quotient and the remainder of 17 divided by 3

# Write a single Python expression that computes the area of a ring (radius 7 and radius 3):
# area = 3.14159 * (7**2 - 3**2)

# =============================================================
# PART 3 — EXTENDED REFLECTION
# =============================================================

# Q1: In your own words, explain what a variable is and why programmers use them.
# A variable is a name that stores a value. Programmers use it to avoid redundancy 
# in typing out the value numerous times. 

# Q1: In your own words, explain what a variable is and why programmers use them.
# A variable is a name that stores a value. Programmers use it to avoid redundancy
# in typing out the value numerous times.

# Q2: Describe a situation where each of the seven arithmetic operators would be useful.
# Addition: Finding the sum of prices for items.
# Subtraction: Calculating someone's net worth; subtracting assets from liabilities.
# Multiplication: Finding the cost for items with the same price.
# Division: Calculating how much each person owes on a bill.
# Integer Division: Calculating how many vans someone would need to fit a certain amount of people.
# Modulo: Checking if a number is even or odd — if num % 2 == 0, it's even.
# Exponent: Calculating the area of a square or circle using a radius or side length.

# Q3: What is operator precedence, and why does Python need it?
# Operator precedence is the order in which Python evaluates operations in an expression.
# Python needs it so that every expression has one predictable result.

# Q4: Explain the difference between / and //. When would a programmer choose one over the other?
# / returns the full decimal result 
# // returns only the whole number, dropping the decimal. It essentially rounds down 
# A programmer uses / when exact precision matters, like splitting a bill.
# A programmer uses // when only whole units matter, like how many vans are needed.

# Q5: How do += and -= improve code readability and reduce mistakes?
# Instead of writing score = score + 1, you can write score += 1.
# It's shorter, easier to read, and reduces the chance of accidentally
# referencing the wrong variable on the right side.

# Q6: Reflect on predicting output before running code in Exercise 6.
# Predicting output before running forces you to actually think through the logic
# instead of just reading the code passively. If your prediction is wrong, 
# it tells you exactly where your understanding broke down, which is more
# valuable than just running it and moving on.

# =============================================================
# PART 4 — EXTENSION CHALLENGES 
# =============================================================

# ---------------------------------------------------------------
# Challenge A — Temperature Converter
# ---------------------------------------------------------------

fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.2f}°C")
# Output: 98.6°F = 37.00°C

# ---------------------------------------------------------------
# Challenge B — Pizza Party
# ---------------------------------------------------------------

slices = 8
people = 6
slices_per_person = slices // people
leftover_slices = slices % people
print(f"Each person gets {slices_per_person} slice(s).")
print(f"Leftover slices: {leftover_slices}")
# Output: Each person gets 1 slice(s).
# Output: Leftover slices: 2

# ---------------------------------------------------------------
# Challenge C — Compound Interest
# ---------------------------------------------------------------

principal = 1000
rate = 0.05
years = 3
amount = principal * (1 + rate) ** years
print(f"After {years} years, the amount is ${amount:.2f}")
# Output: After 3 years, the amount is $1157.63