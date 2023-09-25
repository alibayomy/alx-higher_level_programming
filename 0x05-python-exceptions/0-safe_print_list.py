#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    while (num_printed < x):
        try:
            print(my_list[num_printed], end="")
            num_printed = num_printed + 1
        except:
            print()
            return (num_printed)
    print()
    return (num_printed)
