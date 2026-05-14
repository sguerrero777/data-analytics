# ============================================================
# Exercise 2.B Using Library Functions
# Lab 3: Statistics Module
# ============================================================

import random
import math
import statistics

vals_1_100 = range(1,100) 
vals_sample = random.sample(vals_1_100, 75) 
vals_choices = random.choices(vals_1_100, k = 200)  
radius = random.randint(3,10)  
pi = math.pi 

# ------------- Experimenting with a Subset of Integers 1-100: --------------------
sum_random = sum(vals_sample)
avg_random =  statistics.mean(vals_sample)
median_random = statistics.median(vals_sample)
# vals_sample gets 75 random values without replacement from the range established in vals_1_100.
# By separating the range into its own variable, if we ever need to change the range
# we only have to update it in one place and both vals_sample and vals_choices will use it automatically.

print(
    f"_Experimenting with a Subset of Integers 1-100:\n"
    f"Sum of Random 75 Sample Values: {sum_random}\n"
    f"Average of Random 75 Sample Values: {avg_random}\n"
    f"Median of 75 Sample Values: {median_random}"
)

# Output
# _Experimenting with a Subset of Integers 1-100:
# Sum of Random 75 Sample Values: 3733
# Average of Random 75 Sample Values: 49.77333333333333
# Median of 75 Sample Values: 49

# ------------- Experimenting with a Superset of 200 values, integers 1-100: ------
avg_200 = statistics.mean(vals_choices)
median_200 = statistics.median(vals_choices)
mode_200 = statistics.mode(vals_choices)
stdev_200 = statistics.stdev(vals_choices)
variance_200 = statistics.variance(vals_choices)
# vals_choices pulls 200 values from the same pool of 99 numbers in vals_1_100,
# but with replacement, meaning the same number can be picked more than once
print('\n')
print(
    f"_Experimenting with a SuperSet of 200 Values:\n"
    f"Average of 200 values: {avg_200}\n"
    f"Median of 200 values: {median_200}\n"
    f"Mode of 200 values: {mode_200}\n"
    f"Standard deviation of 200 values: {stdev_200}\n"
    f"Variance of 200 values: {variance_200}"
)

# Output:
# _Experimenting with a SuperSet of 200 Values:
# Average of 200 values: 50.92
# Median of 200 values: 51.5
# Mode of 200 values: 77
# Standard deviation of 200 values: 26.76857078570964
# Variance of 200 values: 716.5563819095478

# ------------- Modeling a Random Circle: -----------------------------------------

circle_area = (pi * radius ** 2)
rounded_up_area = math.ceil(circle_area) 
# .ceil rounds up to nearest integer
rounded_down_area = math.floor(circle_area)
# .floor rounds down to nearest integer

print("_Modeling a random circle:")
print("Radius =", radius, ", area =", rounded_up_area, "(rounded up to the nearest integer)")
print("Radius =", radius, ", area =", rounded_down_area, "(rounded down to the nearest integer)")

# Output:
# _Modeling a random circle:
# Radius = 7 , area = 154 (rounded up to the nearest integer)
# Radius = 7 , area = 153 (rounded down to the nearest integer)