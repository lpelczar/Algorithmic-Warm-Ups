"""
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that
are longer than n.
"""


def filter_long_words(words, n):
    # return [x for x in words if len(x) > n]
    return list(filter(lambda x: len(x) > n, words))

print(filter_long_words(['cat', 'elephant'], 5))
