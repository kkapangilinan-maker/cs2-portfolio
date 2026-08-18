import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

distance_squared = math.pow(dx, 2) + math.pow(dy, 2)
distance = math.sqrt(distance_squared)

print(f"The distance between the two points is: {distance:.2f}")

# Reflection:
# The math library makes the program easier because I can use sqrt() and pow().
# The math library allows you to access advanced math functions.
