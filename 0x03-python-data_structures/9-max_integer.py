#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_list.sort()
        leng = len(my_list) - 1
        return my_list[leng]
