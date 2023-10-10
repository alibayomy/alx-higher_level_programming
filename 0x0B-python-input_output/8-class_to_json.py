#!/usr/bin/python3
"""class_to_json function definition"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return __dict__(obj)
