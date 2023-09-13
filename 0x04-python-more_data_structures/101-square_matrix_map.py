#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_lst = matrix[:]
    for i in range(len(matrix)):
        new_lst[i] = list(map(lambda x: x*x, matrix[i]))
    return list(new_lst)
