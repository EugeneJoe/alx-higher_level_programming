#!/usr/bin/python3
"""Contains definition of lazy_matrix_mul() function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using numpy module

    Args:
        m_a (list): a list of lists containing only integers or floats
            number of columns of m_a must match number of rows of m_b
        m_b (list): a list of lists containing only integers or floats
            number of rows of m_a must match number of columns of m_b

    """

    # Check type of m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # Check type of lists in m_a
    for m1 in m_a:
        if not isinstance(m1, list):
            raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for m1 in m_a:
        if len(m1) == 0:
            raise ValueError("m_a can't be empty")
        for m in m1:
            if not isinstance(m, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    # Check type of lists in m_b
    for m1 in m_b:
        if not isinstance(m1, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for m1 in m_b:
        if len(m1) == 0:
            raise ValueError("m_b can't be empty")
        for m in m1:
            if not isinstance(m, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(set([len(x) for x in m_a])) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set([len(x) for x in m_b])) != 1:
        raise TypeError("each row of m_b must be of the same size")
    columns_a = [len(x) for x in m_a]
    rows_b = len(m_b)
    for a in columns_a:
        if a != rows_b:
            raise ValueError("m_a and m_b can't be multiplied")

    res = np.dot(m_a, m_b)
    return res
