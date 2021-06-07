#!/usr/bin/python3
"""
Contains the definition of the class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of class Square that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an instance of class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Initialize and return size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of an instance of class Square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        Args:
            args (pointer): a "pointer" to an array of strings
            kwargs (double pointer): "double pointer" to a dictionary that has
                                     keyword:value pairs
        """
        if args is not None:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        if kwargs is not None:
            if "id" in kwargs.keys():
                self.id = kwargs.get("id")
            if "size" in kwargs.keys():
                self.width = kwargs.get("size")
                self.height = kwargs.get("size")
            if "x" in kwargs.keys():
                self.x = kwargs.get("x")
            if "y" in kwargs.keys():
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """Returns dictionary representation of instance of class Rectangle"""
        keys = ["id", "size", "x", "y"]
        return {a: getattr(self, a) for a in keys}
