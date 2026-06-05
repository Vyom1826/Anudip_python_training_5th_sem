# Electricity Bill Simulator

units = int(input("Enter the number of units consumed: "))

if units <= 100 :
    bill = units*5
elif units <= 200 :
    bill = 100*5 + (units-100)*7
elif units > 200 :
    bill = 100*5 + 100*7 + (units-200)*10

print("The total electricity bill is: Rs.", bill)

if bill > 5000 :
    print("You have to pay a surcharge of 10% on the bill.")
    bill = bill + (bill*0.10)
    print("This bill includes a surcharge of 10% as the total bill exceeds Rs. 5000.")
    print("The total electricity bill is: Rs.", bill)
else:
    print("The total electricity bill is: Rs.", bill)