#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sort = sorted(a_dictionary)
        for key in sort:
            print(f"{key}: {a_dictionary[key]}")
