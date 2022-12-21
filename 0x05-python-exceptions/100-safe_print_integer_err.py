#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """print int on stdout and other types on stderr
    Args:
        value: argument to print
    Returns:
        True for int otherwise False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
