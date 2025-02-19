#!/usr/bin/python3
''' function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers.'''
    if (list_of_integers == []):
        return (None)
    max = list_of_integers[0]
    for i in list_of_integers:
        if max >= i:
            continue
        else:
            max = i
    return max
