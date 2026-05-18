# Sharleen
# 5/15/2026
# Class Notes: NumPy Arrays

# =========================================================
# DIFFERENCE BETWEEN LIST AND ARRAY
# =========================================================
# Think of it like this:
# List = a grocery list, can have anything (mixed types)
# Array = a spreadsheet column, everything is the same type
#
# List  → built into Python, no import needed, slower for math
# Array → needs numpy, only one data type, WAY faster for math
# =========================================================

# =========================================================
# ARRAY DIMENSIONS — how many layers deep is your data?
# =========================================================
# 1D Array → Single list            ex: [1,2,3]          access: arr[0]
# 2D Array → Rows and columns       ex: [[1,2],[3,4]]     access: arr[1][0]
# 3D Array → Multiple tables/layers ex: [[[1]]]           access: arr[0][0][0]
# =========================================================

import numpy as np

# =========================================================
# 1D ARRAY (One-Dimensional)
# =========================================================
# Just a simple row of numbers, like one row in a spreadsheet

arr_1d = np.array([10, 20, 30, 40, 50])

print("=== 1D Array ===")
print(arr_1d)

# Accessing elements — same as a list, use the index number
print("First element:", arr_1d[0])    # index 0 = first item
print("Third element:", arr_1d[2])    # index 2 = third item
print("Last element:", arr_1d[-1])    # -1 always means last item

print("\n")

# =========================================================
# 2D ARRAY (Two-Dimensional)
# =========================================================
# Like a table with rows and columns (think Excel spreadsheet)
# To access: arr[row][column]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("=== 2D Array ===")
print(matrix)
print(matrix[1][2])   # Row 1, Column 2 → prints 6
# Think: go to row 1 (second row), then column 2 (third column)

print("\n")

# =========================================================
# 3D ARRAY (Three-Dimensional)
# =========================================================
# Like multiple tables stacked on top of each other (layers)
# To access: arr[layer][row][column]

cube = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("=== 3D Array ===")
print(cube)
print(cube[1][0][1])  # Layer 1, Row 0, Column 1 → prints 6
# Think: go to layer 1 (second table), row 0 (first row), column 1 (second column)

print("\n")

# =========================================================
# NUMPY ARRAY ATTRIBUTES
# =========================================================
# Arrays have built-in attributes that describe your data
# These are super useful in data analysis to understand
# what you're working with before doing any calculations
#
# Attribute   Meaning                        Example
# ---------   -------                        -------
# ndim      → Number of dimensions           1D, 2D, 3D
# shape     → Size of each dimension         (3, 4)
# size      → Total number of elements       12
# dtype     → Data type of elements          int64, float64
# itemsize  → Memory size (bytes/element)    8
# nbytes    → Total memory used              96
# T         → Transpose (rows become cols)   flipped matrix
# real      → Real part (complex numbers)    real values
# imag      → Imaginary part                 imaginary values
# data      → Buffer storing raw data        memory reference
# =========================================================

# Create a 2D array to test attributes on
a = np.array([[10, 20, 30],
              [40, 50, 60]])

print("=== Array Attributes ===")
print("Array:")
print(a)

print("\nShape:", a.shape)      # (2, 3) → 2 rows, 3 columns
print("Dimensions:", a.ndim)   # 2 → it's a 2D array
print("Data type:", a.dtype)   # int32 or int64 depending on your computer
print("Total elements:", a.size)  # 6 → 2 rows x 3 columns = 6

print("\n")

# =========================================================
# ARRAY MATH — this is why arrays are better than lists!
# =========================================================
# With a list you'd have to loop through every element to do math
# With an array, you just write the math and it applies to ALL elements

a = np.array([10, 20, 30, 40])

print("=== Array Math ===")
print(a * 2)      # [20, 40, 60, 80]  → multiplies EVERY element by 2
print(a.mean())   # 25.0              → average of all elements
print(a.dtype)    # int64             → tells you the data type

print("\n")

# =========================================================
# NUMPY ARRAY CREATION FUNCTIONS
# =========================================================
# Instead of typing out every value, numpy has shortcuts
# to create arrays automatically

# empty() → makes an array with random leftover memory values
# use this when you plan to fill it in yourself later
e = np.empty((2, 2))
print("np.empty((2,2))")
print(e, "\n")

# arange() → like Python's range() but gives you an array
# arange(start, stop, step) — stop is NOT included
f = np.arange(0, 10, 2)
print("np.arange(0,10,2)")
print(f, "\n")
# output: [0 2 4 6 8]

# linspace() → gives you evenly spaced values between two numbers
# linspace(start, stop, how_many_values) — stop IS included
g = np.linspace(0, 1, 5)
print("np.linspace(0,1,5)")
print(g, "\n")
# output: [0.  0.25  0.5  0.75  1.]

print("=== End of Arrays Demo ===")
print("\n")

# =========================================================
# NaN vs None — What's the difference?
# =========================================================
# You'll see both of these a lot in data analysis
# when data is missing or empty
#
# None  → Python's way of saying "nothing here" / no value at all
#         like an empty cell that was never filled in
#         Type: NoneType
#
# NaN   → NumPy/pandas way of saying "this number is missing"
#         stands for "Not a Number"
#         Used specifically for missing NUMERIC data
#         Type: float
#
# Rule of thumb:
# Use None  → in regular Python when something has no value
# Use NaN   → in NumPy/pandas when a number is missing in a dataset
# =========================================================

x = None
print("None example:")
print(x)               # None
print(type(x))         # <class 'NoneType'>

print("\n")

y = float('nan')
print("NaN example:")
print(y)               # nan
print(type(y))         # <class 'float'>