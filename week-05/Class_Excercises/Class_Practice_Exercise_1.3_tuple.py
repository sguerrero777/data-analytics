# =======================================================
# Python Tuple Methods
# Practice Worksheet
# Sharleen Guerrero
# =======================================================

# =============================================================
# PART 2 — SAMPLE TUPLE
# =============================================================

# Use this tuple for all excercises in this worksheet

my_tuple = (10, 20, 30, 40, 50)

# Additional examples
mixed_tuple = (1, "Alice", 3.14, True)
nested_tuple = (1, (2, 3), (4, 5, 6))
single_item = (42,) # note: trailing comma required for single-item tuple

# =============================================================
# PART 5 — PRACTICE EXCERCISES
# =============================================================

# Exercise 1: Access the first element using indexing

print(my_tuple[0])

# Output: 10

# Exercise 2: Access the last element using negative indexing

print(my_tuple[-1])

# Output: 50

# Exercise 3: Slice the tuple to get elements from index 1 to 3

print(my_tuple[1:4])

# Output: (20, 30, 40)

# Exercise 4: Use count() to count how many times 30 appears

print(my_tuple.count(30))

# Output: 1

# Exercise 5: Use index() to find the position of 30

print(my_tuple.index(30))

# Output: 2

# Exercise 6: Use len() to find the number of elements

print(len(my_tuple))

# Output: 5

# Exercise 7: Check if 30 exists in the tuple using the in operator

print(30 in my_tuple)

# Output: True

# Exercise 8: Unpack the tuple into 5 seperate variables

a, b, c, d, e = my_tuple
print(f"a={a} b={b} c={c} d={d} e={e}")

# Output: a=10 b=20 c=30 d=40 e=50

# Exercise 9: Concatenate my_tuple with (60, 70)

tuple_2 = (60, 70)
t3 = my_tuple + tuple_2

print(t3)

# Output: (10, 20, 30, 40, 50, 60, 70)

# Exercise 10: Repeat my_tuple twice using the * operator

print(my_tuple * 2) 

# Output: (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# Exercise 11: Convert my_tuple to a list

print(list(my_tuple))

# Output: [10, 20, 30, 40, 50]

# Exercise 12: Find the min(), max(), and sum() of my_tuple

print(min(my_tuple))
print(max(my_tuple))
print(sum(my_tuple))

# Output: 
# 10
# 50
# 150

# =============================================================
# PART 6 — CHALLENGE SECTION
# =============================================================

# Exercise 1: Create a tuple of 5 city names. Sort and display them without converting to a list

city = ("North Bergen", "Union City", "Fort Lee", "Clifton", "Edgewater")

for item in sorted(city):
    print(item)

# Output: 
# Clifton
# Edgewater
# Fort Lee
# North Bergen
# Union City

# Exercise 2: Create a nested tuple storing 3 students and their GPA. Access the second student's GPA

students_gpa = (("Alice Jones", 3.8),("Cesar Spencer", "2.1"), ("Max Gomez", "4.0"))
print(students_gpa[1][1])

# Output: 2.1

# Exercise 3: Use a for loop with enumerate() to print each item in my_tuple with its index

for index, value in enumerate(my_tuple):
    print(f"Index {index}: {value}")

# Output:
# Index 0: 10
# Index 1: 20
# Index 2: 30
# Index 3: 40
# Index 4: 50

# Exercise 4: Convert my_tuple to a list, append 60, then convert back to a tuple

my_list = list(my_tuple)
my_list.append(60)
my_tuple = tuple(my_list)
print(my_tuple)

# Output: (10, 20, 30, 40, 50, 60)

# Exercise 5: Use my_tuple as a dictionary key to store the value 'data set A'

my_dict = {my_tuple: "data set A"}
print(my_dict)

# Output: {(10, 20, 30, 40, 50, 60): 'data set A'}