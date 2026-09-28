Activity: PSHS Workshop Registration Validator
Name: Kyle Kiluma A. Pangilinan
Section: 8 - Dahlia
Quarter: 1

Overview

This activity shows a program I created that checks the information of a student for registration. The program checks the student's name, age, grade level, email address, and registration code before accepting the registration.

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | A name | Presence Validation | Blank | Name must not be blank | Student name is required. |
| Age | An integer from 11 to 18 | Data Type and Range Validation | `fourteen`, `25` | Age must be a number and from 11 to 18 | Age must be a number. / Age must be from 11 to 18. |
| Grade Level | 7, 8, 9, 10, 11, or 12 | Acceptable Value Validation | `13` | Grade level must be 7–12 | Invalid grade level. |
| Email Address | Email containing `@` and `.` | Pattern Validation | `studentpshs.edu.ph` | Email must contain `@` and `.` | Invalid email address. |
| Registration Code | Exactly 6 characters | Length Validation | `ABC` | Code must contain exactly 6 characters | The registration code must contain exactly 6 characters. |

1. Why should the student name not be blank?

The student name should not be blank because the program needs to know who is registering.

2. Why should age be checked for both data type and range?

Age should be checked for both because it must be a number and it must be between 11 and 18.

3. Why should grade level only accept specific values?

Grade level should only accept specific values so that the program does not accept an invalid grade level.

4. What format requirements did you use for the email address?

The email must contain both @ and ..

5. What length requirement did you use for the registration code?

The registration code must contain exactly 6 characters.

Part B - Program Design

Before writing the program, I created pseudocode to plan how the program would work.

Pseudocode:

START

INPUT student name

IF student name is blank THEN
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY "Student name is required."
    STOP
END IF

INPUT age

IF age is not a number THEN
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY "Age must be a number."
    STOP
END IF

IF age is less than 11 OR age is greater than 18 THEN
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY "Age must be from 11 to 18."
    STOP
END IF

INPUT grade level

IF grade level is not 7, 8, 9, 10, 11, or 12 THEN
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY "Invalid grade level."
    STOP
END IF

INPUT email

IF email does not contain "@" OR email does not contain "." THEN
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY "Invalid email address."
    STOP
END IF

INPUT registration code

IF registration code does not contain exactly 6 characters THEN
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY "The registration code must contain exactly 6 characters."
    STOP
END IF

DISPLAY "REGISTRATION ACCEPTED"
DISPLAY student name
DISPLAY age
DISPLAY grade level
DISPLAY email
DISPLAY registration code

END

The pseudocode shows the user input, validation decisions, error messages, accepted registration, and rejected registration.

Part C - Program Implementation
Programming Language:
Python
Source Code File:
workshop_validator.py

Final Code:

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

# Check if registration code has exactly 6 characters
elif len(registration_code) != 6:
    print("REGISTRATION NOT ACCEPTED")
    print("The registration code must contain exactly 6 characters.")

else:
    print("")
    print("REGISTRATION ACCEPTED")
    print("")
    print("Student:", student_name)
    print("Age:", age)
    print("Grade Level:", grade_level)
    print("Email:", email)
    print("Registration Code:", registration_code)

Validation Techniques Used:
Presence Validation:
- I used presence validation to check whether the student name is blank.
Data Type Validation:
- I used data type validation with try and except to check whether the age is a number.
Range Validation:
- I checked whether the age is from 11 to 18.
Acceptable Value Validation:
- I checked whether the grade level is one of the accepted values from 7 to 12.
Pattern Validation:
- I checked whether the email contains both @ and ..
Length Validation:
- I checked whether the registration code has exactly 6 characters.

Part D - Testing
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 2 | Blank student name | Presence | Student name is required. | Student name is required. | PASS |
| 3 | Age = `fourteen` | Data type | Age must be a number. | Age must be a number. | PASS |
| 4 | Age = `11` | Minimum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 5 | Age = `18` | Maximum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 6 | Age = `10` | Range | Age must be from 11 to 18. | Age must be from 11 to 18. | PASS |
| 7 | Grade Level = `13` | Acceptable value | Invalid grade level. | Invalid grade level. | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | Invalid email address. | Invalid email address. | PASS |
| 9 | Registration Code = `ABC` | Length | The registration code must contain exactly 6 characters. | The registration code must contain exactly 6 characters. | PASS |
| 10 | Registration Code = `CS2026` | Valid length | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |

Important: For the Actual Output and Result columns, use what you actually get when you run your program. Don't claim PASS if you haven't tested it yet.
Part E - Output Verification
Verification Test 1

Input:

Maria Santos
14
8
maria@example.com
CS2026


Expected Output:


REGISTRATION ACCEPTED

Student: Maria Santos
Age: 14
Grade Level: 8
Email: maria@example.com
Registration Code: CS2026


Actual Output:


REGISTRATION ACCEPTED

Student: Maria Santos
Age: 14
Grade Level: 8
Email: maria@example.com
Registration Code: CS2026


Result: PASS

Explanation: The inputs meet all of the registration requirements, so the registration is accepted.

Verification Test 2

Input:

Maria Santos
10
8
maria@example.com
CS2026


Expected Output:

REGISTRATION NOT ACCEPTED
Age must be from 11 to 18.


Actual Output:

REGISTRATION NOT ACCEPTED
Age must be from 11 to 18.


Result: PASS

Explanation: The age is below the required range of 11 to 18, so the registration is not accepted.

Verification Test 3

Input:

Maria Santos
14
8
studentpshs.edu.ph
CS2026


Expected Output:

REGISTRATION NOT ACCEPTED
Invalid email address.


Actual Output:

REGISTRATION NOT ACCEPTED
Invalid email address.


Result: PASS

Explanation: The email does not contain @, so it does not meet the required email pattern.

Reflection
1. Why should a program validate input before processing it?

A program should validate input so that incorrect information does not cause problems or produce incorrect results.

2. What is the difference between input validation and output verification?

Input validation checks whether the information entered by the user is acceptable. Output verification checks whether the program produced the correct result.

3. Which validation technique was easiest for you to implement? Why?

Presence validation was easiest because I only needed to check if the name was blank.

4. Which validation technique was most challenging? Why?

Data type validation was the most challenging because I needed to handle an age that was not a number.

5. How did testing invalid inputs help you improve your program?

Testing invalid inputs helped me find problems and make sure the program gives the correct error messages.
