#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
   del(a_dictionary[key]) if a_dictionary[key] is not None
   return a_dictionary
