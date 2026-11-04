def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3
def get_performance(average):
    if average >= 85:
        return "Mastery"
    elif average >= 70:
        return "Developing"
    else:
        return "Needs Review"
def is_eligible(average, completed_tasks):
    return average >= 85 and completed_tasks >= 3
  
score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
completed_tasks = int(input("Completed Tasks: "))

average = calculate_average(score1, score2, score3)

performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print("\nAverage:", format(average, ".2f"))
print("Performance:", performance)
print("Eligible for Challenge:", eligible)
