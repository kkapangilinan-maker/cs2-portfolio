# Ask user for their score
student_score = int(input("Enter student score: "))

# Check if score is between 0 and 100
if student_score < 0 or student_score > 100:
    print("Invalid Score.")

# Check score and give the correct classification
elif student_score >= 90:
    print("Outstanding")
elif student_score >= 80:
    print("Very Satisfactory")
elif student_score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")
