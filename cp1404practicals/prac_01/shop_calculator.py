"""
Calculate the total price of a user-inputted amount of items.
"""

number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    while price <= 0:
        price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))