"""
Erica Miller
2031854
"""
import math

# Define the cost of paint per gallon for each color
paint_colors = {
    "red": 35,
    "blue": 25,
    "green": 23,
}

# Prompt the user to input wall's height and width
wall_height = float(input("Enter wall height (feet):\n"))
wall_width = float(input("Enter wall width (feet):\n"))

# Calculate the wall area
wall_area = int(wall_height * wall_width)

# Calculate the amount of paint needed
paint_needed = wall_area / 350.0

# Calculate the number of paint cans needed (rounded up to the nearest gallon)
cans_needed = math.ceil(paint_needed)

# Prompt the user for a paint color
print(f"Wall area: {wall_area} square feet")
print(f"Paint needed: {paint_needed:.2f} gallons")
print(f"Cans needed: {cans_needed} can(s)")

color_choice = input("\nChoose a color to paint the wall:\n").lower()

# Calculate the total cost of paint cans based on the chosen color
if color_choice in paint_colors:
    cost_per_gallon = paint_colors[color_choice]
    total_cost = cost_per_gallon * cans_needed
    print(f"Cost of purchasing {color_choice} paint: ${total_cost}")
else:
    print("Invalid color choice. Please choose a valid color.")
