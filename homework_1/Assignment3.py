"""
Erica Miller
2031854
"""

# Prompt the user for the number of cups of lemon juice, water, and agave nectar
lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))

# Output the ingredients and serving size
print("\nLemonade ingredients - yields {:.2f} servings".format(servings))
print("{:.2f} cup(s) lemon juice".format(lemon_juice_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar".format(agave_nectar_cups))

# Prompt the user to specify the desired number of servings
desired_servings = float(input("\nHow many servings would you like to make?\n"))

# Adjust the amounts of each ingredient accordingly
scale_factor = desired_servings / servings
lemon_juice_cups *= scale_factor
water_cups *= scale_factor
agave_nectar_cups *= scale_factor

# Output the adjusted ingredients and serving size
print("\nLemonade ingredients - yields {:.2f} servings".format(desired_servings))
print("{:.2f} cup(s) lemon juice".format(lemon_juice_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar".format(agave_nectar_cups))

# Convert the ingredient measurements to gallons (1 gallon = 16 cups)
lemon_juice_gallons = lemon_juice_cups / 16
water_gallons = water_cups / 16
agave_nectar_gallons = agave_nectar_cups / 16

# Output the ingredients in gallons
print("\nLemonade ingredients - yields {:.2f} servings".format(desired_servings))
print("{:.2f} gallon(s) lemon juice".format(lemon_juice_gallons))
print("{:.2f} gallon(s) water".format(water_gallons))
print("{:.2f} gallon(s) agave nectar".format(agave_nectar_gallons))
