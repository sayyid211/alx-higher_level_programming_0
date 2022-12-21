#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Performs contigeous divisions
      Args:
        my_list_1: first list
        my_list_2: divisors
        list_length: length of lists
      Returns: List of divisions
    """
    divs = []
    for i in range(0, list_length):
        try:
            fraction = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            fraction = 0
        except ZeroDivisionError:
            print("division by 0")
            fraction = 0
        except IndexError:
            print("out of range")
            fraction = 0
        finally:
            divs.append(fraction)
    return divs
