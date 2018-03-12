"""
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a
frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character
frequency table to the screen.
"""
import os.path
import operator


def char_freq_table():
    filename = input('Enter filename: ')
    if not os.path.exists(filename):
        print('File does not exist!')
    else:
        with open(filename) as f:
            data = f.read()
        d = {}
        for i in data:
            if i != '\n':
                d[i] = d.get(i, 0) + 1
        sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
        for k, v in sorted_d.items():
            print('{} : {}'.format(k, v))

char_freq_table()