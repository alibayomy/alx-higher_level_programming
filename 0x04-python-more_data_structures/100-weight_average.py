#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    average = 0
    for t in my_list:
        weight = weight + (t[0] * t[1])
        average = average + t[1]
    return (weight / average)
