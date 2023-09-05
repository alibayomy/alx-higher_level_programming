#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if (number < 0):
        print(-last_digit)
    else:
        print(last_digit)
