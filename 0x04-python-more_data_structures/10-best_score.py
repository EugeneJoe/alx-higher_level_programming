#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if a_dictionary:
        values = sorted(a_dictionary.values())
        for key in a_dictionary.keys():
            if a_dictionary.get(key) == values[-1]:
                return key
    else:
        return None
