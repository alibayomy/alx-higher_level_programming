#!/usr/bin/python3
"""save_to_json_file function definition"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
                using a JSON representation:"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
