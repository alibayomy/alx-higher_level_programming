#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    sum = 0

    if n == 1:
        print(0)
        exit()
    else:
        for i in range(n - 1):
            sum = int(sys.argv[i + 1]) + sum
    print(sum)
