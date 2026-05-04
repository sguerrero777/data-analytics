# Question 5 - First Program
print('Hello world!')

# Question 15 to 21 - Practice with Variables
message = 'Hello world!'
print(message)


# Hello world prints twice because there are two print calls.
# It is running the first line of code, where it prints 'Hello world!' directly.
# In line 4, it prints the variable called 'message', which stores 'Hello world!'
# as a string.



# Displaying dollars and cents
dollars = 3
cents = .50
print(dollars + cents)

# For this expression, I notice that the variables dollars
# and cents store their own numerical value. The operator in
# the expression performs math on both numbers, adding them 
# together so the result is 3.5 (3 +.50 = 3.5) It only prints
# the result of the expression, not the values of the variable
# because there is no print call for them.

cents = cents + .25
print(dollars + cents)

# Concatenating Strings
d_str = '3 dollars'
c_str = '50 cents'
print(d_str + ' ' + c_str)



