"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list
comprehensions.
"""


def words_to_length(words):
    # lengths = []
    # for i in words:
    #     lengths.append(len(i))
    # return lengths

    # return list(map(lambda x: len(x), words))

    return [len(x) for x in words]


print(words_to_length(['hahaha', 'ha']))