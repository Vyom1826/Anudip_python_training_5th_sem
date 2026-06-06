''' program A bus has seats represented as: 
Where: 
• 1 → Seat Booked  
• 0 → Seat Available  '''

seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 

booked_count = 0 
available_count = 0
available_seat = []

for i in seats:
    if i == 1:
        booked_count += 1
    else:
        available_count += 1

print("Booked Seats :",booked_count)
print("Available Seats :",available_count)

#for the first available seat 
for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i+1
        break

print("First available seat :",first_available)

#
for i in range(len(seats)):
    if seats[i] == 0:
        available_seat.append(i+1)

print("All available seats :",available_seat)

occupied = (booked_count / len(seats)) * 100 

print("bus occupied in percentage :",occupied)

if occupied < 70:
    print("Not More Than 70% Occupied")
else:
    print(" More Than 70% Occupied")
   