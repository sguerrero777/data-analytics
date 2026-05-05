# Sharleen B. Guerrero
# 05-04-2026


# Syntax Errors
# ------------------------------------------------------------
print('Hello")
# mismatched quotes (opening quote is single, closing is double)


# Reserved Keywords
# ------------------------------------------------------------
import keyword
print(keyword.kwlist)
# anything from the list can't be used as a variable name


# Type Function
# ------------------------------------------------------------
type(25)
# output: <class 'int'>

type(Python)
# error: Python thinks Python is a variable, to check the type of a string it must be in quotes

type('Python')
# output: <class 'str'>


# Exploring Arithmetic Operators
# ------------------------------------------------------------

2 + 3    # addition: adds two numbers

3 - 1    # subtraction: subtracts one number from another

2 * 5    # multiplication: multiplies one number by another

10 / 5   # division: divides one number by another and gives the result as a floating-point number

10 // 3  # floor division: divides one number by another and gives the result as a whole number

10 % 2   # modulus: divides one number by another and gives the remainder

5 ** 2   # exponentiation: raises a number to a power
