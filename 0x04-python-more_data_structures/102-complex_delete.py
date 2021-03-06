#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value 'value' in a dictionary"""
    keys_pop = set()
    for k, v in a_dictionary.items():
        if v == value:
            keys_pop.add(k)
    for k in keys_pop:
        a_dictionary.pop(k)
    return a_dictionary
