#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dup = a_dictionary.copy()
    keys = list(dup.keys())

    for i in dup:
        dup[i] *= 2
    return dup
