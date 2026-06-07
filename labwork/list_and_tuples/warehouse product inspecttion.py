# program for warehouse product inspection
'''
Write a program to: 
• Display failed product IDs.  
• Count passed and failed products.  
• Calculate pass percentage.  
• Stop checking if 3 failures are found. '''

products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0
failed_ids = []

# Check products
for status in products:

    if status[1] == "Pass":
        pass_count += 1

    else:
        fail_count += 1
        failed_ids.append(status)

        # Stop checking if 3 failures are found
        if fail_count == 3:
            print("3 failures found. Stopping check.")
            break

# Calculate pass percentage
total_checked = pass_count + fail_count
pass_percentage = (pass_count / total_checked) * 100

# Display results
print("Failed Product IDs:", failed_ids)
print("Passed Products:", pass_count)
print("Failed Products:", fail_count)
print("Pass Percentage:", pass_percentage, "%")