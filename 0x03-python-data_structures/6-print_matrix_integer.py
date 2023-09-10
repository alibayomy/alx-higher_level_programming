#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        if len(lst) == 0:
            print()
        for n in range(len(lst)):
            if (n == len(lst) - 1):
                print("{:d}".format(lst[n]), end="\n")
            else:
                print("{:d} ".format(lst[n]), end=" ")
