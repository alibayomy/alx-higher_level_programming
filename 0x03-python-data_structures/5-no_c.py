#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string
    str_lst = list(new_str)
    if "c" in str_lst:
        str_lst.remove("c")
    if "C" in str_lst:
        str_lst.remove("C")
    new_str = "".join(str_lst)
    return new_str
