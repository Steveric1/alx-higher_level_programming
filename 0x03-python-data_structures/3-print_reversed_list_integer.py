#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    reverse_list = reversed(my_list)
    for r in reverse_list:
        print("{:d}".format(r))