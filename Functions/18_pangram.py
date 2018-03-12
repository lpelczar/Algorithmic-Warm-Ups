"""
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see
if it is a pangram or not.
"""
import string


def is_pangram(sentence):
    sentence = [letter for letter in sentence if letter.isalpha()]
    alphabet = string.ascii_lowercase
    for ch in alphabet:
        if ch not in sentence:
            return False
    else:
        return True


print(is_pangram('The quick brown fox jumps over the lazy dog.'))