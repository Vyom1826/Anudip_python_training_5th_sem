#program for PIN verification
correct_pin = 1234

while True:
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        print("PIN verified successfully!")
        break
    else:
        print("Invalid PIN. Please try again.")
       