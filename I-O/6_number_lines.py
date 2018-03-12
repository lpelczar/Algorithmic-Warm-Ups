"""
Write a program that given a text file will create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file).
"""

def number_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        numbered_lines = [str(k + 1) + '. ' + v for k, v in enumerate(lines)]

    with open('newfile.txt', 'w') as f:
        for line in numbered_lines:
            f.write(line)


number_lines('d.txt')