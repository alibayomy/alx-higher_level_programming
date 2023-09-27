#!/usr/bin/python3
"""Defining my own square class"""


class Square:
    """Defining my own representation of square"""
    def __init__(self, size=0, position=(0, 0)):
        """Inititalize a new square
        Args:
        size: the size of the square
        position: the x,y coordinates of the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """a getter for retreving the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """a setter to set the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ A posoition getter to retrive thde data"""
        return self.__position

    @position.setter
    def position(self, value):
        """a setter to set the position (x,y) values"""
        if ((len(value) != 2) or
            not isinstance(value, tuple)
                or (value[0] > 0 and value[1] > 0)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(slef):
        """get the area of the square"""
        return (self.__size) * (self.__size)

    def my_print(self):
        """that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        position should be use by using space"""
        if self.__size is 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """define the print() representation of square"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
