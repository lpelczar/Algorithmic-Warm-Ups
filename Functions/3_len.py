"""
Define a function that computes the length of a given list or string. (It is true that Python has the len() function
built in, but writing it yourself is nevertheless a good exercise.)
"""


def length(list):
    length = 0
    for i in list:
        length += 1
    return length


print(length([1,5,34,234,3,4]))
print(length('lalala'))