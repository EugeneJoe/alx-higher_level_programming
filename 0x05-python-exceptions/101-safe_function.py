#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely and prints an error message, if any, to stderr"""

    try:
        return fct(*args)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
