"""
Erica Miller
2031854
"""


def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Compare the string with its reverse
    return s == s[::-1]


# Input from the user
input_str = input()

# Check if it's a palindrome
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not a palindrome")
