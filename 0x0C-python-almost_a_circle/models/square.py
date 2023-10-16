#!/usr/bin/python3
"""The Square Class file"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """My own Square class
        inherits from Rectangle
        Attributs:
        size: the size of the Square
        x: the x coordinate of the square
        y: the y coordinate of the square
        id : the id of the square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.__update(*args)
        else:
            self.__update(**kwargs)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
