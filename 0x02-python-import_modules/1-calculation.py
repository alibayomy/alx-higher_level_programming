#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{}".format(a), "+", "{}".format(b), "=", add(a, b))
    print("{}".format(a), "-", "{}".format(b), "=", sub(a, b))
    print("{}".format(a), "*", "{}".format(b), "=", mul(a, b))
    print("{}".format(a), "/", "{}".format(b), "=", div(a, b))
