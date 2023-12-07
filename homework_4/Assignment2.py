"""
Erica Miller
2031854
"""

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        # Try to convert the second part to an integer
        age = int(parts[1]) + 1
    except ValueError:
        # Handle the ValueError by setting age to 0
        age = 0
    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
