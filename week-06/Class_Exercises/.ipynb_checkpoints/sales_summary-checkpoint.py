# ============================================================
# Week 6 Lab: Functions, Parameters, and Arguments
# Script: Sales Summary Calculator
# ============================================================


# ============================================================
# APPROACH 1: Collect input OUTSIDE the function
# Variables are stored separately, so they're available
# anywhere in the script — including the f-string below.
# ============================================================

# Req 1 & 2: Collecting Input and Type Casting
# input() always returns a string, so we cast:
#   int()   → for whole numbers (units can't be 2.5)
#   float() → for decimals (price needs cents)
name   = input("Associate name: ")
region = input("Store region: ")
units  = int(input("Units Sold: "))
price  = float(input("Price Per Unit $: "))

# Req 3: Define the function with 4 parameters (placeholder slots)
# Parameters: name, region, units, price
# Arguments:  the actual values passed in when the function is called
def sales_summary(name, region, units, price):
    revenue = units * price       # Req 5: total revenue calculation
    bonus   = revenue * 0.10      # Req 5: 10% performance bonus
    return revenue, bonus         # return BOTH values at once

# Call the function — arguments fill the parameter slots in order.
# Two variables catch the two returned values.
revenue, bonus = sales_summary(name, region, units, price)

# Req 4: Print report using a triple-quote f-string.
# Triple quotes let us write multi-line strings naturally.
# :.2f formats a float as currency with exactly 2 decimal places.
print(f"""
===== RetailEdge Inc. — Sales Summary =====
Associate : {name}
Region    : {region}
Units sold: {units}
Unit price: ${price:.2f}
-------------------------------------------
Total revenue        : ${revenue:.2f}
Performance bonus (10%) : ${bonus:.2f}
===========================================
""")


# ============================================================
# APPROACH 2: Collect input INSIDE the function call (cleaner)
# Input is passed directly as keyword arguments.
# Because name and region are never stored outside the function,
# we must also return them so the f-string can access them.
# ============================================================

# name has a default value ("Unknown") so it's optional —
# the user can press Enter to skip it.
# RULE: parameters WITH defaults must come AFTER required ones.
def sales_summary_v2(region, units, price, name="Unknown"):
    revenue = units * price
    bonus   = revenue * 0.10
    return revenue, bonus, name, region   # return ALL values we need later

# Keyword arguments — we name each slot explicitly.
# This means order doesn't matter when calling the function.
# Type casting still required since input() always returns a string!
revenue, bonus, name, region = sales_summary_v2(
    region=input("Store region: "),
    units=int(input("Units Sold: ")),
    price=float(input("Price Per Unit $: ")),
    name=input("Associate name (or press Enter to skip): ")
)

print(f"""
===== RetailEdge Inc. — Sales Summary =====
Associate : {name}
Region    : {region}
-------------------------------------------
Total revenue        : ${revenue:.2f}
Performance bonus (10%) : ${bonus:.2f}
===========================================
""")




