# ==================================
# Lab 2
# Script 1: Calculating Net Worth
# ==================================

# Brainstorm: How do you calculate your net worth given your assets and debts? 

# a) What are “assets” that would need to be included in this calculation? What about “debts”?
# Assets that would need to be included in the calculation are anything of monetary value I own.
# This can include real estate property, cars, investments, or liquid money.
# Debts that need to be considered are any financial obligations someone owes. Liabilites can 
# include loans (car, mortage, personal, student) and any standard credit card debts or collections.


# b) Discuss and figure out the formula and what the script would look like, making up example values as needed.
# The formula for calculating net worth would be calculating the sum of assests and subtracting the total by the sum
# of the debts. To calculate my net worth, my variables for assets include liquid money: my checkings and savings accounts.
# I am a student and don't own any houses, cars, or investments currently. My variables for debts include only the sum of my 
# standard credit card debt. I don't owe any outstanding loans.


# Displayed output should be three print statements:
# Your total assets are [number]
# Your total debts are [number] 
# Your net worth is [number]

# =============================================================

# Final Script for Sharleen's Current Net Worth

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