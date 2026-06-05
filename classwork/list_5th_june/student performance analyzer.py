# program for students performance analyzer

marks = [78,45,92,35,88,40,99,56]
count = 0


# HIGHEST MARKS
max = marks[0]
for i in marks :
    if max < i:
        max = i
    else:
        max = max

 # LOWEST MARKS       
min = marks[0]
for i in marks:
    if min > i:
        min = i


 # PASSED STUDENT AND COUNT OF FAILED STUDENTS
for i in marks:    
    if i < 40 :
        marks.remove(i)
        count = +1
print("passed students:", marks )
print("failed count:",count)


#PRINTING MAX AND MIN
print("Highest marks:",max)
print("Lowest marks:",min)

new_marks = []

for i in marks:
    if i > 75:
        new_marks.append(i)

print("New list",new_marks)