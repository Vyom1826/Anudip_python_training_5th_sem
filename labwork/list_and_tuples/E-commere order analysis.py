#An online store records orders as

'''Write a program to: 

• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. '''

orders = [     
    ("Laptop", 55000),     
    ("Mouse", 800),     
    ("Keyboard", 1500),     
    ("Monitor", 12000),     
    ("Pen Drive", 600) 
    ] 

print("---------------------------------------------")

#Display all products costing more than ₹1000.
print("All the products costing more than 1000 :")
for i in orders:
    if i[1] > 1000:
        print(i[0])

print("---------------------------------------------")

# Find the most expensive product. 
max = 0

for  i in orders:
    if max < i[1]:
      max = i[1]

for  i in orders:
    if max == i[1]:
     print("Most Expensive Item : ",i[0],"=>",max)

print("---------------------------------------------")

# Calculate the total order value.
sum = 0 

for i in orders:
   sum += i[1]

print("Total order value : ",sum)
print("---------------------------------------------")

# Count products costing below ₹1000 
count = 0 

for i in orders:
   if i[1] < 1000 :
      count += 1

print("Products costing below 1000 : ",count)
print("---------------------------------------------")