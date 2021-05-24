#!/usr/bin/python3
"""
Contains the definition of class Rectangle.
"""


class Rectangle:
    """Definition of class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new instance of class Rectangle

        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the rectangle

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Return value of width attribute

        Set value of width attribute. Must be a positive integer.
        Raises:
            TypeError
                If value is not of type int
            ValueError
                If value is a negative value
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return value of height attribute

        Set value of height attribute. Must be a positive integer.
        Raises:
            TypeError
                If value is not of type int
            ValueError
                If value is a negative value
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Return a string representation of a rectangle.
        Rectangle is represented using the character '#'

        """

        rect = []
        if self.__height == 0 or self.__width == 0:
            return ''
        for n in range(0, self.__height):
            rect.append('#' * self.__width)
            if n != self.__height - 1:
                rect.append('\n')  # To ensure no extra blank line is added
        return ''.join(rect)

    def __repr__(self):
        """Return a string representation of the rectangle.
           Should be able to recreate a new instance by using eval().
        """

        return '{self.__class__.__name__}({self.width}, {self.height})'.\
format(self=self)
