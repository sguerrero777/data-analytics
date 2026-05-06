# ==================================
# Lab 3
# Script: Modified Tip Amount 
#         Calculator with User Input
# ==================================

# Lab 3 modifies the tip_amount.py script to create input() options 
# instead of the original fixed variables. 

# =============================================================

# Ask User for Bill Amount and Tip Percentage
total_bill = float(input("What is your total bill amount?: "))
tip_percentage = float(input("What percentage do you want to tip?: "))

# Calculate the Tip Amount
tip_amount = total_bill * (tip_percentage / 100)

# Display the results
print(f'Your total tip is ${tip_amount:.2f}')

# Observations: What are possible pitfalls with using input()?
# One pitfall with using inout() is if a calculation is involved
# for the end result, and the user enters an input thats invalid 
# or doesn't match with the format the formula is written, it can
# affect the accuracy of the output or give an error.