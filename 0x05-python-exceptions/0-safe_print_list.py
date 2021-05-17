#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
       Prints x number of elements of my_list.

       Description:
       my_list can contain elements of any type and x may be bigger than
       the number of elements of the list in which case the resulting error
       raised will be handled using a try-except block.

    """
    count = 0
    try:
        for n in range(0, x):
            print(my_list[n], end="")
            count += 1
        print()
    except IndexError:
            print()
    return count
