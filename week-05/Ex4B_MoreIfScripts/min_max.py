# ==================================
# Lab 4
# Script 4: Min & Max
# ==================================

# Create a script that  displays both the smallest and then the 
# largest of three numbers. Name your variables a, b, and c and assign them values. 
# Then use if/else statements to determine and display the answer.

# ---------------------------------------------------------------

# Final Script for Displaying Min/Max with Variables

# Define variables
a = 10
b = 9
c = 5

# Define smallest

if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c

# Define largest

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else: 
    largest = c

print (f'The smallest value is {smallest}')
print (f'The largest value is {largest}')

# Output:
# The smallest value is 5
# The largest value is 10
