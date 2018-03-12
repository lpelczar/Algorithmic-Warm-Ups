"""
Implement the higher order functions map(), filter() and reduce().
(They are built-in but writing them yourself may be a good exercise.)
"""


def map(function, iterable):
    for i in iterable:
        yield function(i)


def filter(function, iterable):
    for i in iterable:
        if function(i):
            yield i


def reduce(func, seq):
    seq = iter(seq)
    value = next(seq)
    for x in seq:
        value = func(x, value)
    return value


print(list(map(lambda x: len(x), ['this','is'])))
print(list(filter(lambda x: x > 4, [3,6,1,2,7,9,10])))
print(reduce(lambda a,b: a if (a > b) else b, [47,11,42,102,13]))