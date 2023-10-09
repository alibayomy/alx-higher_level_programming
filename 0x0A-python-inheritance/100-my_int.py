#!/usr/bin/python3
"""MyInt class that inherted from int"""


class MyInt(int):
    """My own MyInt class"""
    def __eq__(self, value):
        if self.real == value:
            return False
        True

    def __ne__(self, value):
        if self.real != value:
            return False
        True
