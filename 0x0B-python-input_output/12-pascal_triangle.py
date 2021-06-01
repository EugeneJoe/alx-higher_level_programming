#!/usr/bin/python3
"""
Contains definition of function pascal_triangle(n)
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): order of Pascal's triangle to generate
    """
    res = []
    for i in range(n):
        res.append([int(k) for k in str(11**i)])
    return res
