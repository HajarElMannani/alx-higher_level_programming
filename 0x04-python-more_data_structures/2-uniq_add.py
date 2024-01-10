#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    sum = 0
    for i in newlist:
        sum = sum + i
    return sum
