# ==================================
# Lab 3
# Script 1: Creating a Dictionary
# ==================================

# Question 1: Define a dictionary named contact_info that includes the following 
# keys and the sample values of your choice: name, address, city, state, zip

contact_info = {
    "name": "Oscar Ramos",
    "address": "215 60th St",
    "city": "West New York",
    "state": "New Jersey",
    "zip": "07093"  # stored as a string, not an integer, because zip codes can have 
                    # leading zeros and you can't do math on a zip code
}

# ---------------------------------------------------------------
# Question 2: Print the address as properly formatted for mailing. Avoid using multiple 
# print statements. 

print(f"""
Name: {contact_info["name"]}
Address: {contact_info["address"]}
City: {contact_info["city"]}
State: {contact_info["state"]}
Zip: {contact_info["zip"]}
""")
# Triple quotes """ preserve line breaks automatically so \n is not needed.

# Output
# Name: Oscar Ramos
# Address: 215 60th St
# City: West New York
# State: New Jersey
# Zip: 07093

# ---------------------------------------------------------------
# Question 3: Remove the key:value pair for name.

del contact_info["name"]
print(contact_info)
# del permanently removes the key:value pair from the dictionary.
# Unlike .pop(), which removes and returns the value, del just deletes it.


# Output
# {'address': '215 60th St', 'city': 'West New York', 'state': 'New Jersey', 'zip': '07093'}

# ---------------------------------------------------------------
# Question 4: Add a new variable for full_name and assign its value as a dictionary 
# containing two key:value pairs. The first key:value pair should contain the key "first name"
# and a first name, and the second should contain the key "last name" and a last name.

full_name = {
    "first name": "Oscar",
    "last name": "Ramos"
}

# ---------------------------------------------------------------
# Question 5: Use the .update() method to add one more key:value pair to full_name, 
# with the key "honorific" and the value set to Mr. / Ms. / Mx. / Dr. / Hon. / etc.

full_name.update({"honorific": "Mr."})
print(full_name)
# .update() can both add new keys AND overwrite existing ones if the key already exists.

# Output: {'first name': 'Oscar', 'last name': 'Ramos', 'honorific': 'Mr.'}

# ---------------------------------------------------------------
# Question 6: Use the .update() method to add full_name to contact_info.

contact_info.update(full_name)
print(contact_info)

# Output: {'address': '215 60th St', 'city': 'West New York', 'state': 'New Jersey', 'zip': '07093', 'first name': 'Oscar', 'last name': 'Ramos', 'honorific': 'Mr.'}

# ---------------------------------------------------------------
# Question 7: Print the formatted address again, updating as needed to include the 
# new dictionary items.

print(f"""
{contact_info["honorific"]} {contact_info["first name"]} {contact_info["last name"]}
Address: {contact_info["address"]}
City: {contact_info["city"]}
State: {contact_info["state"]}
Zip: {contact_info["zip"]}
""")

# Output
# Mr. Oscar Ramos
# Address: 215 60th St
# City: West New York
# State: New Jersey
# Zip: 07093