#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big = 0
        key_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        for i in val_list:
            if i > big:
                big = i
        position = val_list.index(big)
        return (key_list[position])
    else:
        return None
