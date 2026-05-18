# ============================================================
# Notes: Functions, Parameters, Arguments, Strings, and Range
# Sharleen Guerrero
# May 12, 2026
# ============================================================


# ============================================================
# SECTION 1: Function with NO parameters
# The function handles everything internally — input is
# collected inside the function, not passed in from outside.
# ============================================================

def greeting():
    name = input("Please enter your name: ")
    return name          # return hands the value back to the caller

result = greeting()
print(f"Hello, {result}!")


# ============================================================
# SECTION 2: Function WITH parameters — returning multiple values
# When you return multiple values separated by commas,
# Python automatically packs them into a TUPLE.
#
# Tuple ()  — immutable: you can read it but not change it
# List  []  — mutable: you can add, remove, or change items
#
# Python uses a tuple for multiple returns because the values
# coming back from a function are meant to be read, not modified.
# ============================================================

def greeting(name, city, hobby):
    return name, city, hobby     # Python packs these into a tuple automatically

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(type(result))              # confirms: <class 'tuple'>

# Access each value by its index position (starts at 0)
print(f'Hello, {result[0]}! You are from {result[1]} and you enjoy {result[2]}.')


# ============================================================
# SECTION 3: Unpacking a tuple into separate variables
# Instead of accessing values by index (result[0], result[1]...),
# you can unpack them directly into named variables.
# Much cleaner and more readable!
# ============================================================

def greeting(name, city, hobby):
    return name, city, hobby

# Unpacking: each variable on the left catches one returned value
name, city, hobby = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(f"Hello, {name}! You are from {city} and you enjoy {hobby}.")


# ============================================================
# SECTION 4: Return a single formatted string
# Instead of returning raw values and formatting outside,
# build the full message inside the function and return it
# as one clean string.
# ============================================================

def greeting(name, city, hobby):
    return f"Hello, {name}! You are from {city} and you enjoy {hobby}."

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(result)


# ============================================================
# SECTION 5: Default parameters (keyword parameters)
# Default parameters make arguments optional at call time.
# If no value is passed, Python uses the default.
# RULE: parameters WITH defaults must come AFTER required ones.
# ============================================================

def greeting(name="Unknown", hobby="nothing", city="New York"):
    return f"Hello, {name}! You are from {city} and you enjoy {hobby}."

# Call 1 — no arguments passed, all defaults used
result1 = greeting()
print(result1)

# Call 2 — only name provided, city and hobby use defaults
result2 = greeting(name="Alice")
print(result2)

# Call 3 — all three provided, all defaults overridden
result3 = greeting(name="Alice", hobby="hiking", city="Brooklyn")
print(result3)

# Call 4 — user supplies all three values via input()
# Using keyword arguments means order doesn't matter
result4 = greeting(
    name=input("Please enter your name: "),
    hobby=input("Please enter your hobby: "),
    city=input("Please enter your city: ")
)
print(result4)


# ============================================================
# SECTION 6: Parameters vs Arguments — puppy example
#
# PARAMETER = the placeholder defined in the def line
# ARGUMENT  = the actual value passed in when calling the function
#
# Here, name/breed/age are PARAMETERS.
# Whatever the user types at runtime becomes the ARGUMENT
# that fills that parameter slot.
# ============================================================

def puppy_info(name="Unknown", breed="Mixed", age=0):
    return f"{name} is a {age} year old {breed}."

result = puppy_info(
    name=input("Enter puppy's name: "),    # user types "Bella"  → argument for name
    breed=input("Enter puppy's breed: "),  # user types "Poodle" → argument for breed
    age=input("Enter puppy's age: ")       # user types "3"      → argument for age
)

print(result)


# ============================================================
# SECTION 7: Strings as a sequence
# A string is a sequence of characters — each character has
# an index position starting at 0.
# "Python" → P=0, y=1, t=2, h=3, o=4, n=5
# Negative indexes count from the end: -1 = last character
# ============================================================

# 1. Creating a string
text = "Python"

# 2. Indexing — access a single character by position
print("First character", text[0])    # P
print("Last character", text[-1])    # n

# 3. Slicing — extract a range of characters
# Format: text[start:stop] → stop is NOT included
print("First three characters:", text[0:3])   # Pyt  (index 0,1,2 — stops before 3)
print("From index 2 to end:", text[2:])       # thon (start at 2, go to the end)
print("Every second character:", text[::2])   # Pto  (start:stop:step — skips every other)

# 4. Iteration — loop through each character one at a time
print("Characters in string:")
for char in text:
    print(char, end=" ")   # end=" " prints a space instead of a new line after each char
print()                    # print() with nothing in it just moves to a new line

# 5. Membership — check if a substring exists inside a string
print("'Py' in text?", "Py" in text)      # True
print("'Java' in text?", "Java" in text)  # False

# 6. Length — count total number of characters
print("Length of string:", len(text))     # 6

# 7. Concatenation and repetition
print("Concatenation:", text + "3.1")     # Python3.1 — joins two strings together
print("Repetition:", text * 2)            # PythonPython — repeats the string

# 8. Immutability — strings CANNOT be changed after creation
# This will raise a TypeError:
try:
    text[0] = "J"
except TypeError as e:
    print("Strings are immutable:", e)    # str object does not support item assignment


# ============================================================
# SECTION 8: Splitting a string
# .split(separator) breaks a string into a LIST of parts
# wherever it finds the separator character.
# Great for parsing structured data like codes or CSV.
# ============================================================

def parse_code(product_code):
    parts      = product_code.split("-")  # split wherever there's a "-"
    company    = parts[0]                 # first piece  → "ACME"
    product_id = parts[1]                 # second piece → "123"
    category   = parts[2]                 # third piece  → "L"
    return company, product_id, category

# Calling the function and unpacking the 3 returned values
company, product_id, category = parse_code("ACME-123-L")

print(f"Company: {company}")        # ACME
print(f"Product ID: {product_id}")  # 123
print(f"Category: {category}")      # L


# ============================================================
# SECTION 9: Range
# range() generates a sequence of numbers — used with for loops.
# It does NOT include the stop number (just like slicing).
#
# Formats:
#   range(stop)              → starts at 0
#   range(start, stop)       → custom start
#   range(start, stop, step) → custom start and increment
# ============================================================

# 1. Basic range — starts at 0, stops before 5
print("range(5):")
for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4
print()

# 2. Range with start and stop
print("\nrange(2, 8):")
for i in range(2, 8):
    print(i, end=" ")   # 2 3 4 5 6 7
print()

# 3. Range with start, stop, and step
print("\nrange(0, 20, 5):")
for i in range(0, 20, 5):
    print(i, end=" ")   # 0 5 10 15 (jumps by 5 each time)
print()

# 4. Counting backwards using a negative step
print("\nrange(10, 0, -2):")
for i in range(10, 0, -2):
    print(i, end=" ")   # 10 8 6 4 2 (counts down by 2)
print()