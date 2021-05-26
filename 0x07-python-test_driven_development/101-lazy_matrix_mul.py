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

    return np.array(m_a).dot(np.array(m_b))
