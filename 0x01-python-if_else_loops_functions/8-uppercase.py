#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97:
            print(f"{chr(ord(i) - 32)}", end='')
        else:
            print(f"{i}", end='')
