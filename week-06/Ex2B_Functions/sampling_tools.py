# ============================================================
# Exercise 2.B Using Library Functions
# Lab 1: Random Module
# ============================================================

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# ----- a) Product of the Day -----
# Use random.choice to feature a "Product of the Day" based on one 
# randomly selected item. 
product_of_day = random.choice(products)
print(f"Product of the Day: {product_of_day}")
# I stored it as variable first to be able to reference later if necessary.

# ----- b) Usability Survey -----
# Use random.sample to select 3 unique items from products without replacement
# and to be used for a brief usability survey.
unique_products = random.sample(products, k=3)
print(f"The three products for our usability survey are: {unique_products}")

# ----- c) Randomized Product Display -----
# Use random.shuffle() to shuffle the products list. For a presentation, all products
# should be displayed in a randomized order to avoid any appearance of ranking.
random.shuffle(products)
print(f"All products: {products}")

# ----- d) Simulated Daily Transaction Count -----
# Use random.randit() to generate a simulated daily transaction count between 50 
# and 300, and print the result with a label.
simulated_transaction = random.randint(50, 300)
print(f"Randomly selected transaction count: {simulated_transaction}")