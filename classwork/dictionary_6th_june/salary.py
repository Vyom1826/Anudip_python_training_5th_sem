# Create a dictionary for 10 employees
employees = {}

for i in range(10):
    emp_id = input(f"Enter Employee ID {i+1}: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = salary

# Count employees having salary greater than 30000
count = 0

for salary in employees.values():
    if salary > 30000:
        count += 1

print("\nNumber of employees having salary greater than 30000:", count)

# Display employees whose salary is below 20000
print("\nEmployees whose salary is below 20000:")

for emp_id, salary in employees.items():
    if salary < 20000:
        print(emp_id)