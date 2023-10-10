#!/usr/bin/python3
"""load_from_json_file function definition"""
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file”:"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        mystr = myFile.read()
        mystr = json.loads(mystr)
        return (mystr)
