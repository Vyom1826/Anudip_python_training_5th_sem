'''Problem Statement
Patient heart rates are recorded below.
Sample Data
heart_rate = { "P101": 72, 
"P102": 105, 
"P103": 88, 
"P104": 120, 
"P105": 65, 
"P106": 98, 
"P107": 110, 
"P108": 70, 
"P109": 85, 
"P110": 130 }
Tasks
1.
Display critical patients (heart rate >100).
2.
Find highest and lowest heart rate.
3.
Calculate average heart rate.
4.
Count stable patients (60–100 bpm).'''

heart_rate = { "P101": 72, 
"P102": 105, 
"P103": 88, 
"P104": 120, 
"P105": 65, 
"P106": 98, 
"P107": 110, 
"P108": 70, 
"P109": 85, 
"P110": 130 }

# 1. Display critical patients (heart rate >100).
print("critical patients (heart rate >100):")
for patient, rate in heart_rate.items():
    if rate > 100:
        print(patient)

# 2.find highest and lowest heart rate.
highest_rate = max(heart_rate , key=heart_rate.get)
lowest_rate = min(heart_rate , key=heart_rate.get)
print("Highest heart rate:\n", highest_rate,":", heart_rate[highest_rate])
print("Lowest heart rate:\n", lowest_rate ,":",heart_rate[lowest_rate])

# 3. calculate average heart rate.
average_rate = sum(heart_rate.values()) / len(heart_rate)
print("Average heart rate:", average_rate)

# 4. Count stable patients (60–100 bpm).    
stable_count = 0
for patient, rate in heart_rate.items():
    if 60 <= rate <= 100:
        stable_count += 1

print("Stable patients (60–100 bpm):", stable_count)