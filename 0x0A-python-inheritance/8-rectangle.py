#!/usr/bin/python3
"""
Contains definition of class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize an instance of class Rectangle"""

        try:
            super().integer_validator("width", width)
        except Exception as e:
            raise e
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")
