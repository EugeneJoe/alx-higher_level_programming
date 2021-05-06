#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    values = [x * 2 for x in list(a_dictionary.values())]
    keys = list(a_dictionary.keys())
    new = {}
    for i in range(len(a_dictionary)):
        new.update({keys[i]: values[i]})
    return new
