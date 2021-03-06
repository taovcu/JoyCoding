import time
import sys
import math
import inflect
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.IO as io


def countObjects(m, n):
    io.printTTS("Count objects")
    pitem.emojiPrint(m, n)
    io.printTTS("How many {} do you see?".format(m))

    ans = io.readInt()
    if ans == n:
        io.printTTS('Correct')
    else:
        io.printTTS('Wrong')


# m is the item name: str
# n is the number of items: int
# s is the shape in which items are arranged: str
def countInShapes(m, n, s):
    io.printTTS("Count objects in {}".format(s))
    pitem.emojiPrint(m, n)
    io.printTTS("How many {} do you see?".format(m))

    ans = io.readInt()
    if ans == n:
        io.printTTS('Correct')
    else:
        io.printTTS('Wrong')

