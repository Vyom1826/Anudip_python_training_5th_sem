# program the number is strong number or not

num=int(input("Enter a number: "))
while num<0:
    print("Please enter a positive integer")
    num=int(input("Enter a number: "))

sum=0
temp=num

while temp>0:
    digit=temp%10
    factorial=1
    for i in range(1,digit+1):
        factorial*=i
    sum+=factorial
    temp//=10

if sum == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")