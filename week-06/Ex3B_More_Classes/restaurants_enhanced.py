# ============================================================
# Exercise 3.B More Fun with Classes
# Lab 1: Enhancing a Class for Restaurants
# ============================================================

# number_served and customer_ratings are default attributes, not parameters
# because they start with the same value for every restaurant (0 and [])
# unlike rest_name and food_type which are different for every restaurant

# IMPORTANT: never use [] as a default parameter in __init__
# all instances would share the same list - appending to rest1 would show in rest2!
# always set list attributes inside __init__ so each instance gets its own fresh list

class Restaurant: 
    '''This class collects customer experience data about every restaurant.'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name          # different for every restaurant - passed in as parameter
        self.food_type = food_type          # different for every restaurant - passed in as parameter
        self.number_served = 0              # same starting value for every restaurant - default attribute
        self.customer_ratings = []          # same starting value for every restaurant - default attribute

    def describe_rest(self): 
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers were served today?: "))
        self.number_served += customers
    
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served}")

    def customer_rating(self):
        rating = int(input("How would you rate your experience today on a scale of 1-5 (5 being excellent)?: "))
        if 1 <= rating <= 5:  # checks if rating is between 1 and 5 inclusive
            self.customer_ratings.append(rating)  # appends rating TO the list, passing rating IN
            avg = sum(self.customer_ratings) / len(self.customer_ratings)
            # avg is a local variable - no self needed because it only exists temporarily inside this method
            # self. is only needed for permanent attributes that persist across the whole object
            # len(self.customer_ratings) counts how many ratings are in the list
            # avg = sum of all ratings divided by how many ratings there are
            print(f"Your rating was {rating}.")
            print(f"The average rating for this restaurant is {avg:.2f}")
        else:
            print("Invalid rating. Please pick a rating 1-5.")

# Creating independent instances or objects where I put the real attributes/data values inside
# Instances always go outside the class!
rest1 = Restaurant("Starbucks", "Coffee")
rest2 = Restaurant("McDonalds", "Fast-Food")
rest3 = Restaurant("Ani Ramen", "Japanese Food")

# Method calls
print("===== Restaurant 1 =====")
rest1.describe_rest()
rest1.rest_open()
rest1.add_num_served()
rest1.print_num_served()
rest1.customer_rating()
rest1.customer_rating()
rest1.customer_rating()
print()

print("===== Restaurant 2 =====")
rest2.describe_rest()
rest2.rest_open()
rest2.add_num_served()
rest2.print_num_served()
rest2.customer_rating()
rest2.customer_rating()
rest2.customer_rating()
print()

print("===== Restaurant 3 =====")
rest3.describe_rest()
rest3.rest_open()
rest3.add_num_served()
rest3.print_num_served()
rest3.customer_rating()
rest3.customer_rating()
rest3.customer_rating()

# Output
# ===== Restaurant 1 =====
# Starbucks serves Coffee.
# Starbucks is open.
# How many customers were served today?: 20
# Starbucks has served 20
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 4
# Your rating was 4.
# The average rating for this restaurant is 4.00
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 3
# Your rating was 3.
# The average rating for this restaurant is 3.5
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 2
# Your rating was 2.
# The average rating for this restaurant is 3.00

# ===== Restaurant 2 =====
# McDonalds serves Fast-Food.
# McDonalds is open.
# How many customers were served today?: 15
# McDonalds has served 15
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 5
# Your rating was 5.
# The average rating for this restaurant is 5.00
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 4
# Your rating was 4.
# The average rating for this restaurant is 4.50
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 2
# Your rating was 2.
# The average rating for this restaurant is 3.67
 
# ===== Restaurant 3 =====
# Ani Ramen serves Japanese Food.
# Ani Ramen is open.
# How many customers were served today?: 10
# Ani Ramen has served 10
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 5
# Your rating was 5.
# The average rating for this restaurant is 5.00
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 5
# Your rating was 5.
# The average rating for this restaurant is 5.00
# How would you rate your experience today on a scale of 1-5 (5 being excellent)?: 4
# Your rating was 4.
# The average rating for this restaurant is 4.67