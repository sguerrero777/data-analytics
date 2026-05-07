# ============================================================
# Sharleen Guerrero
# May 6, 2026
# Notes: List and Dictionaries
# ============================================================


# What is a List? --------------------------------------------

# a list is a collection of items stored in a single variable
# uses square brackets []
# can hold mixed data types (integers, strings, floats, even other lists)
# Key Properties of a List:
# Ordered: items stay in the order you put them, index starts at 0
# Mutable: you can add, remove, or change items after creation
# Indexed: each item has a position number starting at 0
# negative indexing (-1) accesses from the end
# Allows duplicates: same value can appear more than once
# Dynamic size: can grow or shrink
# Iterable: can loop through it with a for loop
# Nestable: can contain other lists inside it
# Syntax: []


# Accessing List Elements by Index ---------------------------
# each item in a list has a position number called an index
# indexing starts at 0, not 1
# [2, 4, 't', 'a', 6, 'y']
#   0   1   2    3   4   5   -- positive index
#  -6  -5  -4   -3  -2  -1   -- negative index

values = [2, 4, 't', 'a', 6, 'y']

print(values[0])   # 2
print(values[1])   # 4
print(values[2])   # t
print(values[3])   # a
print(values[4])   # 6
print(values[5])   # y


# Accessing List Elements with a For Loop --------------------

# Instead of manually typing each index, a for loop does it automatically
# for item in list: goes through each element one by one.
# The variable name (item) is temporary. It gets overwritten each loop and
# you can name it anything: item, x, element, etc.

values = [2, 4, 't', 'a', 6, 'y']

# Access each element using a for loop
for item in values:
    print(item)

# output:
# 2
# 4
# t
# a
# 6
# y


# More List Features -----------------------------------------

# list1 shows a list of integers with indexing and slicing
# list2 shows a nested list (a list inside a list) with mixed types
#
# list1[0]   -- first element (positive index)
# list1[-1]  -- last element (negative index, counts from end)
# list1[1:4] -- slicing: returns elements from index 1 up to (not including) 4

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [1, 1.5, "ABC", True, [1, 2, 3]]
print(list2)        # [1, 1.5, 'ABC', True, [1, 2, 3]]

print(list1[0])     # 1   first element
print(list1[-1])    # 10  last element
print(list1[1:4])   # [2, 3, 4] slice from index 1 to 3

for item in list1:
    print(item)


# Example: Classmates List ----------------------------------

# Write a Python program to store the names of three classmates
# in a list. Use one f-string to display the names as shown below.


classmates = ["Maia Black", "Vesna Cari", "Sha'Rya Weaver"]

for name in classmates:
    print(f"My classmate's name is {name}")
# For loop with an f-string lets you print each item with the same sentence format automatically

# output:
# My classmate's name is Maia Black
# My classmate's name is Vesna Cari
# My classmate's name is Sha'Rya Weaver


# What is a Dictionary? --------------------------------------
# a dictionary stores key-value pairs
# uses curly braces {}
# keys are unique and are used to look up their corresponding values
# syntax: {key: value, key: value}
# access a specific value: dictionary['key']
# loop through all pairs: for key, value in dictionary.items()


# Exmaple: Classmates Dictionary ----------------------------

# Create a dictionary to store the name and home state
# of three classmates.

classmates = {
    "Maia": "Georgia",
    "Vesna": "New York",
    "Sha'Rya": "New York"
}

for name, state in classmates.items():
    print(f"{name} : {state}")
# .items() gives you both the key and value at the same time
# two loop variables instead of one: for name, state in dict.items()

# output:
# Maia : Georgia
# Vesna : New York
# Sha'Rya : New York

# you can also access a value directly by its key:
# print(classmates['Maia'])   -- output: Georgia