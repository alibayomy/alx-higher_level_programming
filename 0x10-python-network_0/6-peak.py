#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    listLen = len(list_of_integers)
    if list_of_integers == []:
        return None
    elif (listLen == 1):
        return list_of_integers[0]
    else:
        for i in range(1, listLen):
            if (list_of_integers[i - 1] < list_of_integers[i]
                    & list_of_integers[i] > list_of_integers[i + 1]):
                return list_of_integers[i]
        return list_of_integers[listLen - 1]
