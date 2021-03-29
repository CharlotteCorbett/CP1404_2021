"""
CP1404- Practical 1
Charlotte Corbett
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
Pseudocode:
Get user sales value
while user sales is greater than 0:
    If user sales are under $1000:
        Calculate 10% bonus.
        Display bonus in $.
    If sales are $1000 or more:
        Calculate 15% bonus.
        Display bonus in $.
    Display quit condition.
    Get user sales value
"""
# Constants
bonus_threshold = 1000
lower_bonus = 0.1
higher_bonus = 0.15

# Get user sales value
user_sales = float(input("Sales amount:$"))
while user_sales > 0:
    # If sales under $1000
    if user_sales < bonus_threshold:
        user_bonus = user_sales * lower_bonus
        print("Bonus:$", user_bonus)
    # If sales $1000 or more
    if user_sales >= bonus_threshold:
        user_bonus = user_sales * higher_bonus
        print("Bonus:$", user_bonus)
    # Display quit condition.
    print("Enter negative number to quit.")
    # Get user sales value
    user_sales = float(input("Sales amount:$"))