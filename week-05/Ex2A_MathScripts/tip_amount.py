# ==================================
# Lab 2 (continued)
# Script 1: Calculating Tip Amount
# ==================================

# Brainstorm: How do you calculate the tip amount on a restaurant bill given the tip percentage? 

# a) Figure out the formula and what the script would look like, making up example 
#    values as needed. 
# 


# b) Discuss and figure out the formula and what the script would look like, making up example values as needed.
# The formula for calculating net worth would be calculating the sum of assests and subtracting the total by the sum
# of the debts. To calculate my net worth, my variables for assets include liquid money: my checkings and savings accounts.
# I am a student and don't own any houses, cars, or investments currently. My variables for debts include only the sum of my 
# standard credit card debt. I don't owe any outstanding loans.


# Displayed output should be formatted as followed:
# The tip on a $[number] restaurant bill is $[number]

# =============================================================

# Final Script for Calculating Tip Amount for Ani Ramen Bill

# Define assests and liabilities
check_account = 25.57
savings = 6940.11
credit_debt = 4080.08

# Calculate the Assets, Debts, and Net Worth
total_assets = check_account + savings
total_debt = credit_debt
net_worth = total_assets - total_debt

# Display the results
print(f'Sharleen\'s total assets are ${total_assets:.2f}')
print(f'Sharleen\'s total debts are ${total_debt:.2f}')
print(f'Sharleen\'s net worth is ${net_worth:.2f}')

# Output
# Sharleen's total assets are $6965.68
# Sharleen's total debts are $4080.08
# Sharleen's net worth is $2885.60