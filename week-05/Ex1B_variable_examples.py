# ===============================
# Lab 1
# ===============================

# Question 2 - Variables and Assumptions

# Customer ID 
customer_id = 1
# I used the full name customer_id for specificity.
            
# Customer Name
customer_name = 'Oscar Ramos'
# I wrote the full customer_name instead of two separate
# variables for first and last name to avoid having to 
# concatenate them later. 


# Customer's Gender
customer_gender = 'M'
# I stored the customer_gender as a single character string
# to match conventions; M for Male and F for Female.

# Customer Date of Birth
customer_dob = '19-10-1999'
# I stored the date as a string to avoid Python treating the
# dashes between day, month, and year as an arithmetic operator.

# Driver's license number
driver_license = 'A123456789'
# I wrote the full driver_license instead of just license because I
# learned license is a built-in Python constant. I also stored the
# license  number as a string because license numbers can 
# have both letter and numbers depending on state.

# Auto policy number
auto_policy = '123-456-7891'
# I wrote the auto_policy as a string for the same reason in customer_dob;
# I wanted to avoid Python treating the dashes as a subtraction operator.


# Question 4 - About Me Variables
name = 'Sharleen'
city = 'North Bergen'
state = 'NJ'


# ===============================
# Lab 2
# ===============================

# a) What is the full list of reserved words that can’t be used for variable names? 
''' 
List of reserved keywords in python: False, def, if, raise, None, del, import, return,
True, elif, in, try, and, else, is, while, as, except, lambda, with, assert, finally, 
nonlocal, yield, break, for, not, class, from, or, continue, global, pass
'''

# b) Pick 5 of these words and review the explanation for how it is used as a keyword in 
#    Python. Put ^^ around any terms that you are not familiar with. 

'''
1. class - Used to define a class in Python

2. def - Used to define a function or a method in Python

3. if - Used to make a conditional statement. If the 
condition is true, then a defined action is performed.

4. break - Used as a ^^control flow^^ statement to exit out of a loop.

5. while - Used to start a while loop. It continues 
iterating until a condition is no longer True.
'''