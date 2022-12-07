#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = my_list[:]
    for i, k in enumerate (new):
        if k == search:
            new[i] = replace
    return new
