"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are over $1,000, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
bonus = 0
bonus_percentage = 0
while sales >= 0:
    if sales < 1000:
        bonus_percentage = 0.10
    else:
        bonus_percentage = 0.15
    bonus = bonus_percentage * sales
    print("Your bonus is ${}".format(bonus))
    sales = float(input("Enter sales: $"))
print("Have a nice day.")
