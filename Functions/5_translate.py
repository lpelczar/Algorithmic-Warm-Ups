"""
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
should return the string "tothohisos isos fofunon".
"""


def translate(string):
    return ''.join([i + 'o' + i if i not in ['a', 'e', 'i', 'o', 'u', ' '] else i for i in list(string)])


print(translate("this is fun"))