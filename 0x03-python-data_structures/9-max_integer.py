#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list == []:
        return None
    for n in my_list:
        if n > max:
            max = n
    return max
