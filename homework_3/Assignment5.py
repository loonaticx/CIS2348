"""
Erica Miller
2031854

Prompt:
    Write a program that gets a list of integers from input,
    and outputs non-negative integers in ascending order
    (lowest to highest).
"""
numbers = input()
numberList = sorted([int(num) for num in numbers.split(' ') if int(num) >= 0])
print(' '.join(str(num) for num in numberList) + " ", end = '')
