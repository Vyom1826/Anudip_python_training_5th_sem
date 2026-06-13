class Employee:
    def __init__(self):
        self.name = ""
        self.emp_id = 0
        self.salary = 0

    def accept_details(self):
        self.name = input("Enter employee name: ")
        self.emp_id = (input("Enter employee ID: "))
        self.salary = float(input("Enter employee salary: "))

    def display_details(self):
        print("\n----- EMPLOYEE DETAILS -----")
        print("Name      :", self.name)
        print("Employee ID :", self.emp_id)
        print("Salary     :", self.salary)
        print("Annual Salary :", self.annual_salary())
        self.increment()

    def annual_salary(self):
        return self.salary * 12
    
    def increment(self):
        increment_percentage = float(input("Enter the increment percentage: "))

        self.salary += (increment_percentage / 100) * self.salary
        print("Salary after increment:", self.salary)


# ---------------- MAIN PROGRAM ----------------
employee = Employee()

employee.accept_details()
employee.display_details()