# ==================================
# Lab 4
# Script: Modified Lab 1 Tips Script
#         with F-Strings
# ==================================

# Lab 4 modifies the Ex2A_tips.py script to re-write the print 
# output as f-strings instead of using str() concatenation.
# Using F strings is more elegant and best practice in Python.

# =============================================================

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Original prints using str() concatenation:
# print("The total due is " + str(total_due))
# print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Total due is " + str(total_due))
# print("Tip is " + format(tip, ".2f"))

# Re-written Print Outputs as f-strings:
print(f'The total due is ${total_due:.2f}')
print(f'Food cost is ${food_cost} and tax is ${tax}')
print(f'Total due is ${total_due:.2f}')
print(f'Tip is ${tip:.2f}')