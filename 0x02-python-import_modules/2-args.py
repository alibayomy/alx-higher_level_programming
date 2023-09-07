#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    index = 1
    n = n - 1
    if (n == 1):
        print(n, "argument:")
    elif n == 0:
        print(n, "arguments.")
    else:
        print(n, "arguments:")
    for i in range(n):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
