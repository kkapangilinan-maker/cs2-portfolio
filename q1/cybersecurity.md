Activity: PSHS Secure Club Registration System
Name: Kyle Kiluma A. Pangilinan
Section: 8-Dahlia
Quarter: 1

Activity Overview

In this activity, I analyzed a cybersecurity threat and created secure data-capture rules for a simple PSHS Club Registration System. The goal is to make a program that collects only necessary information and accepts only correct and appropriate input.

Part A - Cybersecurity Threat Analysis

Assigned Case:

Case 1:
Case Title: Fake Login Alert

A message claims that the student's account will be disabled and asks them to click a link and enter their username and password.

1. What cybersecurity threat is shown?

The threat is phishing. It tries to trick the student into giving away their username and password.

2. What warning signs make the situation suspicious?

The message says that the account will be disabled and asks the student to click a link and enter private login information. This creates pressure and makes the message suspicious.

3. What may be affected?

The student's account and personal information could be affected if the student enters their login details into a fake website.

4. What information could be exposed or misused?

The student's username and password could be exposed or misused. Other information connected to the account could also be exposed.

5. What should the user do to reduce the risk?

The user should not click any suspicious links or enter their username and password on shady sites. They should verify the message using an official school website or ask a teacher or school administrator.

Part B - Data Privacy and Secure Data Capture

| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | It is needed to identify the student registering for the club. |
| Section | Collect | It is needed to identify the student's section. |
| Club Choice | Collect | It is needed to know which club the student selected. |
| School Email | Collect | It can be used for school-related communication. |
| Attendance Status | Collect | It is needed to record the student's attendance. |
| Password | Do Not Collect | A password is not needed for this simple registration system. |
| OTP | Do Not Collect | An OTP is not needed for club registration. |
| Home Address | Do Not Collect | A home address is not needed for club registration. |
| Parent Bank Account | Do Not Collect | Banking information is not needed and is sensitive information. |

Why is it safer to collect only information that the program actually needs?
  
  - It is safer because collecting less personal information reduces the amount of private data that could be stolen.

Part C - Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Student's name | Missing student information | Blank | Must not be blank | Student name is required. |
| Section | Teacher-approved section | Incorrect section | Invalid section | Must be an accepted section | Invalid section. |
| Club Choice | Robotics, Science, Mathematics, or Programming | Incorrect club registration | Gaming | Must be an accepted club | Please choose a valid club. |
| School Email | Email containing `@` and `.` | Incorrect email information | studentpshs.edu.ph | Must contain `@` and `.` | Invalid school email. |
| Attendance Status | Present, Absent, or Late | Incorrect attendance information | Excused | Must be an accepted status | Invalid attendance status. |

1. What should your program accept?

The program should accept a non-blank student name, an accepted section, a valid club choice, a school email containing @ and ., and an attendance status of Present, Absent, or Late.

2. What should your program reject?

The program should reject blank names, invalid sections, invalid club choices, emails without @ or ., and invalid attendance statuses.

3. How do your validation rules help reduce incorrect or unsafe input?

The validation rules help prevent incorrect information from being accepted. They also make sure that the program only accepts the information needed for registration.

Part D - Secure Program Implementation
Program

The program collects only:

- Student Name

- Section

- Club Choice

- School Email

- Attendance Status

The program does not request passwords, OTPs, banking information, and other unnecessary personal information.

Source Code File:
secure_registration.py

Final Code:

student_name = input("Enter student name: ")

#Check if student name is blank
if student_name == "":
    print("REGISTRATION NOT ACCEPTED")
    print("Student name is required.")

else:
    section = input("Enter section: ")

    #Check if section is valid
    if section != "Dahlia":
        print("REGISTRATION NOT ACCEPTED")
        print("Invalid section.")

    else:
        club_choice = input("Enter your choice of club from the following: Robotics, Science, Mathematics, Programming: " )

        #Check if club choice is valid
        if club_choice not in ["Robotics", "Science", "Mathematics", "Programming"]:
            print("REGISTRATION NOT ACCEPTED")
            print("Please choose a valid club.")

        else:
            school_email = input("Enter school email: ")

            # Check if email contains @ and .
            if "@" not in school_email or "." not in school_email:
                print("REGISTRATION NOT ACCEPTED")
                print("Invalid school email.")

            else:
                attendance_status = input("Enter attendance status (Present, Absent, Late): ")

                #Check if attendance status is valid
                if attendance_status not in ["Present", "Absent", "Late"]:
                    print("REGISTRATION NOT ACCEPTED")
                    print("Invalid attendance status.")

                else:
                    print("")
                    print("REGISTRATION ACCEPTED")
                    print("")
                    print("Student:", student_name)
                    print("Section:", section)
                    print("Club:", club_choice)
                    print("Email:", school_email)
                    print("Attendance:", attendance_status)


Security Practices Applied:

Required Input:

I checked if the student name is blank. If it is blank, the registration is rejected.

Allowed Values:

The section, club choice, and attendance status are checked against accepted values.

Format Check:

The school email must contain both @ and ..

Error Messages:

Clear error messages tell the user what information is incorrect.

Data Minimization:

I did not collect passwords, OTPs, home addresses, or parent bank account information because they are not necessary for club registration.

Part E - Security Testing and Reflection
Testing:

| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | Registration accepted | Registration accepted | PASS |
| 2 | Blank student name | Registration rejected | Registration rejected | PASS |
| 3 | Invalid section | Registration rejected | Registration rejected | PASS |
| 4 | Invalid club choice | Registration rejected | Registration rejected | PASS |
| 5 | Email missing `@` | Registration rejected | Registration rejected | PASS |
| 6 | Email missing `.` | Registration rejected | Registration rejected | PASS |
| 7 | Invalid attendance status | Registration rejected | Registration rejected | PASS |
| 8 | Different valid inputs | Registration accepted | Registration accepted | PASS |


Reflection
1. What is one cybersecurity threat that can affect an application or user?

Phishing is a cybersecurity threat that can trick users into giving away private information such as usernames and passwords.

2. How can users reduce the risk of phishing or suspicious messages?

Users can avoid clicking suspicious links, check the sender, and verify messages through an official source.

3. How can validation rules improve the security of user input?

Validation rules help prevent incorrect or unexpected information from being accepted by the program.

4. Why should a program avoid collecting unnecessary personal information?

A program should avoid collecting unnecessary information because private data could be exposed or misused.

5. How did SG7's input validation concepts become security practices in SG8?

The input validation concepts from SG7 help make sure that programs accept only appropriate information. In SG8, these checks can also help protect data and reduce unsafe input.
