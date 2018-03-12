"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list
of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""


def sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


def multiply(numbers):
    m = 1
    for i in numbers:
        m *= i
    return m


print(sum([1, 2, 3, 4]))
print(multiply([1, 2, 3, 4]))