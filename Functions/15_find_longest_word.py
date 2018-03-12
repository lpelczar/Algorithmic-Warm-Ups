"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
"""


def find_longest_word(words):
    return len(max(words, key=len))


print(find_longest_word(['cat', 'elephant']))