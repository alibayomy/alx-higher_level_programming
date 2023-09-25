#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    num = 0
    while (num_printed < x):
        try:
            print("{:d}".format(my_list[num]), end="")
            num_printed = num_printed + 1
            num = num + 1
        except (TypeError, ValueError):
            num = num + 1
            continue
    print()
    return (num_printed)
