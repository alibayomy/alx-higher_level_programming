#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for n in lst:
            if (n == len(lst) - 1):
                print("{:d}".format(n), end=" ")
            else:
                print("{:d} ".format(n), end="")
        print()
