# checks the suspecious transitions detector 

high_count = 0
low_count = 0
total_amount = 0

while True:
    amount = int(input("Enter transaction amount (-1 to stop): "))

    if amount == -1:
        break

    total_amount = total_amount + amount

    if amount > 50000:
        high_count = high_count + 1

    if amount < 1000:
        low_count = low_count + 1

print("Transactions above ₹50,000:", high_count)
print("Transactions below ₹1,000:", low_count)
print("Total transaction amount:", total_amount)