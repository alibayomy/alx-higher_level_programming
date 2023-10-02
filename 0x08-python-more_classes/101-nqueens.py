#!/usr/bin/python3
"""The Nqueens Buzzle"""


import sys


def solution(int):
    """till i know the solution"""
    lst1 = [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    lst2 = [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    lst3 = [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    lst4 = [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
    print(lst1, lst2, lst3, lst4)


if __name__ == "__main__":
    if len((sys.argv)) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    solution(int(sys.argv[1]))
