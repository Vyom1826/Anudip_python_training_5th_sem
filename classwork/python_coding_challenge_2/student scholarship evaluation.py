# Marks obtained by students

marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# 1. Display students scoring above 85 marks
print("Students scoring above 85 marks:")
for student, score in marks.items():
    if score > 85:
        print(student, ":", score)

# 2. Find the topper
topper = max(marks, key=marks.get)
print("\nTopper:")
print(topper, ":", marks[topper])

# 3. Find the student with the lowest marks
lowest_student = min(marks, key=marks.get)
print("\nStudent with lowest marks:")
print(lowest_student, ":", marks[lowest_student])

# 4. Calculate class average marks
average_marks = sum(marks.values()) / len(marks)
print("\nClass Average Marks:", round(average_marks, 2))

# 5. Generate grades
print("\nStudent Grades:")

grades = {}

for student, score in marks.items():

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 50:
        grade = "C"

    else:
        grade = "F"

    grades[student] = grade
    print(student, ":", grade)

# 6. Create a list of scholarship students
scholarship_students = []

for student, score in marks.items():
    if score >= 90:
        scholarship_students.append(student)

print("\nScholarship Students (Marks >= 90):")
print(scholarship_students)