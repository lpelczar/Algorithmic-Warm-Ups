"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word
or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at
http://www.puzzlers.org/pub/wordlists/unixdict.txt
write a program that finds the sets of words that share the same characters that contain the most words in them.
"""
from collections import defaultdict


def anagram(filename):
    with open(filename) as f:
        words = f.read().splitlines()

    d = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        d[key].append(word)

    for v in sorted(d.values(), key=len):
        print('Quantity: {} -> {}'.format(len(v), v))


anagram('unixdict.txt')