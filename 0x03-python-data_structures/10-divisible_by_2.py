#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lst = []
    idx = 0
    for i in my_list:
        if my_list[i] % 2 == 0:
            new_lst.append(True)
        else:
            new_lst.append(False)
    return new_lst
