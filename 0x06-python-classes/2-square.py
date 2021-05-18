#!/usr/bin/python3
"""Contains a definition of a class Square"""


class Square:
    """Definition of a class Square."""

    def __init__(self, size=0):
        """Initializes an object of the class Square.

        Ensures that the parameter passed is of type int and is not less than 0

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
