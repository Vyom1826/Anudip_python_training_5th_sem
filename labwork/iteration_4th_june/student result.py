# Program to calculate student result that accepts marks of 5 subjects

marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    while mark < 0 or mark > 100:
        print("Please enter a valid mark between 0 and 100")
        mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "FALL"

print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Grade: {grade}")