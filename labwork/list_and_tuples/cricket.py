# A batsman's scores in different matches are stored in a list.

'''Write a program to: 

• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score.  '''

scores = [45, 78, 12, 100, 67, 8, 90, 55] 
print("----------------------------------------------")
# Count half-centuries and centuries.  
half_count = 0
full_count = 0

for i in scores:
    if i >= 50 and i < 100 :
        half_count += 1
    elif i >= 100 :
        full_count += 1

print("Number of Half Centuries : ",half_count)
print("Number of Centuries : ",full_count)
print("----------------------------------------------")

# Find the highest score.
max = 0

for i in scores:
    if max < i :
        max = i 

print("Highest Score : ",max)
print("----------------------------------------------")

# Display all scores below 20.
print("Scores below 20")
for i in scores:
    if i < 20 :
        print(i)
print("----------------------------------------------")

# Calculate the average score.  
average = 0 

for i in scores:
    average += i
average = average/len(scores)
print("Average score : ",average)
print("----------------------------------------------")
