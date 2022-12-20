#!/usr/bin/python3

def safe_print_division(a, b):
    """Print the division of a and b.
    Args:
    a: numerator
    b: denominator
    Returns: a/b
    """
    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
        return (c)
