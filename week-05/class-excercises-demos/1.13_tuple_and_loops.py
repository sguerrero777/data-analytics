# ============================================================
# Sharleen Guerrero
# May 7, 2026
# Topics: Tuples, Sets, Loops, Conditionals
# ============================================================


# ============================================================
# WARM UP: Temperature Conversion (Celsius → Fahrenheit)
# ============================================================
# Formula: F = (9/5) * C + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"Fahrenheit = {fahrenheit:.2f}")
# :.2f rounds the output to 2 decimal places

# Output:
# Enter temperature in Celsius: 100
# Fahrenheit = 212.00


# ============================================================
# TUPLES
# ============================================================
# A tuple is an ordered, immutable collection
# Immutable = cannot be changed after creation
# Uses () instead of []

# Sample Tuple
student = ("Alice", 20, "Data Analytics", 3.5, True)

print(student)
print(f"Name   : {student[0]}")
print(f"Age    : {student[1]}")
print(f"Major  : {student[2]}")
print(f"GPA    : {student[3]}")
print(f"Active : {student[4]}")
print(f"Length : {len(student)}")

# Output:
# ('Alice', 20, 'Data Analytics', 3.5, True)
# Name   : Alice
# Age    : 20
# Major  : Data Analytics
# GPA    : 3.5
# Active : True
# Length : 5


# Tuple Functions -------------------------------------

t = (1, 2, 2, 3, 2)

# Count(x)
print(t.count(2))
# how many times 2 appears in the tuple
# Output: 3

# Index(x)
print(t.index(2))
# index position where 2 FIRST appears
# Output: 1

# Len(t)
print(len(t))
# total number of elements in the tuple
# Output: 5

# Min(t)
print(min(t))
# for numbers: smallest value 
# for strings: alphabetically first
# for mixed types (int + str): raises TypeError in Python 3
# Output: 1

# Max(t)
print(max(t))
# largest value — for strings: alphabetically last
# Output: 3

# Sum(t)
print(sum(t))
# total of all values added together
# Output: 10

# Sorted(t)
print(sorted(t))
# returns a sorted LIST (does not change the original tuple)
# Output: [1, 2, 2, 2, 3]

# Type(t)
print(type(t))
# Output: <class 'tuple'>

# Other Functions ------------------------------------------

t = ("a", "b", "c")

# Indexing
print(t[0])
print(t[-1])
# a
# c
# [0] index 0 prints the first element
# [-1] index -1 prints the last element

# Slice
t = (1, 2, 3, 4, 5)

print(t[1:4])
# Starts at index 1, stops BEFORE index 4
# Output: (2, 3, 4)

# Concatenation
t = (1, 2, 3)

t2 = ("a", "b", "c")
t3 = t + t2

print(t3)
# Output: (1, 2, 3, 'a', 'b', 'c')

# Repetition
t = (1, 2, 3)
t2 = t * 3

print(t2)
# Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
t = (1, 2, 3)

print(2 in t)
print(9 in t)
# True
# False

# Uniqueness
t = (1, 2, 3, 4, 5)

print(len(set(t)))
# Set removes duplicates, len counts what's left
# Output: 5

# Convert to List
t = (1, 2, 3, 4, 5)

print(list(t))
# Output: [1, 2, 3, 4, 5]

# Tuple Excercise ------------------------------------------

# Create a Python Tuple named states that contains at least 5 U.S. states (as strings)

# Process the tuple using built in functions to:
# Display the total number of states in the tuple using a built-in function
# Display the first state and the last state in the tuple
# Use a built-in function to determine if "Texas" is in the tuple
# Display the states in alphabetical order (hint: use a function that works with iterables)
# Find and display the length (number of characters) of the longest state name
# Use f-string for all output

states = ("New Jersey", "New York", "California", "Virgina", "Florida")

print(f"The total number of states is {len(states)}")
# Output: The total number of states is 5

print(f"The first state is {states[0]}")
# Output: The first state is New Jersey

print(f"The last state is {states[-1]}")
# Output: The last state is Florida

print(f"Is Texas in the tuple? {'Texas' in states}")
# Output: Is Texas in the tuple? False

print(f"Alphabetical order of states: {sorted(states)}")
# Output: Alphabetical order of states: ['California', 'Florida', 'New Jersey', 'New York', 'Virginia']

print(f"Longest state name length: {len(max(states, key=len))}")
# max(states, key=len) → finds the longest string
# len() then returns the character count
# Output: Longest state name length: 10


# ============================================================
# SETS
# ============================================================
# A set is an unordered collection of UNIQUE elements
# Uses {} — no duplicates allowed, no guaranteed order

# Iterate with a for loop
my_set = {"Alice", "Bob", "Charlie"}

for item in my_set:
    print(item)

# Output (order not guaranteed):
# Charlie
# Alice
# Bob

# Membership test with in
my_set = {1, 2, 3, 4, 5}

print(3 in my_set)
print(9 in my_set)
# True
# False

# Convert to a list - then access by index
my_set = {1, 2, 3, 4, 5}

my_list = list(my_set)
print(my_list[2])
# Output: some value at index 2 (order not guaranteed)

# Convert to a sorted list - access in a predictable order
my_set = {1, 2, 3, 4, 5}

my_list = sorted(my_set)
print(my_list[2])
# sorted order is guaranteed: [1, 2, 3, 4, 5]
# Output: 3

# Unpacking - assign elements to variables (order not guaranteed)
my_set = {1, 2, 3, 4, 5}

a, b, c, d, e = my_set
print(a, b, c, d, e)
# Output: 1 2 3 4 5 (order not guaranteed since sets are unordered)


# ============================================================
# CONDITIONALS
# ============================================================
# if      → checks the first condition
# elif    → checks next condition ONLY if all above were False
# else    → runs if nothing above matched (catch-all)

# Basic if
num = 5
if num > 5:
    print("Hello")
print("Done")
# Output: Done  (5 is not > 5, so if block is skipped)

# if / else
num = 5
if num > 5:
    print("Hello")
else:
    print("Hi")
print("Done")
# Output:
# Hi
# Done

# if / elif / else
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
print("Done")


# ============================================================
# LOOPS
# ============================================================

# While Loop
# repeats as long as the condition is True
# num -= 1 decreases num each time → eventually stops (condition control)

num = 5
while num > 0:
    print("Hello")
    num -= 1

# Output: Hello (printed 5 times)

# For Loop - break
# break → exits the loop entirely when condition is met

for item in [1, 2, 3, 4]:
    if item == 2:
        break
    print(item)

# Output: 1
# stops at 2 without printing it — break exits before the print runs

# For Loop - continue
# continue → skips the current iteration and moves to the next one

for item in [1, 2, 3, 4]:
    if item == 2:
        continue
    print(item)

# Output:
# 1
# 3
# 4
# 2 is skipped, but the loop keeps going

# For Loop - pass
# pass → placeholder, does nothing
# used when syntax requires a block but you have no code to put there yet

for item in [1, 2, 3, 4]:
    pass


# ============================================================
# EXERCISE: Grading Scale
# ============================================================
# Prompt user for a score and print the corresponding letter grade

score = int(input("Enter a score: "))

if score >= 90:
    print(f"Score: {score} - Grade: A")
elif score >= 80:
    print(f"Score: {score} - Grade: B")
elif score >= 70:
    print(f"Score: {score} - Grade: C")
elif score >= 60:
    print(f"Score: {score} - Grade: D")
else:
    print(f"Score: {score} - Grade: F")

# Sample output:
# Enter a score: 85
# Score: 85 - Grade: B