# ========================================
# Lab 1 (continued)
# Script 4: Distance Between Coordinates
# ========================================

# Brainstorm: How do you calculate the distance between coordinates 
# (x1, y1) and (x2, y2)?

# The distance between two coordinates can be found using the 
# euclidean distance formula, which is the square root of the 
# sum of both differences in the x and y coordinates. The official 
# formula is d = √((x2 - x1)**2 + (y2 - y1)**2) 
# For this calculation, we need four variables. Two for each x 
# coordinate and two for each y coordinate.
# =============================================================

# Final Script for Distance Between Two Coordinates

# Define coordinate values
x1 = 5
x2 = 7
y1 = 2
y2 = 4

# Calculate the distance

from math import sqrt

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the results
print(f'The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}')

# Output
# The distance between (5, 2) and (7, 4) is 2.83