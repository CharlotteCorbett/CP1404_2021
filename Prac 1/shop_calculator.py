"""
CP1404- Practical 1
Charlotte Corbett
Shop Calculator
Pseudocode:
Get number of items
If number of items is less than 0:
    while number of items is less than 0:
        Display error message
        Get number of items
For each item:
    Calculate price of item
    Calculate total price of items
If total is greater than $100:
    Calculate discounted price
Display number of items and total price
"""
# Constants
discount = 0.1

# Set up an accumulator variable
total_price = 0.0

# Get number of items
number_of_items = int(input("Number of items: "))
# Input validation loop condition for number of items
if number_of_items < 0 or number_of_items == -0:
    while number_of_items < 0 or number_of_items == -0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
# Get item prices and accumulate them
for each_item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price -= (total_price * discount)
print("Total price for", number_of_items, "items is ${:.2f}".format(total_price))
