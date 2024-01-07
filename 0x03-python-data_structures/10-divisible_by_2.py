#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copylist = my_list[:]
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            copylist[i] = True
        else:
            copylist[i] = False
    return copylist
