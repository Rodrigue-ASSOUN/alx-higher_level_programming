#!/usr/bin/python3

"""Rectangle class."""


class Rectangle:
    """A simple rectangle."""

    def __init__(self, width=0, height=0):
        """
        Instantiates the rectangle with optional width and height
        """
        self.width = width
        self.height = height
Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a '#' string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (('#' * self.__width + '\n') * self.__height)[:-1]

    def __repr__(self):
        """should return a string representation of the rectangle to be able
            to recreate a new instance by using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """destructor"""
        print("Bye rectangle...")
Rectangle.number_of_instances -= 1
