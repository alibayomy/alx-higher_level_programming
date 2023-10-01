#!/usr/bin/python3
"""A function that adds to ints"""


def add_integer(a, b=98):
    """Returns the addition of a two ints or floats"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
