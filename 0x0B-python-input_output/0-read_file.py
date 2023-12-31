#!/usr/bin/python3
"""Read file function"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)
                and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
