"""
Erica Miller
2031854
"""

# Read coefficients and constants for the two equations
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

# Flag to check if a solution is found
solution_found = False

# Iterate through possible values of x and y
for x in range(-10, 11):
    for y in range(-10, 11):
        # Check if both equations are satisfied
        if (a1 * x + b1 * y == c1) and (a2 * x + b2 * y == c2):
            print(x, y)
            solution_found = True
            break

# If no solution is found, print "No solution"
if not solution_found:
    print("No solution")
