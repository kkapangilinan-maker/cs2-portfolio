# Excercise 3:

for num in range(1, 16):
# Starts loop with 1 being the starting value and 16 being the ending value that is not included.
    if num % 3 == 0:
# Checks is value of 'num' is divisible by 3.
        continue
# Skips the number divisible by 3.
    print(num)
# prints the value of 'num' that isn't skipped.
