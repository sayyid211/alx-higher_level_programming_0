#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dup = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            dup[i] = replace
    return dup
