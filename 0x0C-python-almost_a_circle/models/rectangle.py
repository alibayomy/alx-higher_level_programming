#!/usr/bin/python3
"""The Definition of Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base
    class attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int("width", value)
        self.__width = value

    @property
    def height(self):
        "The height of the recatngle"
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value)
        self.__height = value

    @property
    def x(self):
        """the x coordiante of the recatngle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return self.__height * self.__width

    def display(self):
        for d in range(self.y):
            print()

        for h in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id,
                                                self.x, self.y, self.width,
                                                self.height)

    def _update(self, id=None, width=None, height=None, x=None, y=None):
        """assigns an argument to each attribute:"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args:
            self._update(*args)
        else:
            self._update(**kwargs)

    def to_dictionary(self):
        return {"y": self.__y,
                "x": self.__x,
                "id": self.id, "width": self.width,
                "height": self.height}
