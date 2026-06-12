'''Problem Statement
Daily mobile screen time (in minutes) of a student is recorded for 10 days.
Sample Data
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]
Tasks
1.
Calculate average screen time.
2.
Find the highest and lowest screen time.
3.
Count days exceeding 200 minutes.
4.
Display days with healthy usage (<180 minutes).
5.
Categorize usage:
o
Healthy (<180)
o
Moderate (180–240)
o
Excessive (>240)'''

screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# 1. Calculate average screen time.
average_time = sum(screen_time) / len(screen_time)
print("Average screen time:", average_time, "minutes")

# 2. Find the highest and lowest screen time.
highest_screen_time = max(screen_time)
lowest_screen_time = min(screen_time)
print("Highest screen time:", highest_screen_time, "minutes")
print("Lowest screen time:", lowest_screen_time, "minutes")

# 3.count days exceeding 200 minutes.
count = 0
for i in range(len(screen_time)):
    if screen_time[i] > 200 :
        count += 1

print("Days exceeding 200 minutes:", count)

# 4. Display days with healthy usage (<180 minutes).
print("Days with healthy usage (<180 minutes):")
for i in range(len(screen_time)):
    if screen_time[i] < 180:
        print("Day", i+1)

# 5. 5.Categorize usage:
print("Categorized usage:")
healthy_count = 0
moderate_count = 0
excessive_count = 0

for i in range(len(screen_time)):
    if screen_time[i] < 180:
        healthy_count += 1
        
    elif 180 <= screen_time[i] <= 240:
        moderate_count += 1
        
    elif screen_time[i] > 240:
        excessive_count += 1

print("Healthy:", healthy_count)
print("Moderate:", moderate_count)
print("Excessive:", excessive_count)