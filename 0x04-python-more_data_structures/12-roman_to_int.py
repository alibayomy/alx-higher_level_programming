#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        value = 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        str_lst = list(roman_string)
        for i in str_lst:
            if i in dic:
                value = dic[i] + value
        if "IV" in roman_string or "IX" in roman_string:
            value = value - 2
        return value
    else:
        return 0
