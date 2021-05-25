#!/usr/bin/python3
"""
Contains definition for class LockedClass.
"""


class LockedClass:
    """Definition of class LockedClass that only defines one attribute"""

    def __setattr__(self, name, value):
        """Called when dynamically creating a new instance attribute

        Args:
            name (str): name of new attribute being created
            value (any): value of the attribute being created
        """

        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'{}' object has no attribute '{}'".
                                 format(self.__class__.__name__, name))
