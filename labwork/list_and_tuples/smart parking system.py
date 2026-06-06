# Smart parking system 

'''
Where: 
   • 1 = Occupied  
   • 0 = Available 
    
 Write a program to: 
     • Count occupied and available slots.  
     • Find the first available slot.  
     • Display all available slot numbers.  
     • Check whether parking occupancy exceeds 75%. '''

slots = [1, 0, 1, 1, 0, 0, 1, 0] 

# Count occupied and available slots.  
print("------------------------------------------")
occupied_count = 0
available_count = 0

for i in slots:
    if i == 1 :
        occupied_count += 1
    else:
        available_count += 1

print("Occupied : ",occupied_count)
print("Available : ",available_count)
print("------------------------------------------")

# or i in sloFind the first available slot.
for i in range(len(slots)):
    if slots[i] == 0:
        first_available = i+1
        break
print(" first available slot : ",first_available)
print("------------------------------------------")

# Display all available slot numbers
available_slots = []
for i in range(len(slots)):
    if slots[i] == 0:
        available_slots.append(i+1)

print("All available slots :",available_slots)   
print("------------------------------------------")

# Check whether parking occupancy exceeds 75%.  
occupied = (occupied_count / len(slots)) * 100 

print("bus occupied in percentage :",occupied)

if occupied < 70:
    print("Not More Than 75% Occupied")
else:
    print(" More Than 75% Occupied")
   