
student_name = input("Enter student name: ")

try:
    age = int(input("Enter age: "))
except ValueError:
    print("REGISTRATION NOT ACCEPTED")
    print("Age must be a number.")
    age = -1

grade_level = input("Enter grade level: ")
email = input("Enter email: ")
registration_code = input("Enter registration code: ")

# Check if student name is blank
if student_name == "":
    print("REGISTRATION NOT ACCEPTED")
    print("Student name is required.")

# Check if age is within the valid range
elif age < 11 or age > 18:
    print("REGISTRATION NOT ACCEPTED")
    print("Age must be from 11 to 18.")

# Check if grade level is accepted
elif grade_level not in ["7", "8", "9", "10", "11", "12"]:
    print("REGISTRATION NOT ACCEPTED")
    print("Invalid grade level.")

# Check if email contains @ and .
elif "@" not in email or "." not in email:
    print("REGISTRATION NOT ACCEPTED")
    print("Invalid email address.")

# Check if registration code has 6 characters
elif len(registration_code) != 6:
    print("REGISTRATION NOT ACCEPTED")
    print("The registration code must contain exactly 6 characters.")

else:
    print("------------------------------")
    print("REGISTRATION ACCEPTED")
    print("------------------------------")
    print("Student:", student_name)
    print("Age:", age)
    print("Grade Level:", grade_level)
    print("Email:", email)
    print("Registration Code:", registration_code)
