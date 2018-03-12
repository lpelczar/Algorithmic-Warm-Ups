"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul",
"and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into
Swedish. Use the higher order function map() to write a function translate() that takes a list of English words and
returns a list of Swedish words.
"""

lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}


def translate(words):
    return list(map(lambda x: lexicon[x], words))


print(translate(['merry', 'christmas', 'and', 'happy', 'new', 'year']))