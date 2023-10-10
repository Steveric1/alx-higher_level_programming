#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if my_list:
        for r in reversed(my_list):
            print("{:d}".format(r))
