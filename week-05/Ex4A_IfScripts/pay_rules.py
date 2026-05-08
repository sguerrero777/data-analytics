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

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

print(f"{'Pay rate:':<18} ${pay_rate:.2f}")
print(f"{'Hours worked:':<18} {hours_worked}")
print(f"{'Gross pay:':<18} ${gross_pay:.2f}")


# Output:
# What is your pay rate?: 17.50
# How many hours did you work?: 45
# Pay rate:          $17.50
# Hours worked:      45
# Gross pay:         $831.25