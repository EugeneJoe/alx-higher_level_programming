#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    res = [[x ** 2 for x in row] for row in matrix]
    return res
