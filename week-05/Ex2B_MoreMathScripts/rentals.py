# ==================================
# Lab 1 (continued)
# Script 6: Van Rentals
# ==================================

# Brainstorm: Calculating Van Rentals for Tour

# There are X people going on a tour. Charter vans seat 15 passengers each.
# Vans cost $250 per day to rent (including driver's pay).
# How many vans do you need? How much will it cost? What is the cost per 
# person? Test with 38 tourists. To figure out how many vans I need, I need
# three variables. One for number of tourists, one for cost of each van, and
# one for the capacity of each van. 

# =============================================================

# Final Script for Calculating How Many Vans are Needed

# Define known values
num_tourists = 38
van_capacity = 15
van_cost = 250

# Calculate the unknowns
import math 

vans_needed = math.ceil(num_tourists / van_capacity)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / num_tourists

# Display the results
print(f'The number of vans needed for {num_tourists} tourists is {vans_needed}')
print(f'The total cost to rent the vans is ${total_cost:.2f}')
print(f'The cost per person is ${cost_per_person:.2f}')

# Output
# The number of vans needed for 38 tourists is 3
# The total cost to rent the vans is $750.00
# The cost per person is $19.74

# Answers:

# a) How much money did your script say you had to charge per person?
# The script said I needed to charge $19.74 per person

# b) If you multiply that out, how much did you collect?
# $19.74 * 38 = $750.12
  
# c) How much were the vans?
# The vans were $750.00

# d) Why do you have leftover money?
# I have left over money because ceil() rounded up to 3 vans to fully fit 38 tourists.
# The cost is split across all 38 people but only 3 vans were needed, leaving a small remainder.