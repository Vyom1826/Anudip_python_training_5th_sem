'''Problem Statement: Design a Vehicle class containing: 
    • Vehicle Number  
    • Vehicle Type  
    • Rent per Day  
    
    Implement methods to: 
    • Accept vehicle details.  
    • Calculate total rental amount based on the number of days rented.  
    • Display the bill.  '''

class Vehicle: 
    def __init__(self):
        self.vehicle_number = ""
        self.vehicle_type = ""
        self.rent_per_day = 0
        self.days_rented = 0
    
    def accept_details(self):
        self.vehicle_number = input("Enter vehicle number: ")
        self.vehicle_type = input("Enter vehicle type: ")
        self.rent_per_day = float(input("Enter rent per day: "))
        self.days_rented = int(input("Enter number of days rented: "))
    
    def calculate_total_amount(self):
        return self.rent_per_day * self.days_rented
    
    def display_bill(self):
        print("\n----- VEHICLE BILL -----")
        print("Vehicle Number :", self.vehicle_number)
        print("Vehicle Type   :", self.vehicle_type)
        print("Rent per Day   :", self.rent_per_day)
        print("Days Rented    :", self.days_rented)
        print("Total Amount   :", self.calculate_total_amount())


# ---------------- MAIN PROGRAM ----------------
vehicle = Vehicle()

vehicle.accept_details()
vehicle.display_bill()