# ==================================
# Lab 1
# Script 1: Department Codes
# ==================================

# Create a script to uses if/elif/else logic to determine and print 
# department name based on a department code. Make sure to test your 
# script with multiple codes. 

# 1     Marketing
# 5     Human Resources
# 10    Accounting 
# 12    Legal
# 18    IT
# 20    Customer Relations 

# ---------------------------------------------------------------

# Final Script for Retrieving Department Names

dept_code = int(input('What is your department code: '))

if dept_code == 1:
    print('Your department is Marketing!')
elif dept_code == 5:
    print('Your department is Human Resources!')
elif dept_code == 10:
    print('Your department is Accounting!')
elif dept_code == 12:
    print('Your department is Legal!')
elif dept_code == 18:
    print('Your department is IT!')
elif dept_code == 20:
    print('Your department is Customer Relations!')
else:
    print('Invalid department code. Please re-enter: ')


# Output:
# What is your department code: 1
# Your department is Marketing!