# ==================================
# Lab 2
# BONUS LAB: Calculating leap Year
# ==================================

#  Create a script to determine whether a given year is a leap year
# in the Gregorian calendar. You will need to do a little research
# to determine exactly what makes a year a leap year.  

# Rules for a Leap Year
# 1. Has to be divisible by 4
# 2. If it's divisible by 100 evenly, NOT a leap year
# 3. If divisible evenly by 400, YES 

# ---------------------------------------------------------------

# Final Script for Calculating Leap Year

year = int(input('Please enter a year (yyyy): '))

# == means "is equal to" — comparing two values, not assigning them
# % gives the remainder after division — if remainder is 0, it divides evenly
# indentation tells Python what is "inside" each if block
# no elif here because 100 and 400 checks only happen inside the 4 check, not as separate branches

# if the year has no remainder when divided by 4, it is a leap year candidate
if year % 4 == 0:
    # if it is also divisible by 100, we need to check further
    if year % 100 == 0:
        # if it is also divisible by 400, it overrides the 100 rule and is a leap year
        if year % 400 == 0:
            print(f'{year} is a leap year')
        # divisible by 100 but not 400, so it is not a leap year
        else:
            print(f'{year} is not a leap year')
    # divisible by 4 but not 100, so it is a leap year
    else:
        print(f'{year} is a leap year')
# not divisible by 4 at all, so it is not a leap year
else:
    print(f'{year} is not a leap year')

# Output:
# Please enter a year (yyyy): 2026
# 2026 is not a leap year