#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for n in lst:
            if (n == len(lst)):
                print("{:d}".format(n), end="")
                break
            print("{:d} ".format(n), end="")
        print()
