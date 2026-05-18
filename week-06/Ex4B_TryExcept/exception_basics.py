# ============================================================
# Exercise 4.B Working with Exceptions
# Lab 1: Exception Basics
# ============================================================

# Notes Before I Begin:
# ValueError - right type but wrong value
# ex. int("hello") - "hello" is a string that can't be converted to int

# NameError - using a variable that doesn't exist/hasn't been defined yet
# ex. print(banana) - banana was never defined!

# TypeError - wrong type used for the operation
# ex. "hello" + 5 - can't add a string and an integer together

# SyntaxError - broken code structure, Python can't even read it
# ex. if x = 5: - should be == not =
# SyntaxError is tricky to catch with try/except because
# Python catches it BEFORE the code even runs!

# Flow:
# try: attempts the code that may raise an error (can also be user input)
# except ValueError: if a ValueError occurs, don't crash - handle it gracefully
# else: if no error occurs, print the result
# finally: always runs whether there's an error or not - use a neutral message

# ValueError
print("\n-------ValueError Demo-------")
try:
    num = int("Hello")          # tries to convert string to int - raises ValueError
except ValueError:
    print("ValueError: Oops, looks like you tried to assign a string as an integer.")
else:
    print(f"Good the number is {num}!")   # only runs if no error occurred
finally:
    print("Let's try another one...\n")  # always runs regardless of error or not

# NameError
print("-------NameError Demo-------")
try:
    print(chicken_wings)    # chicken_wings is a variable that was never defined  
except NameError:
    print("NameError: Oops, you tried to use a variable that hasn't been defined yet!")
else:
    print(f"Success! No NameError.")   
finally:
    print("Let's try another one...\n") 

# TypeError
print("-------TypeError Demo-------")
try:
    total = "cake" + 4
except TypeError:
    print("Oops. Looks like you tried to add a string and integer together.")
else: 
    print(f"Good! The total is {total}")
finally:
    print("Let try another one...\n")

# SyntaxError
print("-------SyntaxError Demo-------")
# SyntaxError cannot be caught with try/except because Python
# detects it before the code even runs!
# workaround: use eval() to attempt to run invalid syntax at runtime
try:
    eval("if age = 21: pass")   # eval() runs the string as code - = should be == causing SyntaxError
except SyntaxError:
    print("SyntaxError: Oops! Looks like you used = instead of == in your comparison.")
else:
    print("Good! No SyntaxError occurred.")
finally:
    print("Let's try another one...")
