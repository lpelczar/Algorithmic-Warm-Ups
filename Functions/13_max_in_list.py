"""
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three
numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how
many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
"""


def max_in_list(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max


print(max_in_list([1,3,5,323,5]))