# ==================================
# Lab 2 (continued)
# Script 1: Calculating Tip Amount
# ==================================

# Brainstorm: How do you calculate the tip amount on a restaurant bill given the tip percentage? 

# a) Figure out the formula and what the script would look like, making up example 
#    values as needed. 
# The tip percentage for me when I eat out is always 20% minimum. The last time I ate at a restaurant
# was a few months ago at a ramen place called Ani Ramen, with the total bill being $65.75 The tip 
# percentage as a decimal and the total bill amount are my two variables. The exact tip amount is the 
# product of these two variables.

# Displayed output should be formatted as followed:
# The tip on a $[number] restaurant bill is $[number]

# =============================================================

# Final Script for Calculating Tip Amount for Ani Ramen Bill

# Define Bill Amount and Tip Percentage
total_bill = 65.75
tip_percentage = .20 # 20%

# Calculate the Tip Amount
tip_amount = total_bill * tip_percentage

# Display the results
print(f'The tip on a ${total_bill} restaurant bill is ${tip_amount:.2f}')

# Output
# The tip on a $65.75 restaurant bill is $13.15