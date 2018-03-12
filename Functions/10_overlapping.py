"""
Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
"""


def overlapping(a, b):
    return any(a == b for a, b in zip(a, b))


print(overlapping([1,2,3,4], [5,6,7,8]))