# program that accepts a number and checks if it has consecutive digits

num = input("Enter a number: ")
while num > 0:
    print("Invalid input. Please enter a positive integer.")
    num = input("Enter a number: ")

is_consecutive = True

# using loop to check if each digit is consecutive to the next one 

for i in range(len(num) - 1):
    if int(num[i + 1]) != int(num[i]) + 1:  # in this we check the index to the next index
        is_consecutive = False
        break

if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")
