#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if n >= 97 and n <= 122:
            print("{}".format(chr(n - 32)), end="")
        elif n == 32:
            print("{}".format(chr(n)), end="")
    print("")
