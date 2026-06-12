'''Problem Statement
Delivery times (in minutes) for different orders are recorded below:
Sample Data
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
Tasks
1.
Find the fastest delivery time.
2.
Find the slowest delivery time.
3.
Calculate the average delivery time.
4.
Display delayed orders (>45 minutes).
5.
Categorize deliveries:
o
Fast (≤30 minutes)
o
Normal (31–45 minutes)
o
Delayed (>45 minutes)'''

delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Find the fastest delivery time.
fastest_time = min(delivery_times)
print("Fastest delivery time:", fastest_time, "minutes")

# 2. Find the slowest delivery time.
slowest_time = max(delivery_times)
print("Slowest delivery time:", slowest_time, "minutes")

# 3. Calculate the average delivery time.
average_time = sum(delivery_times) / len(delivery_times)
print("Average delivery time:", (average_time), "minutes")

# 4. Display delayed orders (>45 minutes).
delayed_orders = []
for time in delivery_times:
    if time > 45:
        delayed_orders.append(time)
print("Delayed orders (>45 minutes):\n", delayed_orders)

''' 5. Categorize deliveries:
o
Fast (≤30 minutes)
o
Normal (31–45 minutes)
o
Delayed (>45 minutes)'''

print("Categorized deliveries:")
fast_count = 0
normal_count = 0
delayed_count = 0

for time in delivery_times:
    if time <= 30:
        fast_count += 1
        

    elif 31 <= time <= 45:
        normal_count += 1
        

    elif time > 45:
        delayed_count += 1 

    else:
        delayed_count += 1
        print("Delayed delivery")   

print("Fast delivery :", fast_count) 
print("Normal delivery :", normal_count)
print("Delayed delivery :", delayed_count)