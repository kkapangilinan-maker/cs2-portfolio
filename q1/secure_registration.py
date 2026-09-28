student_name = input("Enter student name: ")

# Check if student name is blank
if student_name == "":
    print("REGISTRATION NOT ACCEPTED")
    print("Student name is required.")

else:
    section = input("Enter section: ")

    # Check if section is valid
    if section != "Dahlia":
        print("REGISTRATION NOT ACCEPTED")
        print("Invalid section.")

    else:
        club_choice = input("Enter your choice of club from the following: Robotics, Science, Mathematics, Programming: " )

        # Check if club choice is valid
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

                # Check if attendance status is valid
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
