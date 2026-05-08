# ============================================================
# Sharleen Guerrero
# May 8, 2026
# Notes: Sets, Conditionals, While Loops, For Loops
# ============================================================


# ============================================================
# SETS
# ============================================================
# A set is an unordered collection of UNIQUE elements
# Uses {} — no duplicates allowed, no guaranteed order

# Unordered
my_set = {3, 1, 2}
print(my_set)

# Output: {1, 2, 3}
# even though we put 3 first, sets don't preserve order

# No Duplicates
my_set = {1, 2, 3, 3, 3, 3}
print(my_set)

# Output: {1, 2, 3}
# set automatically removes all duplicates

# Add
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# Output: {1, 2, 3, 4}

# Remove
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)

# Output: {1, 3}
# remove() raises an error if the value doesn't exist

# Discard
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

# Output: {1, 3}
# discard() does the same thing but will NOT raise an error if the value doesn't exist
# use discard() when you're not sure if the value is there

# Iteration
my_set = {1, 2, 3}
for item in my_set:
    print(item)

# Output:
# 1
# 2
# 3

# Unindexable
# my_set = {1, 2, 3}
# print(my_set[0])
# raises error — sets don't have indexes, can't access by position
# if you need to access by index, convert to a list first


# Set Exercise -------------------------------------

# Create a Python set named states that contains at least 5 U.S. states (as strings)
# Display total count, check if Texas exists, display alphabetically,
# find longest state name, add Georgia, remove Florida

states = {"New York", "New Jersey", "Virginia", "Maryland", "Florida"}

print(f"Total number of states: {len(states)}")
# Output: Total number of states: 5

print(f"Is Texas in the set: {'Texas' in states}")
# Output: Is Texas in the set: False

print(f"States in alphabetical order: {sorted(states)}")
# Output: States in alphabetical order: ['Florida', 'Maryland', 'New Jersey', 'New York', 'Virginia']

longest = max(states, key=len)
print(f"Longest state name: '{longest}' ({len(longest)}) characters.")
# Output: Longest state name: 'New Jersey' (10) characters.

states.add("Georgia")
print(f"After adding Georgia: {states}")

states.discard("Florida")
print(f"After removing Florida: {states}")


# ============================================================
# CONDITIONALS EXERCISE: Day of the Week
# ============================================================
# Prompt user for a number 1-7 and print the corresponding day
# Display an error if the number is outside that range

num = int(input("Please enter a number 1 through 7: "))

# check if number is out of range first before checking individual days
if num < 1 or num > 7:
    print("Error! Number must be between 1 and 7.")
elif num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")


# ============================================================
# WHILE LOOP
# ============================================================
# Use a while loop when you DON'T know how many times to loop ahead of time
# It keeps running as long as the condition is True
# IMPORTANT: always make sure the condition can eventually become False
# or the loop will run forever (infinite loop)

# Structure:
# While condition:
# Do something
# Update the condition. This is easy to forget, causes infinite loop

# Exercise: Sum of Numbers
# Ask user to enter positive numbers one at a time
# Enter a negative number to signal the end of the series
# Display the total sum and count after

# Initialize variables
# these start at 0 and grow each loop — called accumulators
total = 0
count = 0

print("Enter positive numbers one at a time.")
print("Enter a negative number to stop.\n")

# Ask for the first number BEFORE the loop
# The while condition needs something to check before it starts
number = float(input("Enter a number: "))

# Continues while number is positive, stops when negative is entered
while number >= 0:
    total += number   # same as total = total + number, adds to running total
    count += 1        # tracks how many numbers were entered
    number = float(input("Enter a number: "))
    # ask for the next number at the END of the loop
    # this is what gets checked again at the top — don't forget this line
    # without it the loop runs forever on the same number

# Once the loop exits, print the final results
print(f"\nNumbers entered : {count}")
print(f"Sum             : {total:.2f}")


# ============================================================
# FOR LOOPS
# ============================================================
# Use a for loop when you DO know how many times to loop
# or when you want to go through every item in a sequence
# A sequence can be a list, string, tuple, range, etc.

# Structure:
# for variable in sequence:
#     do something
# the variable takes on each value in the sequence one at a time

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# fruit becomes "apple" first, then "banana", then "cherry"
# Output:
# apple
# banana
# cherry

# Looping through a string
# strings are sequences too — each character is one item
for char in "banana":
    print(char)
# Output:
# b
# a
# n
# a
# n
# a

# range(start, stop, step)
# range generates a sequence of numbers
# start = where to begin, stop = where to end (not included), step = how much to count by
for i in range(2, 10, 2):  # start=2, stop=10, step=2
    print(i)

# Output:
# 2
# 4
# 6
# 8
# stops at 8 because 10 is not included

# For loop with break
# break → exits the loop entirely the moment the condition is met
for fruit in fruits:
    if fruit == "banana":
        break       # stops here, nothing after this runs
    print(fruit)

# Output: apple
# print is before the break so apple prints, then banana triggers break

# For loop with continue
# continue → skips the rest of the current loop and goes back to the top
for fruit in fruits:
    if fruit == "banana":
        continue    # skips banana and moves to cherry
    print(fruit)

# Output:
# apple
# cherry

# For loop with else
# else → runs ONLY if the loop finished without hitting a break
# if break is triggered, the else block is skipped
for num in range(3):
    print(num)
else:
    print("Loop completed")
    
# Output:
# 0
# 1
# 2
# Loop completed

# WHILE vs FOR — when to use which:
# for loop  → you know how many times, or looping through a sequence
# while loop → you don't know how many times, depends on user input or a condition