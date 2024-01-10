#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = []
    for elem in my_list:
        if elem != search:
            nlist.append(elem)
        else:
            nlist.append(replace)
    return nlist
