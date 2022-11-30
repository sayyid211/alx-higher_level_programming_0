#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97:
            conv = -32
        else:
            conv = 0
        print("{}".format(chr(ord(i) + conv)), end='')
    print()
