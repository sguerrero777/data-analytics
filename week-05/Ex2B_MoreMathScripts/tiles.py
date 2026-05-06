# ==================================
# Lab 1 (continued)
# Script 5: Tiling a Room
# ==================================

# Brainstorm: How can you calculate the total boxes you need to tile a room?

# You are going to tile a room whose dimensions are length by 
# width feet. There are 12 tiles per box, each 1 foot by 1 foot.
# You also want to buy at least 10% more tiles to handle chips, 
# breakage, and mess-ups. To figure out the number of boxes I need,
# four variables are needed. One for length, one for width, and one 
# for how many tiles come in one box. Since each tile is 1 foot 
# by 1 foot, the area of the room automatically implies the amount 
# of tiles I need.

# =============================================================

# Final Script for Tiling Room

# Define tile area
length = 20
width = 25
tiles_per_box = 12 

# Calculate the unknowns

import math 

total_tiles = length * width
extra_tiles = total_tiles * 0.10 # I need at least 10% more tiles. Stored as a decimal.
tiles_with_extra = total_tiles + extra_tiles
boxes_needed = math.ceil(tiles_with_extra / tiles_per_box)
# Ceil function rounds up to nearbest whole number, in this case to nearest full box.

# Display the results
print(f'The area of the room is {total_tiles}.')
print(f'The total number of boxes I need to tile this room with backup tiles are {boxes_needed}')

# Output: 
# The area of the room is 500.
# The total number of boxes I need to tile this room with backup tiles are 46.