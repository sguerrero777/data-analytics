# ============================================================
# Exercise 2.C Creating and Calling Functions
# Lab 2: Functions for Mail Organization
# ============================================================

# ----- Address Label Function -----
# Creating the function
def display_mailing_label(name, address, city, state, zip):
    return(
        (f"{name}\n{address}\n{city} {state} {zip}")
    )

# a) Call display_mailing_label() at least twice with data for two different people.
print(display_mailing_label('Oscar Ramos', '215 60th St', 'West New York', 'NJ', '07093'))
print(display_mailing_label('Leonardo Guerrero', '6817 Smith Ave', 'North Bergen', 'NJ', '07047'))

# ----- Adding Numbers Argument -----
def add_numbers(*args): # *args accepts any number of arguments and stores them as a tuple instead of a list because we don't want the input to change
    result = sum(args) # calculates the total of the arguments and sotring it in result to be resuable later
    equation = " + ".join(str(n) for n in args) # n isn assigned to each parameter or item in args
    # for n in args loops through each variable and converts them to a string with .join concatenating them
    # with "+", which is the separator for each varaible or item n. it converts them to string for display because the
    # math was already done in result
    return(f"{equation} = {result}") 
    # result2 goes first because thats how math expressions display, with the equation first
    # and result at the end of the operator.

# b) Call add_numbers() three times with one number, two numbers, and your choice of 
#    however many numbers (more than two). 
print(add_numbers(7))
print(add_numbers(7,7))
print(add_numbers(7,7,7))

# ----- Receipt Function ------------
def display_receipt(total_due, amount_paid):
    remaining_balance = total_due - amount_paid
    change = amount_paid - total_due
    if amount_paid < total_due:
        return(f"Total Due: ${total_due:.2f}\nAmount Paid: ${amount_paid:.2f}\nRemaining Balance: ${remaining_balance:.2f}\n")
    elif amount_paid == total_due:
        return(f"Total Due: ${total_due:.2f}\nAmount Paid: ${amount_paid:.2f}\nThank you, no change due!\n")
    else:
        return(f"Total Due: ${total_due:.2f}\nAmount Paid: ${amount_paid:.2f}\nChange Due: ${change:.2f}\n")
# building the formatting inside the function in return statements eliminates the need to rewrite it in print 
# statememnt, the function will do it for us when it's called with values.

# c) Call display_receipt() three times. The first time, overpay the bill. The second 
#    time, pay the bill exactly. The third time, underpay the bill.
# Pay Exact Amount
print(display_receipt(100, 100))

# Over-Pay
print(display_receipt(100, 150))

# Underpay
print(display_receipt(100, 70))