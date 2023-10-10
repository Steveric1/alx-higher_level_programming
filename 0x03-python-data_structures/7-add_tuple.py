#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, padding with 0 if necessary
    tuple_a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    tuple_b = tuple_b[:2] + (0,) * (2 - len(tuple_b))

    # Calculate the sum of the corresponding elements from both tuples
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple
