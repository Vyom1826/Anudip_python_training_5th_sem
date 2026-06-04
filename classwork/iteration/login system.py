#program for login system
correct_username = "admin"
correct_password = "admin123"    

#loop until the user enters correct credentials 
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Please try again.")