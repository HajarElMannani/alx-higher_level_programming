#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    i = 0
    try:
        for j in range(0, x):
            print("{}".format(my_list[i]), end="")
            num += 1
            i += 1
        print("")
    except IndexError:
        print("")
        return num
    return num
