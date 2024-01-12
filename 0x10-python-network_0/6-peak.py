#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    if (list_of_integers == []):
        return None
    left = leftTree(list_of_integers)
    right = rightTree(list_of_integers)
    if (left < right):
        return right
    return left


def leftTree(numList):
    """Left tree """
    if (len(numList) == 0):
        return 0
    elif (len(numList) == 1):
        return numList[0]
    else:
        mid = (len(numList) - 1) // 2
        if (numList[mid - 1] < numList[mid] &
                numList[mid] > numList[mid+1]):
            return numList[mid]
        else:
            return leftTree(numList[:mid + 1])


def rightTree(numList):
    """check right tree"""
    if (len(numList) == 0) | (numList == []):
        return 0
    elif (len(numList) == 1):
        return numList[0]
    else:
        mid = (len(numList)) // 2
        if (numList[mid - 1] < numList[mid] &
                numList[mid] > numList[mid+1]):
            return numList[mid]
        else:
            return rightTree(numList[mid:])
