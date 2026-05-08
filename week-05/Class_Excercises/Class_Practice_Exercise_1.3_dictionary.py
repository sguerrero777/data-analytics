# =======================================================
# Python Dictionary Methods
# Practice Worksheet
# Sharleen Guerrero
# =======================================================

# =============================================================
# PART 1 — SAMPLE DICTIONARY
# =============================================================

# Use this dictionary for all exercises in this worksheet:

student = {
 "name" : "Alice",
 "age" : 20,
 "major" : "Data Analytics",
 "gpa" : 3.5
}

# =============================================================
# PART 3 — PRACTICE EXCERCISES
# =============================================================

# Tips:
# If I want to return a value, do inside print
# If I want to modify the dictionary, call alone then print\

# Exercise 1: Use get() to access "name"
print(student.get("name", "Not Available"))

# Output: Alice

# Exercise 2: Use get() with a default value for "grade"

print(student.get("grade", "Not Available"))

# Output: Not Available

# Exercise 3: Use update() to add "year": "Sophmore
student.update({"year": "Sophmore"})
print(student)

# Output: {'name': 'Alice', 'age': 20, 'major': 'Data Analytics', 'gpa': 3.5, 'year': 'Sophmore'}

# Exercise 4: Use pop() to remove "age"
student.pop("age")
print(student)

# Output: {'name': 'Alice', 'major': 'Data Analytics', 'gpa': 3.5, 'year': 'Sophmore'}

# Exercise 5: Use popitem()
student.popitem()
print(student)

# Output: {'name': 'Alice', 'major': 'Data Analytics', 'gpa': 3.5}

# Exercise 6: Use keys()
student.update({"age": 20})
print(student.keys())

# Output: dict_keys(['name', 'major', 'gpa', 'age'])

# Exercise 7: Use values()
print(student.values())

# Output: dict_values(['Alice', 'Data Analytics', 3.5, '20'])

# Exercise 8: Use items()
print(student.items())

# Output: dict_items([('name', 'Alice'), ('major', 'Data Analytics'), ('gpa', 3.5), ('age', '20')])

# Exercise 9: Use copy()
print(student.copy())

# Output: {'name': 'Alice', 'major': 'Data Analytics', 'gpa': 3.5, 'age': '20'}

# Exercise 10: Use clear()

student.clear()
print(student)

# Output: {}

# =============================================================
# PART 4 — CHALLENGE SECTION
# =============================================================

# Exercise 1: Add "courses" with a list of 3 courses using update()
student.update({"Course": ["Anatomy", "Python", "Biology"]})
print(student)
# A dictionary key can only hold one value. So if I want multiple values under one key, that one value needs to be a list []

# Output: a dictionary key can only hold one value. So if you want multiple values under one key, that one value needs to be a list:

# Exercise 2: Check if "gpa" exists as a key in the dictionary
print(student.get("gpa", "Not Available"))

# Output: Not Available

# Exercise 3: Loop through the dictionary and print each key and its value

for key, value in student.items():
    print(f"{key}: {value}")

# Output: Course: ['Anatomy', 'Python', 'Biology']
