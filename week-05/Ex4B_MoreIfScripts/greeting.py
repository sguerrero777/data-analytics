# ==================================
# Lab 2
# Script 2: Greeting
# ==================================

# Create a script that defines a variable that contains the current hour
# (0-23). Display one of the greetings below based on the current hour: 

# Time                     Greeting
# until 10:00am            Good morning!
# 10:00am until 5:00pm     Good day!
# 5:00pm or later          Good evening!

# ---------------------------------------------------------------

# Final Script for Retrieving Department Names

hour = int(input('What time is it?: '))

if hour < 10:
    print('Good morning!')
elif 10 <= hour < 17:
    print('Good day!')
# this check must come before good evening because elif hour >= 17 would catch
# all hours from 17 onward including 23, and python stops at the first true condition
# so the late night check would never be reached if good evening came first
elif hour >= 23 or hour < 4:
    print('What are you doing up so late?')
elif hour >= 17:
    print('Good evening!')
else:
    print('Invalid hour. Please re-enter using military time: ')


# Output:
# What time is it?: 15
# Good day!