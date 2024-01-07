#!/usr/bin/python3
def no_c(my_string):
    copy_string = list(my_string)
    i = 0
    for a in copy_string:
        if a == 'c' or a == 'C':
            copy_string[i] = ""
            i = i + 1
    return "".join(copy_string)
