"""
Erica Miller
2031854

Prompt:
    Write a program that reads a list of words.
    Then, the program outputs those words and their frequencies.
"""
words = input()
wordList = words.split(' ')
for word in wordList:
    print(f"{word} {wordList.count(word)}")
