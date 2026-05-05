# ===============================
# Lab 1
# ===============================

# Sample problem: How do you calculate the total due at a restaurant given the food cost, tax, and tip? 
# Formula: Total Due is determined by: Food Cost + Tax + Tip 
# Script: 

# Define known values 
food_cost = 79.25 
tax = 6.54 
tip = 12.00 

# Calculate the unknown 
total_due = food_cost + tax + tip 

# Display the results 
print("The total due is " + str(total_due))
# 2a) Here, the str() function is used to cast the total amount due as a string.
# Now, it can be concatenated with other strings using the + operator.

print("Food cost is " + str(food_cost) + " and tax is " + str(tax)) # Food cost is 79.25 and tax is 6.54 
print("Tip is " + str(tip)) # Tip is 12.0
print("Total due is " + str(total_due)) # Total due is 97.79

# An f string and format function is used to display the tip as a float with 2 decimal places and return a string directly.
print("Tip is " + format(tip, ".2f")) 
