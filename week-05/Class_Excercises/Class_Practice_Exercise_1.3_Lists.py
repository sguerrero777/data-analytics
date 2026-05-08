# =======================================================
# Python List Methods
# Practice Worksheet
# Sharleen Guerrero
# =======================================================

# =============================================================
# PART 2 — SAMPLE LIST
# =============================================================

# Use this list for all excercises in this worksheet

my_list = [1, 2, 3, 4, 5]

# Additional examples
mixed_list = [10, "Alice", 3.14, True]
nested_list = [1, [2, 3], [4, 5, 6]]

# =============================================================
# PART 4 — PRACTICE EXCERCISES
# =============================================================

# Exercise 1: Use append() to add 6 to the end of the list

my_list.append(6)
print(my_list)

# Output: [1, 2, 3, 4, 5, 6]

# Exercise 2: Use insert() to add 99 at index 2

my_list.insert(2, 99)
print(my_list)

# Output: [1, 2, 99, 3, 4, 5, 6]

# Exercise 3: Use remove() to delete the value 3

my_list.remove(3)
print(my_list)

# Output: [1, 2, 99, 4, 5, 6]

# Exercise 4: Use pop() to remove and return the item at index 0

my_list.pop(0)
print(my_list)

# Output: [2, 99, 4, 5, 6]

# Exercise 5: Use sort() to sort the list in ascending order

my_list.sort()
print(my_list)

# Output: [2, 4, 5, 6, 99]

# Exercise 6: Use reverse() to reverse the list

my_list.reverse()
print(my_list)

# Output: [99, 6, 5, 4, 2]

# Exercise 7: Use index() to find the position of the value 3

my_list.append(3)
print(my_list.index(3))
# Since I removed the value of 3 in excercise 3, I had to add it back to 
# find it's index position

# Output: 5

# Exercise 8: Use count() to count how many times 3 appears 

my_list.count(3)
print(my_list.count(3))

# Output: 1

# Exercise 9: Use slicing to extract elements from index 1 to 3

print(my_list[1:3])

# Output: [6, 5]

# Exercise 10: Use copy() to create a copy of the list

print(my_list.copy())

# Output: [99, 6, 5, 4, 2, 3]

# Exercise 11: Use clear() to remove all items from the list
my_list.clear()
print(my_list)

# Output: []

# =============================================================
# PART 5 — CHALLENGE SECTION
# =============================================================

# Exercise 1: Create a list of 5 student names and sort them alphabetically

students = ["Oscar", "Sharleen", "Joaly", "Esteban", "Aylin"]
students.sort()
print(students)

# Output: ['Aylin', 'Esteban', 'Joaly', 'Oscar', 'Sharleen']

# Exercise 2: Create a nested list to store 3 students and their grades, then access the second student's grade

student_grades = [["Aylin", "A"], ["Oscar", "B"], ["Joaly", "C"]]
print(student_grades[1][1])

# Output: B

# Exercise 3: Use a for loop to print each item in my_list with its index position
my_list = [1, 2, 3, 4, 5]

for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")
# enumerate() adds a number to each item in the list
# like a numbered list:
# 0 Oscar
# 1 Sharleen
# 2 Joaly

# index, value splits each numbered item into two variables
# index = the number, value = the item
# so you can use both separately in the loop

# I can use this anytime I need both the item and where it is. Ex. Finding which student is failing.

# Output
# Index 0: 1
# Index 1: 2
# Index 3: 4
# Index 4: 5

# Exercise 4: Check if the value 10 exists in my_list using the in operator

print(10 in my_list)

# Output: False
