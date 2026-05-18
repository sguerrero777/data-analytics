# ============================================================
# Exercise 2.D Lambdas and Generators
# Lab 1: Using Lambdas and Generators in Functions
# ============================================================

# a) Creating a variable names doubler that uses a lambda funtion to double whatever
#    argument it recieves
doubler = lambda n: n * 2
# doubler stores the function as a variable to be able to call later
# lambda is the key word that creates the function
# n is the parameter
# : is the return
# n*2 is what the lambda function is doing to the parameter

# b) Print the variable multiple times to test it out with the following values:
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Output:
# 16
# -8
# bananabanana

# c) Create a tripler variable using similar logic but multiplying the supplied argument by 3
#    instead of 2, and test it out with the same sample values.
tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# Output:
# 24
# -12
# bananabananabanana

# d) Create a multiplier() function and use it to create the variables.
def multiplier(x):           # outer function
    return lambda n: n * x   # inner function (lambda) being stored and returned
# whatever n is, its mupltiplied by x

# Multiplier variables for numbers 4-10 and print tests
quadrupler = multiplier(4)  # creates the variable, x = 4 and runs the multiplier function
print(quadrupler(8))        # this is when the lambda runs

quintupler = multiplier(5)
sextupler  = multiplier(6)
septupler  = multiplier(7)
octupler   = multiplier(8)
nonupler   = multiplier(9)
decupler   = multiplier(10)

print(quintupler(8))
print(sextupler(8))
print(septupler(8))
print(octupler(8))
print(nonupler(8))
print(decupler(8))

# Output
# 32
# 40
# 48
# 56
# 64
# 72
# 80