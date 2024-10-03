#!/usr/bin/python3
def no_c(my_string):
    ''' a function that removes c and C from a string'''
    new_string = ""
    for char in my_string:
        if (ord(char) == 67) or (ord(char) == 99):
            continue
        new_string = new_string + char
    return new_string
