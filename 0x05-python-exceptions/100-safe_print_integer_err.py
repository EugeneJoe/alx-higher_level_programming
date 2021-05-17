#!/usr/bin/python
import sys


def safe_print_integer_err(value):
    """Prints an integer and handles exceptions"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
