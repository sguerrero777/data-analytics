# ==================================
# Lab 1
# Script 1: Movie List
# ==================================

# Question 2: Create a list with the titles of your favorite movies (or movies you’d 
# like to watch) – include at least 2, but no more than 10.  

movie_list = ["Hoppers", "Weapons", "Toy Story 5", "Shrek 5", "The Devil Wears Prada"]

# ---------------------------------------------------------------
# Question 3: Use the len() function to print the descriptive statement: 
# The list [list name] includes my top [length] favorite movies 

print(f'The list movie_list includes the {len(movie_list)} movies I want to watch.')
print(movie_list)

# Output
# The list movie_list includes the 5 movies I want to watch.
# ['Hoppers', 'Weapons', 'Toy Story 5', 'Shrek 5', 'The Devil Wears Prada']

# ---------------------------------------------------------------
# Question 4: Print a sorted list two ways (Note: make sure that your list items 
# aren’t already in alphabetical order to start with, or you won’t notice any difference):

# a) Use the sorted() function to print a sorted list, then print the list 
# again without using sorted() 

print(sorted(movie_list))
print(movie_list)

# Output
# ['Hoppers', 'Shrek 5', 'The Devil Wears Prada', 'Toy Story 5', 'Weapons']
# ['Hoppers', 'Weapons', 'Toy Story 5', 'Shrek 5', 'The Devil Wears Prada']

# What do you notice when you compare the two outputs?
# I notice that sorted() sorts the list alphabetically, but only temporarily, 
# it doesn't change the original list.

# b) Use the .sort() method to sort the list, then print the list again, like this: 
# listname.sort() 
# print(listname) 

movie_list.sort()
print(movie_list)

# Output
# ['Hoppers', 'Shrek 5', 'The Devil Wears Prada', 'Toy Story 5', 'Weapons']

# What do you notice when you compare the two outputs?
# I notice that .sort() is similar to sorted() in that it sorts the list alphabetically,
# but it does permanently change the original list.

# ---------------------------------------------------------------
# Question 5: Think of at least one more movie to add to your list, and use the 
# .append() method to add it. Then print the list again, also including an updated 
# description statement.

movie_list.append("Michael")
print(f'The list movie_list now includes {len(movie_list)} movies I want to watch.')
print(movie_list)

# Output
# The list movie_list now includes 6
# ['Hoppers', 'Shrek 5', 'The Devil Wears Prada', 'Toy Story 5', 'Weapons', 'Michael']

