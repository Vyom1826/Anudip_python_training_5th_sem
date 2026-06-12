'''Problem Statement
An online store maintains stock quantities of products.
Sample Data
inventory = { "Laptop": 15, "Mouse": 45, "Keyboard": 32, "Monitor": 12, "Headphones": 28, "Printer": 8, "Webcam": 20, "Speaker": 18, "Tablet": 10, "Router": 25 }
Tasks
1.
Display products with stock below 15 units.
2.
Find the product with maximum stock.
3.
Find the product with minimum stock.
4.
Calculate total stock available.
5.
Create a list of products requiring restocking (<10 units).'''

inventory = { "Laptop": 15, 
             "Mouse": 45, 
             "Keyboard": 32, 
             "Monitor": 12, 
             "Headphones": 28, 
             "Printer": 8, 
             "Webcam": 20, 
             "Speaker": 18, 
             "Tablet": 10, 
             "Router": 25 
             }

# 1. Display products with stocks below 15 units.
print("Products with stocks below 15 units:")
for product, stock in inventory.items():
    if stock < 15:
        print(product)

# 2. Find the product with maximum stock.
max_stock_product = max(inventory, key=inventory.get)
print("\nProduct with maximum stock:")
print(max_stock_product, ":", inventory[max_stock_product])

# 3. Find the product with minimum stock.
min_stock_product = min(inventory, key=inventory.get)
print("\nProduct with minimum stock:")
print(min_stock_product, ":", inventory[min_stock_product],"Units")

# 4. Calculate total stock available.
total_stock = sum(inventory.values())
print("\nTotal stock available:", total_stock)

# 5. create a list of products requiring restocking(<10 units)
print("\nProducts requiring restocking (<10 units):")
restocking_products = []

for products, stock in inventory.items():
    if stock < 10 :
        restocking_products.append(products)

print(restocking_products)
