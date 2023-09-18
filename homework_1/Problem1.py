"""
Erica Miller
2031854
"""
print("Birthday Calculator\n")

current_month = int(input("Enter the current month: "))
current_day = int(input("Enter the current day: "))
current_year = int(input("Enter the current year: "))
birthday_month = int(input("Enter your birthday month: "))
birthday_day = int(input("Enter your birthday day: "))
birthday_year = int(input("Enter your birthday year: "))
age = current_year - birthday_year
if current_month < birthday_month:
    age -= 1
elif current_month == birthday_month:
    if current_day < birthday_day:
        age -= 1
print(f"You are {age} years old.")
if current_month == birthday_month and current_day == birthday_day:
    print("Happy Birthday!")
