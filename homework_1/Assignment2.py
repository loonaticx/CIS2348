"""
Erica Miller
2031854
"""
# Get the first user input
user_num = int(input("Enter integer:\n"))

# Output the user's input
print("You entered:", user_num)

# Calculate and output the square and cube of the input
square = user_num * user_num
cube = user_num * user_num * user_num
print(f"{user_num} squared is {square}")
print(f"And {user_num} cubed is {cube} !!")

# Get the second user input
user_num2 = int(input("Enter another integer:\n"))

# Calculate and output the sum and product of the two inputs
sum_result = user_num + user_num2
product_result = user_num * user_num2
print(f"{user_num} + {user_num2} is {sum_result}")
print(f"{user_num} * {user_num2} is {product_result}")
