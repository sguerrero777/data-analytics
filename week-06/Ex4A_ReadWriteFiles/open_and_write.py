# ============================================================
# Exercise 4.A Practicing Read/Write
# Lab 1: File Handling
# ============================================================

# "a" (append) mode is used instead of "w" (write) to protect existing content
# "w" would wipe everything if the script ran twice
# "a" always adds to the end, never deletes existing content
with open("about_me.txt", "a") as file:
    pass # passed is used as a placeholder, nothing 
         # has been written in the file yet

with open("about_me.txt", "a") as file:
    file.write("If you could do anything for your perfect night out, where would you go and what would you do?\n\n")
    file.write("My perfect night out would be at an amusement park a cool summer evening with my friends and boyfriend.")