# progarm for ATM Transtion history of depoite 

transitions = [5000 , -2000 , 3000 , -1000 , -500 , 7000]
sum = 0
Deposite = []
Withdrawal = []
max = transitions[0]
min = transitions[0]

for i in transitions:
    if max < i:
        max = i
    if min > i:
        min = i

    sum = sum + int(i)
    if i > 0:
        Deposite.append(i)
    else:
        Withdrawal.append(i)

print("Current balance",sum)


print("Deposite:",Deposite)
print("Withdrawal:",Withdrawal)
print("Highest deposite",max )
print("Highest withdrawal",min)