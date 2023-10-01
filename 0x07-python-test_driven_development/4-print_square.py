#!/usr/bin/python3
"""print_square function definition"""


def print_square(size):
    """ prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for y in range(0, size):
            for x in range(0, size):
                print("#", end="")
            print()
