# ============================================================
# Exercise 4.A Practicing Read/Write
# Lab 1 cont.: File Handling
# ============================================================

# open() unlocks the file
# "about_me.txt" and "r" are arguments passed into open()
# "about_me.txt" → tells open() which file to open
# "r" → tells open() the mode (read only)
# "as file" is the variable name that stores the opened file object - can be named anything
# with statement automatically closes the file when done

#with open("about_me.txt", "r") as file:
#    content = file.read()  # .read() is a method called on the file object that reads ALL content and returns it as a string
#    print(content)         # content variable stores the full text to be displayed

# -----------------------------------------------------------------------------------------------------------------------

# with open("about_me.txt", "r") as file:
#    print(file.read(50))    
#    print(file.read(50))    

# The first .read(50) reads the first 50 characters.
# Name: Sharleen Guerrero
# Place of Birth: North Ber

# The second .read(50) reads the next 50 characters,
# continuing where we left off from the first .read(50)
# gen Did you have any pets growing up? What kind? 

# -----------------------------------------------------------------------------------------------------------------------

# with open("about_me.txt", "r") as file:
#   print(file.readline(10))  # first 10 characters of line 1
#   print(file.readline())    # rest of line 1? or line 2?

# The first .readline(10) read the first 10 characters.
# .readline() with the argument of 10 reads only 10 characters regardless 
# of where the line ends.
# Name: Shar

# The second .readline() finished the rest of the same line where left 
# off. readline() with no argument reads until the end of the current line.
# leen Guerrero

# -----------------------------------------------------------------------------------------------------------------------

# Task 13b - for loop using readline()
# with open("about_me.txt", "r") as file:
#    print(file.readline(10))
#    print(file.readline())
#    for i in range(1, 5):
#        print(file.readline())  # reads one full line at a time for 4 iterations

# Task 13c - Experiment with running all readline() statements together vs commenting out
# When all readline() statements run together, each one picks up where the last left off,
# reading through the file sequentially line by line.
# When one or more statements before the loop are commented out, the file cursor starts
# at an earlier position, so the loop reads different lines than before.
# This shows that readline() maintains a cursor position throughout the file,
# and each call advances that cursor to the next line.

# -----------------------------------------------------------------------------------------------------------------------

# Task 14 - readlines()
# a) print(file.readlines(1)) with no argument specified returns a list containing
#    the first line of the file as a string element, e.g. ['Name: Sharleen Guerrero\n']
#    The number 1 acts as a hint for the minimum bytes to read, but always completes the full line.

# b) Adding a second print(file.readlines(1)) continues from where the first left off,
#    returning the next line as a list, e.g. ['\n'] for a blank line or the next line of content.

# c) print(file.readlines(10)) reads lines until at least 10 characters have been read,
#    returning them as a list. It always completes full lines even if that means reading
#    more than 10 characters.

# d) Commenting out the first two readlines(1) statements and running readlines(10) twice:
#    The first readlines(10) starts from the beginning of the file and reads lines until
#    10 characters are covered. The second readlines(10) continues from where the first left off.

# e) readlines(100) reads lines until at least 100 characters have been read, returning
#    them as a list of complete lines. readlines(-1) reads ALL remaining lines in the file
#    and returns them as a list, similar to readlines() with no argument.

# -----------------------------------------------------------------------------------------------------------------------

# Task 15 & 16 - Combining Read Methods
with open("about_me.txt", "r") as file:
    first_50 = file.read(50)                    # a) first 50 characters
    next_4_lines = []
    for i in range(1, 5):
        next_4_lines.append(file.readline())    # b) next 4 lines appended to list
    rest = file.readlines(100)                  # c) next 100 characters worth of lines as list

print(f"First 50 characters: {first_50}\n")
print(f"Next four lines, as list by line: {next_4_lines}\n")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {rest}")