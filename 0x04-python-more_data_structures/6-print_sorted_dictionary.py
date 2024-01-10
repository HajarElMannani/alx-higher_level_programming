#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictn = sorted(a_dictionary.keys())
    for i in dictn:
        print("{}: {}".format(i, a_dictionary[i]))
