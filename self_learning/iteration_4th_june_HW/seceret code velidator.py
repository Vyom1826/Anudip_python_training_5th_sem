# program for secret code validator

secret_code = input("Enter the secret code: ") # input from user, secret code to be validated
if len(secret_code) != 6: # check if the length of the secret code is less than 6 or greater than 20 characters
    print("Invalid secret code. The code must be between 6 and 20 characters long.")
else:
    print("Valid secret code.")

# secret code validator , if the sum of first 3 characters is equal to the sum of last 3 characters
if len(secret_code) == 6:
    first_three = sum(int(char) for char in secret_code[:3]) # calculate the sum of the first three characters
    last_three = sum(int(char) for char in secret_code[3:]) # calculate the sum of the last three characters
    if first_three == last_three:
        print("The secret code is valid.")
    else:
        print("Invalid secret code. The sum of the first three characters must be equal to the sum of the last three characters.")