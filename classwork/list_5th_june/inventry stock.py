# program to check inventry and alert the user , inventry alert system

stock = [25,5,0,12,3,18,0,30]
count = 0
available_count = 0
Restock_products = []
stock1 = []

for i in stock :
    if i == 0:
        count += 1
    if i < 10:
        Restock_products.append(i)
    if i > 0:
        available_count += 1
    if i > 15 :
        stock1.append(i)
print("Out of stock products:",count)
print("Restock_products:",Restock_products)
print("available stock:",available_count)
print("Healthy stock:",stock1)