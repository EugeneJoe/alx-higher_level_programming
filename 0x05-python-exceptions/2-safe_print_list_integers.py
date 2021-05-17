#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
       Print the first x elements of my_list and only integers.

       Description:
       Print only the first x integer elements of my_list and skip any
       non-integer elements. Catches any IndexError exceptions raised.
       Returns the number of integers printed

    """
    count = 0
    try:
        for n in range(0, x):
            if type(my_list[n]) is int:
                print("{:d}".format(my_list[n]), end="")
                count+=1
        print()
    except IndexError as IE:
        raise
    return count
