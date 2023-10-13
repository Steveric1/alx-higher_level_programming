#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set()
    sum = 0

    for number in my_list:
        if number not in unique_numbers:
            sum += number
            unique_numbers.add(number)
    return (sum)
