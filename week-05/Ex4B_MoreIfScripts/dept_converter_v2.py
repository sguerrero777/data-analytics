# ==================================
# Lab 1 (continued)
# Script 1: Department Codes V2
# ==================================

# Create a script to uses if/elif/else logic to determine and print 
# department name based on a department code. Make sure to test your 
# script with multiple codes. Once your script is working, rewrite it 
# using a match/case statement instead of if/elif/else.

# 1     Marketing
# 5     Human Resources
# 10    Accounting 
# 12    Legal
# 18    IT
# 20    Customer Relations 

# ---------------------------------------------------------------

# Version 2 Script for Retrieving Department Names

dept_code = int(input('What is your department code: '))

match dept_code:
    case 1:
        print('Your department is Marketing!')
    case 5:
        print('Your department is Human Resources!')
    case 10:
        print('Your department is Accounting!')
    case 12:
        print('Your department is Legal!')
    case 18:
        print('Your department is IT!')
    case 20:
        print('Your department is Customer Relations!')
    case _:
        print('Invalid department code. Please re-enter: ')

# Output:
# What is your department code: 10
# Your department is Accounting!