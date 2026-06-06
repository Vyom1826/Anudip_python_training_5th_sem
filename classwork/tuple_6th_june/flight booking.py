# A flight reservation system stores passenger records as tuples:
'''Where: 
• Passenger ID  
• Destination  
• Booking Status

Tasks :
    Write a Python program to: 
1. Display all passengers whose booking status is Confirmed. 
2. Count the number of passengers travelling to Delhi.  
3. Count Confirmed, Waiting, and Cancelled bookings separately.  
4. Create a list containing passenger IDs with Waiting status.  
5. Determine which destination has the highest number of bookings. '''

bookings = (     
    ("P101", "Delhi", "Confirmed"),     
    ("P102", "Mumbai", "Waiting"),    
    ("P103", "Delhi", "Confirmed"),     
    ("P104", "Chennai", "Cancelled"),     
    ("P105", "Mumbai", "Confirmed"),     
    ("P106", "Delhi", "Waiting") 
    ) 

count = 0
confirm = 0
waiting = 0
cancel = 0
waiting_list = []

print("---------------------------------------")
for i in bookings:
    if i[2] == "Confirmed":
       print(i[0],i[1])

for i in bookings:
    if i[1] == "Delhi":
       count += 1
print("----------------------------------------")
print("Passengers Travelling to Delhi : ",count)
print("----------------------------------------")

for i in bookings:
    if i[2] == "Confirmed":
        confirm += 1
    elif i[2] == "Waiting":
        waiting_list.append(i[0])
        waiting += 1
    else :
        cancel += 1

print("Confirmed : ",confirm)
print("Waiting : ",waiting)
print("Cancalled : ",cancel)
print("----------------------------------------")

print("Waiting list :",waiting_list)
print("----------------------------------------")
book = []
for i in bookings:
    book.append(i[1])

max_count = 0
most_booked = ""

for city in book:
    count = book.count(city)
    if count > max_count:
        max_count = count
        most_booked = city

print("Most Booked Destination:", most_booked)