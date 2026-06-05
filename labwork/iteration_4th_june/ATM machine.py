# program to implement ATM machine
# input of pin number and amount to withdraw
# display in menu and ask for the option to withdraw , check balance , deposit and exit

initial_balance=10000

pin=int(input("Enter your pin number: "))
if(pin!=1234):  
    exit("Invalid pin number")

    # using while loop to display the menu and ask for the option to withdraw , check balance , deposit and exit
while True:
    print("1. Withdraw")
    print("2. Check balance")
    print("3. Deposit")
    print("4. Exit")

    # enter choice
    option=int(input("Enter your option: "))
   
    # using if else to perform the operations
    #FOR WITHDRAWAL
    if(option==1):
        amount=int(input("Enter the amount to withdraw: "))
        if(amount>initial_balance):
            print("Insufficient balance")
        else:
            initial_balance=initial_balance-amount
            print("Amount withdrawn successfully")
            print("Your current balance is: ",initial_balance)

     # FOR CHECKING BALANCE       
    elif(option==2):
        print("Your current balance is: ",initial_balance)

        # FOR DEPOSIT
    elif(option==3):
        amount=int(input("Enter the amount to deposit: "))
        initial_balance=initial_balance+amount
        print("Amount deposited successfully")
        print("Your current balance is: ",initial_balance)


    elif(option==4):
        exit("Thank you for using the ATM machine")
    else:
        print("Invalid option")






