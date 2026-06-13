class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = []

    def accept_details(self):
        self.name = input("Enter student name: ")
        self.roll_no = int(input("Enter roll number: "))

        for i in range(1, 4):
            mark = float(input(f"Enter marks for Subject {i}: "))
            self.marks.append(mark)

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def display_report(self):
        print("\n----- STUDENT REPORT -----")
        print("Name      :", self.name)
        print("Roll No.  :", self.roll_no)

        for i in range(len(self.marks)):
            print(f"Subject {i+1} :", self.marks[i])

        print("Total Marks :", self.calculate_total())
        print("Percentage  :", round(self.calculate_percentage(), 2), "%")


# ---------------- MAIN PROGRAM ----------------

student = Student()

student.accept_details()
student.display_report()