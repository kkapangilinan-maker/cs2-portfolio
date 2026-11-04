def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3) /3
def get_performance(average):
  if average >= 85:
    return "Mastery"
  elif average < 70:
    return "Needs Review"
  else:
    return "Developing"
def is_eligible(average, completed_tasks):
  if average >= 85 and completed_tasks >= 3:
    return "True"
  else:
    return "False"

score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
completed_tasks = int(input("Completed Tasks: "))

average = calculate_average(score1, score2, score3)
performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print("------------------------------------------------")
print(f"Average: {average:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge {eligible}")
print("------------------------------------------------")

# 1. Which function returns a number, which returns a string, and which returns a Boolean? - calculate_average() returns a number, get_performance() returns a string, and is_eligible() returns a Boolean.
# 2. Explain how the average moves from calculate_average() into get_performance(). - calculate_average() returns the average from the values of score 1 - 3 which is stored in the variable "average" which is then used by the function get_performance().
# 3. What happens when a student has a high average but has completed fewer than three tasks? - The student will not be eligible for the challange task because the requirement to become eligible for the challange is to have atleast 3 completed task.
# 4. Why is return more appropriate than simply printing the result inside each function? - Return stores the value into a variable which can then be used by other functions.
