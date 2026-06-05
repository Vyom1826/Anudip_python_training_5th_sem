# program take a input of 20 number 
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Taking a num which user want to remove the duplicates from the list
num_to_remove = int(input("Enter a number to remove from the list: "))

# Removing duplicates of the num_to_remove from the list
count = numbers.count(num_to_remove)
if count == 0:
    print(num_to_remove, "is not present in the list.")
elif count == 1:
    print(num_to_remove, "is present in the list but has no duplicates.")
else:
    numbers.reverse() # reverse the list to remove duplicates from the end
    for i in range(1, count):
        numbers.remove(num_to_remove) # remove the num_to_remove from the list

        numbers.reverse() # reverse the list back to original order

        print("After removing duplicates of", num_to_remove, ":", numbers)
    