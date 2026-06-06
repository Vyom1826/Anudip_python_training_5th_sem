# Employee Performance Evaluation using tuple

'''Where:
   • First value = Employee ID 
   • Second value = Employee Name  
   • Third value = Performance Score  
   
   Tasks Write a Python program to: 
   1. Display details of employees scoring 80 or above.  
   2. Count the number of employees who need improvement (score below 60).  
   3. Find the employee with the highest score.  
   4. Create a list containing the names of all employees scoring above 75.  
   5. Display the performance category for each employee:  
          o 90 and above → Excellent  
          o 75 to 89 → Good  
          o 60 to 74 → Average  
          o Below 60 → Needs Improvement  '''

employees = (    
     ("E101", "Anuj", 92),     
     ("E102", "Rahul", 76),     
     ("E103", "Priya", 58),     
     ("E104", "Neha", 88),     
     ("E105", "Amit", 45) 
     ) 

count =0
max = employees[0][2]
new_list = []

# task 1  and  2 
print("---------------------------------------")
print("Employees scoring 80 or above")
for score in employees:
    if score[2] >= 80 :
        print(score[0],score[1],score[2])
    elif score[2] < 60:
        count += 1
print("----------------------------------------------")
print("Number of Employees need improvement : ", count)
print("----------------------------------------------")

# task 3
for score in employees:
    if max < score[2] :
        max = score[2]

for score in employees:
    if max == score[2] :
     print("Highest score : ",score[0],score[1],score[2]) 


print("----------------------------------------------")

# task 4
for score in employees:
    if score[2] > 75:
        new_list.append(score[1])

print("high performers : ",new_list)

print("------------------------------------------------")

for  score in employees:
    if score[2] >= 90:
        category = "Excellent"
    elif score[2] >= 75:
        category = "Good"
    elif score[2] >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    print(score[1], "--->" ,category)
