"""
Your task in this exercise is as follows:
Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.

Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of
opening/closing brackets (in that order), none of which mis-nest.

Examples:

  []        OK   ][        NOT OK
  [][]      OK   ][][      NOT OK
  [[][]]    OK   []][[]    NOT OK
  [][][][]

"""
import random
import re


def brackets(n):

    brackets_list = list('[]' * n)
    random.shuffle(brackets_list)
    result = ''.join(brackets_list)

    bracket_string = result

    while re.findall(r'\[\]', result):
         result = re.sub(r'\[\]', '', result)

    if result:
        print(bracket_string + ' NOT OK')
    else:
        print(bracket_string + ' OK')


brackets(4)
