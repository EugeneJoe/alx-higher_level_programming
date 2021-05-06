#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a new list"""
    new = [x if x is not search else replace for x in my_list]
    return new
