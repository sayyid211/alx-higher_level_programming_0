#!/usr/bin/python3
for i in range(99):
    if int(i / 10) != i % 10 and int(i / 10) < i % 10:
        if i < 89:
            print("{}{}, ".format(int(i / 10), i % 10), end='')
print("89")
