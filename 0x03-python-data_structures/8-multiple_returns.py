#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != ():
        length = len(sentence)-1, sentence[0]
    else:
        length = 0, None
    return length
