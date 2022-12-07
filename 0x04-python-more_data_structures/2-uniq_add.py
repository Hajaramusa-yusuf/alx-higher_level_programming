#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    re = 0
    for i in new:
        re += i
    return re
