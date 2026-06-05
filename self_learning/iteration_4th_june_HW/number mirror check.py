# program to check the second half of the number is equal to first half or not (mirror number or not)

num = input("Enter a number: ")

mid = len(num) // 2

left_half = num[:mid]
right_half = num[mid:]

if left_half == right_half:
    print("Mirror Number")
else:
    print("Not a Mirror Number")