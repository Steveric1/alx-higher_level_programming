#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length/2)
    LOI = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return LOI[mid]
    elif mid - 1 < 0:
        return LOI[mid] if LOI[mid] > LOI[mid + 1] else LOI[mid + 1]
    elif mid + 1 >= length:
        return LOI[mid] if LOI[mid] > LOI[mid - 1] else LOI[mid - 1]

    if LOI[mid - 1] < LOI[mid] > LOI[mid + 1]:
        return LOI[mid]

    if LOI[mid + 1] > LOI[mid - 1]:
        return find_peak(LOI[mid:])
    return find_peak(LOI[:mid])
