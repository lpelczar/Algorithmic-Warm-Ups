"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
"""

def length_mapping(words):
    lengths = []
    for i in words:
        lengths.append(len(i))
    return lengths


print(length_mapping(['cat', 'elephant']))