#!/usr/bin/python3
"""My definition of Rectangle class"""


class Rectangle:
    """My Rectangle class"""
    def __init__(self, width=0, height=0):
        """New instance of Rectangle class with
            2 attributes:
            Width: the width of the recatngle
            Height: the height of the rectangle"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return (self.width * 2) + (self.height * 2)
