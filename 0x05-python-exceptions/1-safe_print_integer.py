#!/usr/bin/python3


def safe_print_integer(value):
    """Print value with {:d}.format() format specifier and handle any ValueError
       exceptions.

    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
