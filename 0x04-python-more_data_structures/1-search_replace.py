#!/usr/bin/python3
def search_replace(my_list, search, replace):
    c = lambda(search, replace): search = replace
    return map(c, my_list)
