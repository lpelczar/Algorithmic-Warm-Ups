"""
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the
lengths of the word tokens in the text, divided by the number of word tokens).
"""
import re


def avg_word_length(filename):
    with open(filename) as f:
        words = re.findall('\w+', f.read())
        return sum([len(word) for word in words]) / len(words)


print(avg_word_length('d.txt'))