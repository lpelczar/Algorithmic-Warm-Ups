"""
"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as
it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics
are as follows:
99 bottles of beer on the wall, 99 bottles of beer.

Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero.

Your task here is write a Python program capable of generating all the verses of the song.
"""


def generate_song():
    bottles_quantity = 99
    for i in reversed(range(0, bottles_quantity)):
        print('{} bottles of beer on the wall, {} bottles of beer. Take one down, pass it around, {} bottles of' \
            ' beer on the wall.'.format(bottles_quantity, bottles_quantity, bottles_quantity - 1))
        bottles_quantity -= 1

generate_song()