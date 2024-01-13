#!/usr/bin/python3
""" model for rectangle that inherits from base class """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            self.__width

        @width.setter
        def width(self):
            self.__width = width

        @property
        def height(self):
            self.__height

        @height.setter
        def height(self):
             self.__height = height

        @property
        def x(self):
            self.__x

        @x.setter
        def x(self):
            self.__x = x

        @property
        def y(self):
            self.__y

        @y.setter
        def y(self):
            self.__y = y
