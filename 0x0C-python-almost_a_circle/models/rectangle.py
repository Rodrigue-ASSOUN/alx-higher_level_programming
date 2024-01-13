#!/usr/bin/python3
""" model for rectangle that inherits from base class """

from models.base import Base


class Rectangle(Base):
    """
    Private instance attributes, each with its own public getter and setter

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        If the input is not an integer,
        raise the TypeError exception with the message:
        <name of the attribute> must be an integer.
          Example: width must be an integer
        If width or height is under or equals 0,
        raise the ValueError exception with the message:
            <name of the attribute> must be > 0.
        Example: width must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        If x or y is under 0,
        raise the ValueError exception with the message:
            <name of the attribute> must be >= 0.
        Example: x must be >= 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """ rints in stdout the Rectangle instance with the character # """
        print("\n" * self.__y, end="")
        for _ in range(self.height):
            print(" " * self.__x, end="")
            print("#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                                                            self.id, self.__x,
                                                            self.__y, self.__width,
                                                            self.__height)

    def update(self, *args):
        """
        that assigns an argument to each attribute
        """
        if len(args) > 1:
            self.id = args[0]

        if len(args) > 2:
            self.width = args[1]

        if len(args) > 3:
            self.height = args[2]

        if len(args) > 4:
            self.x = args[3]

        if len(args) > 5:
            self.y = args[4]
