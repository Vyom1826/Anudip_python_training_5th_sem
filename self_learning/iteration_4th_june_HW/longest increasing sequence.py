# program to find the length of the longest increasing subsequence in a list of integers

n = int(input("Enter the number of elements in the list: ")) # input from user, number of elements in the list
print("Enter the elements of the list: ") # prompt user to enter the elements of the list

prev = int(input()) # input from user, first element of the list
count = 1 # initialize count of longest increasing subsequence to 1
max_count = 1 # initialize max_count to 1

for _ in range(1, n):
    curr = int(input()) # input from user, current element of the list
    if curr > prev:
        count += 1
    else:
        count = 1
    if count > max_count: # if count exceeds the maximum count found so far, update max_count
        max_count = count
    prev = curr

print("The length of the longest increasing subsequence is:", max_count)
