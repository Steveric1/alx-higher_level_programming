#!/usr/bin/python3

def search_replace(my_list, search, replace):
    i = 0
    list_copy = my_list.copy()
    length = len(list_copy)

    while i < length:
        if search == list_copy[i]:
            list_copy[i] = replace
        i += 1

    return list_copy
