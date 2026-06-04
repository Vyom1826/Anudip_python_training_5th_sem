#program to calculate electricity bill
units=int(input("Enter the number of units consumed: "))
while units<0:
    print("Please enter a positive integer")
    units=int(input("Enter the number of units consumed: "))

# Calculates unit consumption and bill amount based on the following rates:
# - For the first 100 units: Rs. 5 per unit 
# - For the next 100 units (101-200): Rs. 7 per unit
# - For units above 200: Rs. 10 per unit

if units<=100:
    bill=units*5
    print("low consumption")
elif units<=200:
    bill=100*5+(units-100)*7
    print("medium consumption")
else:
    bill=100*5+100*7+(units-200)*10
    print("high consumption")

    print("units consumed:",units)
print("Your electricity bill is: Rs.", bill)
