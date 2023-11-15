#!/usr/bin/python3
"""Square class definition"""


class Square:
    """New square class definition"""
    def __init__(self, size=0):
        """initialize the square class with filed of size
        Args:
            size(int or float): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve a value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a value (Setter of self.__size)
        Args:
            value(int or float): size of the square
        return: None
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if square is equal to another by area
        Args:
            other(Square): square to compare against
        Return:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other(Square): square to compare against
        Return:
            True or False
        """
        return self.size != other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other(Square): square to compare against
        Return:
            True or False
        """
        return self.size > other.size

    def __ge__(self, other):
        """Compare if square is greater than equal to
        another by area
        Arg:
            other(Square): square to compare against
        Return:
            True or False
        """
        return self.size >= other.size

    def __lt__(self, other):
        """Compare if square is less than another by area
        Arg:
            other(Square): square to compare against
        Return:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another
        by area
        Args:
            other(Square): square to compare against
        Return:
            True or False
        """
        return self.size <= other.size
