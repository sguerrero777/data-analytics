# ==================================
# Lab 2 (continued)
# Script 4: Calculating Circle Area
# ==================================

# Brainstorm: How do you calculate the area of a circle?

# a) The diameter of a given circle is the same as the day of your birthday (not the month, 
#    just the day). Figure out the formula, refresh your recollection of the difference 
#    between diameter and radius, and figure out what the script should look like.
# My birthday is August 26; the diameter for the circle will be 26. The formula for finding 
# the area of a circle is a = (pi * r**2) To find the radius of a circle from its diamter, 
# you can first divide the diameter by 2.

# Displayed output should be formatted as followed:
# The area of a circle with radius [number] is [number]

# =============================================================

# Final Script for Calculating the Area of a Circle

# Define Measurements
diameter = 26
radius = diameter / 2

# Calculate the Area of Circle
from math import pi

area = pi * (radius ** 2)

# Display the results
print(f'The area of a circle with radius {radius} is {area:.2f}')

# Output
# The area of a circle with radius 13.0 is 530.93