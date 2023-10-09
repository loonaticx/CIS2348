"""
Erica Miller
2031854
"""

import csv

# Hardcoded input file name
file_name = input()

# Create a dictionary to store word frequencies
word_count = {}

# Open the input file and read its contents using csv.reader
with open(file_name, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        for word in row:

            # If the word is already in the dictionary, increment its count
            if word in word_count:
                word_count[word] += 1
            else:
                # If the word is not in the dictionary, add it with count 1
                word_count[word] = 1

# Iterate through the dictionary and print unique words and their frequencies
for word, count in word_count.items():
    print(f"{word} {count}")
