#program that calculates the total bill for a shopping cart
total_bill = 0  
while True:
    item_price = float(input("Enter the price of the item (or -1 to finish): "))
    if item_price == -1:
        break
    total_bill += item_price

print("Total bill: $", total_bill)