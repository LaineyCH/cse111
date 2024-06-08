"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""

import math
from datetime import date

subtotal = 0
while True :
    print()
    item_price = float(input("Please enter the item price: $"))
    if item_price == 0: 
        break
    quantity = float(input("Please enter the quantity: "))
    line_price = item_price * quantity
    subtotal += line_price

print()
print(f"Subtotal:       ${subtotal: .2f}")

today = date.today()
weekday = today.weekday()
discount = 0

if weekday == 5 or weekday == 2:
    if subtotal >= 50:
        discount = subtotal * 0.1
        subtotal -= discount
        print(f"Discount:       ${discount: .2f}")
        print(f"After discount: ${subtotal: .2f}")
    else: 
        discount = 0
        shortfall = 50 - subtotal
        print(f"If you spent ${shortfall: .2f} more, you could get a 10% discount.")

tax = subtotal * 0.06
total = subtotal + tax

print(f"Tax:            ${tax: .2f}")
print(f"Total:          ${total: .2f}")
print()

