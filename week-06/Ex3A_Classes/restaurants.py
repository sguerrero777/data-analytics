# ============================================================
# Exercise 3.A Working with Classes
# Lab 1: Creating a Class for Restaurants
# ============================================================

# Notes Before I Begin:
# A class is a blueprint that defines what every object is created from and what it can do
# An object is like a variable that stores attributes (data about the object)
# and methods (functionality that the object can do, like change data about the object)

# class Restaurant:
#   '''Describes what the class does in English'''
    # docstring goes directly below the class name using triple quotes
    # can be printed using Restaurant.__doc__

# A method is a function that lives inside a class
# __init__ is the initializer method that sets up the attributes every object will have
# it runs automatically when a new object is created
# it always has self as the first parameter, plus any other attributes the object needs

# self is a parameter that always needs to be included as the first parameter in every method
# it tells Python which specific object is being set up or used at that moment
# every attribute also needs self. in front of it to mark it as belonging to that specific object
# without self, Python wouldn't know which object's data it's working with

#__init__ → setting up a new phone for the first time
# other methods → all the things you can DO with the phone after setup (call, text, take photos)

# method calls use dot notation
# object.method() (any extra parameter values would go inside)

class Restaurant: # Defining a Class
    ''' This class contains restaurant names and the type of food they serve.'''
    def __init__(self, rest_name, food_type): # Using the Initializer method to set up attributes rest_name and rest_food as fields
        self.rest_name = rest_name # Creating an attribute called rest_name, just setting up no real data yet
        self.food_type = food_type # Creating an attribute calles food_type
        # Self.rest_name = rest_name to make it clear that we are referencing this
        # specific method in the class

    # only needs self because it already has access to rest_name and food_type
    # through self - no need to pass them in again as parameters
    # self.rest_name and self.food_type were already set up in __init__
    def describe_rest(self): # Creating a method that will return the restuarant name and food it serves for every object
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Creating independent instances or objects where I put the real attributes/data values inside
# Instances always go otuside the class!
rest1 = Restaurant("Starbucks", "Coffee")
rest2 = Restaurant("McDonalds", "Fast-Food")
rest3 = Restaurant("Ani Ramen", "Japanese Food")

# Method calls
rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()

# Output
# Starbucks serves Coffee.
# Starbucks is open.
# McDonalds serves Fast-Food.
# McDonalds is open.
# Ani Ramen serves Japanese Food.
# Ani Ramen is open.