#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        if len(lst) == 0:
            print()
        for n in range(len(lst)):
            print("{:d}".format(lst[n]),
                  end="\n" if n is len(lst) - 1 else " ")
