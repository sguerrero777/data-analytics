# ==================================
# Lab 2 (continued)
# Script 5: Savings Account Forecast
# ==================================

# Brainstorm: How long will it take a savings account worth X to double in value 
# based on an interest rate of IR? 

# a) Figure out the formula and what the script would look like, making up example 
#    values as needed.
# The rule of 72 is a financial shortcut that estimates how long it will take for an 
# investment to double in value when earning an annual interest rate of return. To use 
# this rule, divide 72 by the annual interest rate (percentage) to get the approximate 
# years. In this scenario, the variables needed are my current savings balance, 
# and a variable for the interest rate. The official formula uses is t = 72 / R, where t
# is the number of years to double and r is the annual interest rate in percent.

# Displayed output should be formatted as followed:
# Your current savings is [number]. 
# At a [number]% interest rate, your savings account will be 
# worth [number] in [number] years. 

# =============================================================

# Final Script for Calculating Savings Account Worth

# Define Bill Amount and Tip Percentage
starting_savings = 6940.11
interest_rate = 4.0 # 4.5% interest rate, stored as a whole number, per for Rule of 72

# Calculate the Tip Amount
years_to_double = 72 / interest_rate
doubled_balance = starting_savings * 2

# Display the results
print(f'Your current savings is ${starting_savings:.2f}')
print(f'At a {format(interest_rate / 100, ".0%")} interest rate, your savings account will be worth ${format(doubled_balance, ".2f")} in {format(years_to_double, ".1f")} years.')

# Output
# Your current savings is $6940.11
# At a 4% interest rate, your savings account will be worth $13880.22 in 18.0 years.