"""
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""


def max_of_three(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


print(max_of_three(1, 88, 16))