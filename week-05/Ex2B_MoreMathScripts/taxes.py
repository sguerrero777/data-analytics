# ==================================
# Lab 1 (continued)
# Script 3: Federal Tax Withholding
# ==================================

# Brainstorm: Federal taxes are 23% of your salary every month. 
# You make X amount of money. How much is withheld for taxes?

# To calculate federal tax withholding, two variables are needed.
# One for monthly salary, and one for the percentage of federal 
# taxes.

# =============================================================

# Final Script for Tax Withholdings

# Define known values
monthly_salary = 1600
tax_rate = 23  # stored as whole number for percentage display

# Calculate the unknown
tax_withheld = round(monthly_salary * (tax_rate / 100), 2)

# Display the results
print(f'Your monthly salary is ${monthly_salary:.2f}')
print(f'Federal taxes withholds {tax_rate}%')
print(f'The amount withheld for federal taxes is ${tax_withheld:.2f}')

# Output
# Your monthly salary is $1600.00
# Federal taxes withholds 23%
# The amount withheld for federal taxes is $368.00