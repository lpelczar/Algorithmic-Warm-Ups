"""
Define a function gcd(a, b) which returns the greatest common divisor of numbers a and b.
* Define a function gcd_of_all(*numbers) which returns the greatest common divisor for all numbers.
"""


def gcd(a, b):
    high = max(a, b)
    for i in reversed(range(1, high + 1)):
        if a % i == 0 and b % i == 0:
            return i


def gcd_of_all(*numbers):
    high = max(numbers)
    for i in reversed(range(1, high + 1)):
        if all(number % i == 0 for number in numbers):
            return i


print(gcd_of_all(2,4,6))