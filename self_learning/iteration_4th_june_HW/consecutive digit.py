# program that accepts a number and checks if it has consecutive digits

num = input("Enter a number: ")

is_consecutive = True

for i in range(len(num) - 1):
    if int(num[i + 1]) != int(num[i]) + 1:
        is_consecutive = False
        break

if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")
