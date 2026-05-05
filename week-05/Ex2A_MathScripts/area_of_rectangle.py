# ===============================================
# Lab 2 (continued)
# Script 2: Calculating the Area of a Rectangle
# ================================================

# Brainstorm: How do you calculate the area of a rectangle using the dimensions of your birthday?

# a) Say you have a rectangle that has dimensions corresponding to your birthday – the 
#    month number is one side and the day of the month is the other side. How would 
#    you calculate the area of this rectangle?  
# My birthday is August 26, 2004. In this scenario, the length of the rectangle would be the day of 
# my birthday since it is numerically larger, and the month would be the width because it is smaller. 
# So the dimensions of the rectangle are: length is 26 with a width of 8.


# b) Figure out the formula and what the script would look like.
# The formula for calulating the area of a rectangle is length times width.
# A = l * w 


# Displayed output should be three print statements:
# Side A is [number] 
# Side B is [number] 
# The area of the rectangle is [number]

# =============================================================

# Final Script for Sharleen's Birthday Rectangle

# Define Measurements
length = 26
width = 8

# Calculate the Area of Rectangle
area = length * width

# Display the results
print(f'Side A is {length}')
print(f'Side B is {width}')
print(f'The area of the rectangle is {area}')

# Output
# Side A is 26
# Side B is 8
# The area of the rectangle is 208