'''Problem Statement: Create a Product class containing product name, 
quantity, and price per unit. Implement methods to: 
• Calculate total price.  
• Update quantity.  
• Display product details.  '''

class Product:
    def __init__(self,name ,quantity , price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print("Product Name :",self.name)
        print("Quantity :", self.quantity)
        print("Price per Unit :", self.price)
        print("Total Price :", self.calculate_total())

    def calculate_total(self):
        return self.quantity * self.price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Quantity updated successfully.")


# ---------------- MAIN PROGRAM ----------------
name = input("Enter product name: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))

product = Product(name, qty, price)

while True:
    print("\n---------- Shopping Cart ----------")
    print("1. Display Product Details")
    print("2. Update Quantity")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product.display()
    elif choice == 2:
        new_qty = int(input("Enter new quantity: "))
        product.update_quantity(new_qty)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
