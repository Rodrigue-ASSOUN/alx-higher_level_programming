#!/usr/bin/python3
"""
module to access and update private attribute
"""


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Getter method to get the value of size
        """
        return (self.__size)

    """
    Setter method to set the value of size
    """
    @size.setter
    def size(self, value):
        """
        check if the value is an integer. If not, raise a TypeError
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")

        """
        If value is less than 0, raise a ValueError.
        """
        elif value < 0:
            raise ValueError("size must be >= 0")

        """
        If value is a valid integer and not less than 0,
        assign it to the private instance attribute
        """
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return (self.__size ** 2)
