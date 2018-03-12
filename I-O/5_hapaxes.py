"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a
language, the works of an author, or in a single text. Define a function that given the file name of a text will
return all its hapaxes. Make sure your program ignores capitalization.
"""
import re


def hapaxes(filename):
    with open(filename) as f:
        data = f.read()
    words = re.findall(r"[\w']+|[.,!?;]", data)
    words = [word.lower() for word in words]

    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    for k, v in count.items():
        if v == 1:
            print('{} : {}'.format(k, v))


hapaxes('d.txt')