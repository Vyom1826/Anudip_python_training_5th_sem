#program to check whether a number is prime or not if not prime then find factor of that number

num=int(input("Enter a number: "))
while num<1:
    print("Please enter a positive integer")
    num=int(input("Enter a number: "))

if num>1:
    for i in range(2,int(num/2)+1):
        if (num%i)==0:
            print(num,"is not a prime number")
            print("Factors of",num,"are:")
            for j in range(1,num+1):
                if (num%j)==0:
                    print(j)
            break
    else:
        print(num,"is a prime number")