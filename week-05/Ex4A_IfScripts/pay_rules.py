# ==================================
# Lab 2
# Script 1: Calculating Gross Pay
# ==================================

# Create a script to calculate gross pay given the variables 
# pay_rate and hours_worked. If the person works more than 40 hours, pay the 
# overtime hours at 1.5 times the rate of regular hours.

# ---------------------------------------------------------------

# Final Script for Calculating Gross Pay

pay_rate = float(input('What is your pay rate?: '))
hours_worked = eval(input('How many hours did you work?: '))
gross_pay = []

for _ in range(n):
    name = input('Rep name:').strip()
    sales = float(input('Monthly sales ($): '))
    sales_reps.append((name, sales))