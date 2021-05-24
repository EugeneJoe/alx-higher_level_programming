#!/usr/bin/python3
"""
Contains the definition of class Rectangle.
"""


class Rectangle:
    """Definition of class Rectangle

    Args:
        number_of_instances (int): counter for number of objects in existence
        print_symbol (any): used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new instance of class Rectangle

        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the rectangle

        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

        rect = ''
        if self.__height == 0 or self.__width == 0:
            return ''
        for n in range(0, self.__height):
            rect += (str(self.print_symbol) * self.__width)
            if n != self.__height - 1:
                rect += '\n'  # To ensure no extra blank line is added
        return rect

    def __repr__(self):
        """Return a string representation of the rectangle.
           Should be able to recreate a new instance by using eval().
        """

        return '{self.__class__.__name__}({self.width}, {self.height})'.\
            format(self=self)

    def __del__(self):
        """Prints a message to the screen when a Rectangle object is deleted"""

        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError
                if either rect_1 or rect_2 is not instance of Rectangle class
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance that is a square of size 'size'

        Args:
            size (int): size of sides of the square
        """

        return cls(size, size)
