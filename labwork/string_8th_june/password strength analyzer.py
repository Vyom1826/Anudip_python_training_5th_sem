'''A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately. '''
# Program to analyze password strength

# Taking password as input from the user

password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
):
    print("Valid Password")
else:
    print("Invalid Password")

    if len(password) < 8:
        print("- Password must contain at least 8 characters")
    if not has_upper:
        print("- Password must contain an uppercase letter")
    if not has_lower:
        print("- Password must contain a lowercase letter")
    if not has_digit:
        print("- Password must contain a digit")
    if not has_special:
        print("- Password must contain a special character")


# --------------------------------------------------
# Initializing counters and lists
# --------------------------------------------------
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

digit_list = []
special_list = []

# --------------------------------------------------
# Counting uppercase, lowercase, digits,
# and special characters
# --------------------------------------------------
for ch in password:

    # Checking for uppercase letter
    if ch.isupper():
        uppercase_count += 1

    # Checking for lowercase letter
    elif ch.islower():
        lowercase_count += 1

    # Checking for digit
    elif ch.isdigit():
        digit_count += 1
        digit_list.append(ch)

    # Remaining characters are special characters
    else:
        special_count += 1
        special_list.append(ch)

# --------------------------------------------------
# Determining password strength
# --------------------------------------------------

# Checking all conditions for a strong password
if (len(password) >= 8 and
    uppercase_count >= 1 and
    lowercase_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):

    strength = "Strong"

# Checking conditions for a medium password
elif len(password) >= 8 and (uppercase_count > 0 or
                             lowercase_count > 0 or
                             digit_count > 0):
    strength = "Medium"

# Otherwise password is weak
else:
    strength = "Weak"

# --------------------------------------------------
# Displaying results
# --------------------------------------------------
print("\nPassword:", password)

print("\nUppercase Letters:", uppercase_count)
print("Lowercase Letters:", lowercase_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("\nDigits Found:", int(digit_list))
print("Special Characters Found:", special_list)

print("\nPassword Strength:", strength)
