# ============================================================
# Sharleen Guerrero
# May 5, 2026
# Notes: Strings
# ============================================================


# Immutability -----------------------------------------------
name = "Hello"

print(f"Original string: {name}")
print(f"First character: {name[0]}")
name[0] = "J"
# not possible because strings are immutable


# Indexing and Slicing ---------------------------------------
string = "Hello, World!"

# every character in a string has a position number called an index
# indexing starts at 0, not 1
# H = 0, e = 1, l = 2, l = 3, o = 4, , = 5, (space) = 6, W = 7 ...

# Positive Indexing: First character
print(string[0])
# output: H

# Negative Indexing: Last character
# -1 starts from the end of the string
print(string[-1])
# output: !

# Slicing: From index 1 to 3 (4 is excluded)
# string[start:stop] -- stop index is never included
print(string[1:4])
# output: ell


# String Operations ------------------------------------------

# Concatenation
greeting = "Hello, " "World!"
print(greeting)
# output: Hello, World!

# Repetition
repeat = "Hello! " * 3
print(repeat)
# output: Hello! Hello! Hello!

# Membership Test
print("World" in greeting)
# output: True

# Convert to Uppercase
print(string.upper())
# output: HELLO, WORLD!

# Finding a Substring
# .find() searches inside the string for a word or character
# it returns the index where that word begins
print(string.find("World"))
# output: 7 -- "World" starts at index position 7

# Replacing a Substring
# .replace(old, new) finds the old word and swaps it with the new word
# it doesn't change the original string, it's creating a new one
print(string.replace("World", "Python"))
# output: Hello, Python!

# Splitting a String
# .split(delimiter) chops the string into pieces wherever it sees the delimiter
# the result is a list (square brackets)
# the delimiter (in this case the comma) gets removed from the result
print(string.split(","))
# output: ['Hello', ' World!']


# Practice: F-String with Classmate Names --------------------
# Store three classmate names and display using one f-string

name1 = "Sha'Rya Weaver"
name2 = "Marenza Santarin"
name3 = "Maia Black"

print(f'The names of three classmates are:\n {name1},\n {name2},\n {name3}.')


# Importing Math Module --------------------------------------
# Write a simple Python program that imports the Math module and display
# the value of pi. Try two ways, by importing Math and then access pi,
# and by importing pi as a specific constant and display without reference
# to the Math module. Format output to two decimal places.

# Way 1: Import the whole math module
import math
print(f"Pi = {math.pi:.2f}")

# Way 2: Import pi directly 
from math import pi
print(f"Pi = {pi:.2f}")