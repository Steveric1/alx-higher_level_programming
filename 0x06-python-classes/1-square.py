#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square defines
    Arg(any data type): the square value
    """
    def __init__(self, size):
        """size with no type/value verification"""
        self.__size = size
