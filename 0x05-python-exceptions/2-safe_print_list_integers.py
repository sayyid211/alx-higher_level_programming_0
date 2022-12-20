#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print a list of integers
       Args:
            my_list: list to print
            x: index of list
       Returns:
               Number of integers printed
    """
    rt = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            rt += 1
        except (ValueError, TypeError):
            continue
    print()
    return (rt)
