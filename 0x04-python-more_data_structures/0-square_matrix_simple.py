#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_lst = matrix[:]
    double = lambda x : x * x
    for i in range(len(matrix)):
        new_lst[i] = list(map(double, matrix[i]))
    return list(new_lst)
