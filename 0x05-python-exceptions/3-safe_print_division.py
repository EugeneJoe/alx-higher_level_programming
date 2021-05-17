#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides 2 integers and prints the result. Handles ZeroDivision error"""
    res = 0
    try:
        res = float(a) / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(res if b != 0 else None))
    return res
