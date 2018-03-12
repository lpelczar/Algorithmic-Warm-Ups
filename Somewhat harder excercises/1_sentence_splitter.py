"""
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for
sentence splitting includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that
Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
Periods followed by a digit with no intervening whitespace are not sentence boundaries.
Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are
not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries
Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file is able to write its content with each
sentence on a separate line. Test your program with the following short text:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it
isn't.

The result should be:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.
"""
import re

titles = "(Mr|St|Mrs|Ms|Dr)[.]"

def sentence_splitter(filename):
    with open(filename) as f:
        data = f.read()

    print(data + '\n')
    data = data.replace("\n", " ")
    data = re.sub('\. (?=[a-z])', '<prd><space>', data)
    data = re.sub('\.(?=[1-9])', '<prd>', data)
    data = re.sub('(Mr|St|Mrs|Ms|Dr)[.](?= [A-Z])', '\\1<prd>', data)
    data = re.sub('(?<=[a-z])\.(?=[a-z])', '<prd>', data)

    sentences = re.split('(?<=[.?!]) ', data)
    for s in sentences:
        s = s.replace('<prd>', '.')
        s = s.replace('<space>', ' ')
        print(s)


sentence_splitter('data.txt')