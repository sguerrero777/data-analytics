# ==================================
# Lab 3
# Script 3: Calculating Federal Tax
# ==================================

# Create a script that will calculate federal tax based on the values 
# of annual gross income (a number) and a filing status (‘single’ or ‘joint’).

# Single Filers
# Annual Income Range       Tax Rate
# Under 12000               5 %
# 12000 - 24999.99          10 %
# 25000 - 74999.99          15 %
# 75000 and over            20 %

# Joint Filers
# Annual Income Range       Tax Rate
# Under 12000               0 %
# 12000 - 24999.99          6 %
# 25000 - 74999.99          11 %
# 75000 and over            20 %      
# ---------------------------------------------------------------

# Final Script for Calculating Federal Tax Based on Annual Income / Filing Status


pay_rate = float(input('What is your pay rate?: '))
hours_worked = float(input('How many hours did you work?: '))
filing_status = input('Enter filing status (single or joint): ').strip().lower()

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

annual_income = gross_pay * 52

# using if here instead of elif for joint would make it a separate independent check
# meaning python would always evaluate it regardless of whether single was true
# this also causes the else to only attach to the joint block, not the whole filing status check
# rule of thumb: if two conditions are mutually exclusive, the second one should always be elif

if filing_status == 'single':
    if annual_income < 12000:
        tax_rate = .05
    elif 12000 <= annual_income <= 24999.99:
        tax_rate = .10
    elif 25000 <= annual_income <= 74999.99:
        tax_rate = .15
    elif annual_income >= 75000:
        tax_rate = .20
elif filing_status == 'joint':
    if annual_income < 12000:
        tax_rate = 0
    elif 12000 <= annual_income <= 24999.99:
        tax_rate = .06
    elif 25000 <= annual_income <= 74999.99:
        tax_rate = .11
    elif annual_income >= 75000:
        tax_rate = .20
else:
    print('Error. Please enter a valid filing status: ')
    tax = 0
# For invalid value, this will prevent the program from using an undefined 
# tax_rate variable in the calculations below, which would cause an error.

weekly_tax_withhold = gross_pay * tax_rate
net_pay = gross_pay - weekly_tax_withhold

print(f'You worked {hours_worked} this period.')
print(f'Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:,.2f}')
print(f'Your filing status is {filing_status}.')
print(f'Your tax withholding for the week is ${weekly_tax_withhold:,.2f}')
print(f'Your net pay is ${net_pay:,.2f}')
# :,.2f formatting adds thousand seperators

# future tip: elif doesn't need >= 12000 because python already knows previous 
# conditions failed, so it only needs to check if it's less than 25000.

# Output:
# What is your pay rate?: 20
# How many hours did you work?: 45
# Enter filing status (single or joint): single
# You worked 45.0 this period.
# Because you earn $20.00 per hour, your gross weekly pay is $950.00
# Your filing status is single.
# Your tax withholding for the week is $142.50
# Your net pay is $807.50