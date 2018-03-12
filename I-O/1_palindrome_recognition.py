"""
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line
to the screen if it is a palindrome.
"""


def palindrome(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            if line == line[::-1] and line:
                print(line)


palindrome('d.txt')