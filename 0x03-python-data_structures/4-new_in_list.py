#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    n = len(new_list)
    if idx < 0 or idx > (n - 1):
        return new_list
    new_list[idx] = element
    return new_list
