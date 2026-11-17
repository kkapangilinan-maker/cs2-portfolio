# Exercise 4:

def show_table(num):
# Defines function that will show the multiplication table.
    for i in range(1, 11):
# Starts loop using variable 'i', with 1 being the starting value and 11 being the ending value that isn't included.
        print(num, "x", i, "=", num * i)
# Prints each segment of multiplication table of the number.
num = int(input("Enter a number: "))
# Asks for the value of 'num'
show_table(num)
# Calls function
