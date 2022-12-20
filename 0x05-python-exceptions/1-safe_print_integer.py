#!/usr/bin/python3

def safe_print_integer(value):
    """print integer with .format.

    Args:
         value(int): The int vals to print
    Returns:
         false for TypeError otherwise True
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
