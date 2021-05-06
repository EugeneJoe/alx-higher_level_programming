#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary ordered by keys"""
    key_list = list(a_dictionary.keys())
    key_list.sort()
    for n in key_list:
        print("{}: {}".format(n, a_dictionary.get(n)))
