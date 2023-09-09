#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for n in lst:
            if (n == len(lst)):
                print("{}".format(n), end="")
                break
            print("{} ".format(n), end="")
        print()
