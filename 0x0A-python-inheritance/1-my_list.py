#!/usr/bin/python3
"""My List class"""


class MyList(list):
    """My own MyList class definition"""
    def print_sorted(self):
        print(sorted(self))
