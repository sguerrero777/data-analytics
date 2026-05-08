# =======================================================
# The for Loop
# input(), for loop, if-elif-else, f-strings
# Sharleen Guerrero
# =======================================================

# =============================================================
# LOOP ANATOMY — Know Before You Start
# =============================================================

# ── Three for-loop forms you will use in this exercise set ──────────
# Form 1 — iterate over a list (Problem 1, 2)
# for item in my_list:
#   print(f'{item}')

# Form 2 — iterate a fixed number of times with range() (Problem 3, 4)
# for i in range(1, n+1):
# i counts 1, 2, 3 ... n

# Form 3 — iterate over collected inputs (Problem 5)
#for item in collected_list:
#   if item > threshold:
# print(f'{item:.2f} is above threshold')

# Key rule: indent EVERYTHING inside the for block
# f-string formatting: {value:.2f} = 2 decimal place
# A foor loop does NOT need a counter variable because Python handles iteration automatically.

# =============================================================
# PROBLEM 1 — Sales Performance Report
# =============================================================

# Collect the number of sales representatives and their monthly sales figures.
# Use a for loop to process each rep, classify their performance with if/elif/else,
# and print a formatted report card with all money values to 2 decimal places.

n = int(input('How many sales reps?: '))
sales_reps = []
# n stores how many reps the user wants to enter
# sales_reps is an empty list that will hold everyones info

for _ in range(n):
    name = input('Rep name:').strip()
    sales = float(input('Monthly sales ($): '))
    sales_reps.append((name, sales))
# loop 1: repeats n times, once for each rep
# asks for name and sales each time
# strip() removes accidental spaces from the name
# append() pairs name and sales together and adds them to the list

print(' ── Sales Performance Report ──────────────────────────')
# prints the report header using unicode characters for the lines

for name, sales in sales_reps:
    if sales >= 5000:
        rating = 'Excellent'; bonus = sales * 0.10
    elif sales >= 3000:
        rating = 'Good'; bonus = sales * .05
    else:
        rating = 'Needs Improvement'; bonus = 0.0
    print(f' {name:<8} | Sales: ${sales:.2f} | {rating:<18} | Bonus: ${bonus:.2f}')
# prints each reps report card in a clean formatted line
# :<8 and :<18 left align the name and rating so columns line up
# Indent the print so it runs for every rep
# loop 2: goes through the list we built in loop 1
# unpacks each pair into name and sales
# checks sales top to bottom, stops at first true condition
# assigns a rating and calculates bonus based on performance

print(f' {name:<8} | Sales: ${sales:.2f} | {rating:<18} | Bonus: ${bonus:.2f}')
# prints each reps report card in a clean formatted line
# :<8 and :<18 left align the name and rating so columns line up

total = sum(s for _, s in sales_reps)
# adds up all the sales numbers from the list
# _ ignores the name, s grabs just the sales number

print(' ' + '-' * 56)
# prints a divider line to make the report look clean

print(f' Team Total: ${total:.2f}')
# prints the total sales for the whole team

# Output
# How many sales reps?: 3
# Rep name:Maya
# Monthly sales ($): 6200
# Rep name:Leo
# Monthly sales ($): 3450
# Rep name:Sam
# Monthly sales ($): 2100
# ── Sales Performance Report ──────────────────────────
# Maya     | Sales: $6200.00 | Excellent          | Bonus: $620.00
# Leo      | Sales: $3450.00 | Good               | Bonus: $172.50
# Sam      | Sales: $2100.00 | Needs Improvement  | Bonus: $0.00
# Sam      | Sales: $2100.00 | Needs Improvement  | Bonus: $0.00
# --------------------------------------------------------
# Team Total: $11750.00

