#!/usr/bin/python3
"""My BaseGeometry class"""


class BaseGeometry:
    """My own definied BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(self.name))
