"""
Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the
largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function
directly?
"""
import functools


def max_in_list(numbers):
    return functools.reduce(lambda a, b: a if a > b else b, numbers)


print(max_in_list([47, 11, 42, 102, 13]))