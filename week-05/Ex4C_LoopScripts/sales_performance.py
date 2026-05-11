# ==================================
# Lab 4
# Script 4: Sales Performance
# ==================================

# You have been given the following list of sales records. Each record is a tuple 
# containing a salesperson's name, their region, and their total sales for the month: 
# Use a for loop to unpack each tuple directly in the loop statement, and print a 
# summary line for each record that looks like this: 
# Marcus Webb (East): $4,250.00 
# Priya Sharma (West): $5,875.50 
# Add a conditional inside your loop: if a salesperson's total is greater than $5,000, also 
# print "  ^ Top performer!" below their summary line. 
# BONUS: Add a variable before the loop to track total sales across all employees, and 
# print the overall total after the loop finishes. 
# ---------------------------------------------------------------

# Final Script for Sales Performance

# Sales Records
sales_data = [ 
('Marcus Webb',    'East',  4250.00), 
('Priya Sharma',   'West',  5875.50), 
('DeShawn Carter', 'East',  3100.75), 
('LaTonya Rivers', 'South', 6420.00), 
('Bob Nguyen',     'West',  4980.25), 
] 

# Summary of Records

print('── Sales Performance Report ──────────────────────────')
total_sales = 0

# enumerate() was removed because the assignment doesn't require numbered output
# for name, region, sales unpacks each tuple directly into 3 variables
# in the same order they appear in the tuple: (name, region, sales)
# no need for () around them since we're not using enumerate
for name, region, sales in sales_data:
    # every salesperson gets the summary line printed first
    # this avoids repeating the same print in both if and else blocks
    print(f'{name} ({region}): ${sales:,.2f}')
    # total_sales += sales adds each salesperson's sales to the running total
    total_sales += sales
    # only top performers get the extra line, printed below their summary
    if sales > 5000:
        print('  ^ Top performer!')

# this runs once after the loop finishes, not inside it
print(f'\nTotal sales across all employees: ${total_sales:,.2f}')

# Output: 
# ── Sales Performance Report ──────────────────────────
# Marcus Webb (East): $4,250.00
# Priya Sharma (West): $5,875.50
#  ^ Top performer!
# DeShawn Carter (East): $3,100.75
# LaTonya Rivers (South): $6,420.00
#   ^ Top performer!
# Bob Nguyen (West): $4,980.25

# Total sales across all employees: $24,626.50

# Python executes line by line from top to bottom. So for every salesperson it always prints
# the summary line first, then immediately checks if they're a top performer and prints that below.
