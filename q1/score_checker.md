Clean Decision Code Makeover: Student Score Checker

Name: Kyle Kiluma A. Pangilinan

Section: 8-Dahlia

Part 1 - Analyzing logic
Input

The program needs a student score.

Valid Range

Minimum valid score: 0

Maximum valid score: 100

Possible Outputs

Invalid Score.

Outstanding

Very Satisfactory

Satisfactory

Needs Improvement

Boundary Condition

The program checks if the score is below 0 or above 100.

student_score < 0 OR student_score > 100


If this condition is true, the program displays Invalid Score.

Multiple Decision Paths

The program uses if, elif, and else to choose the correct classification based on the student's score.

Part 2 - Flowchart
- cs2-portfolio/q1/score_checker_flowchart.png

Part 3 - Pseudocode
START

INPUT student_score

IF student_score < 0 OR student_score > 100 THEN
    DISPLAY "Invalid Score."
ELSE IF student_score >= 90 THEN
    DISPLAY "Outstanding"
ELSE IF student_score >= 80 THEN
    DISPLAY "Very Satisfactory"
ELSE IF student_score >= 75 THEN
    DISPLAY "Satisfactory"
ELSE
    DISPLAY "Needs Improvement"
END IF

END

Part 4 - Clean Code
Programming Language:
Python
Source Code:
score_checker.py

Final Code
#Ask the user for score
student_score = int(input("Enter student score: "))

#Check if score is between 0 and 100
if student_score < 0 or student_score > 100:
    print("Invalid Score.")

#Check score and give the correct classification
elif student_score >= 90:
    print("Outstanding")
elif student_score >= 80:
    print("Very Satisfactory")
elif student_score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")

| Test | Input | Purpose |
|---:|---:|---|
| 1 | -1 | Below minimum |
| 2 | 0 | Minimum boundary |
| 3 | 74 | Below Satisfactory boundary |
| 4 | 75 | Satisfactory boundary |
| 5 | 80 | Very Satisfactory boundary |
| 6 | 90 | Outstanding boundary |
| 7 | 100 | Maximum boundary |
| 8 | 101 | Above maximum |

Testing Reflection
1. Why is it important to test the values 0 and 100?

It is important to test 0 and 100 because they are the minimum and maximum valid scores.

2. Why did you also test -1 and 101?

I tested -1 and 101 because they are outside the valid range and should display Invalid Score.

3. Which test helped you understand boundary conditions the most?

The tests for 75, 80, and 90 helped me understand boundary conditions because these scores are where the classifications change.

4. Did any of your tests initially fail? If yes, what did you change in your program?

No. My tests passed because the conditions were arranged correctly.

Reflection
1. How did selection structures make the program more useful?

Selection structures allow the program to choose different outputs depending on the student's score.

2. How did proper comments and readable formatting improve your program?

The comments explain the important parts of the code, and proper formatting makes the program easier to read and understand.

3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?

A flowchart and pseudocode help organize the program's logic before writing the actual code. They make it easier to understand the decisions the program needs to make.
