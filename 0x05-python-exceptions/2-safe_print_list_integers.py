#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    i = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
            i += 1
        except (TypeError, ValueError):
            i += 1
            continue
    print("")
    return num
