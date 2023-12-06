#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    for k in sorted(keys):
        print("{} : {}".format(k, a_dictionary[k]))
