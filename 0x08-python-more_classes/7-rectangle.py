#!/usr/bin/python3
"""My definition of Rectangle class"""


class Rectangle:
    """My Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """New instance of Rectangle class with
            2 attributes:
            Width: the width of the recatngle
            Height: the height of the rectangle"""
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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

    def __str__(self):
        """The string representation of an instance of the Rectangle class"""
        string = ""
        if not (self.width == 0 or self.height == 0):
            for i in range(self.height):
                for x in range(self.width):
                    string = string + str((self).print_symbol)
                if i != self.height - 1:
                    string = string + "\n"
        return string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
