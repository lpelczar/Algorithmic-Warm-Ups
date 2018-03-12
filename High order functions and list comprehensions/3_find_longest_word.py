"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
Use only higher order functions.
"""
import functools


def find_longest_word(words):
    return len(functools.reduce(lambda a, b: a if len(a) > len(b) else b, words))


print(find_longest_word(['cat','elephant','snake']))