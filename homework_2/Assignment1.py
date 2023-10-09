"""
Erica Miller
2031854
"""


def strengthen_password(password):
    # Define the character replacement key
    char_replacements = {
        'i': '!',
        'a': '@',
        'm': 'M',
        'B': '8',
        'o': '.'
    }

    # Initialize an empty result string
    result = ""

    # Iterate through the characters in the input password
    for char in password:
        # Check if the character is in the key, if so, replace it
        if char in char_replacements:
            result += char_replacements[char]
        else:
            result += char  # If not in the key, keep the original character

    # Append "q*s" to the end of the result string
    result += "q*s"

    return result


# Get user input for the password
userPassword = input()

# Call the function to strengthen the password
strong_password = strengthen_password(userPassword)

# Print the result
print(strong_password)
