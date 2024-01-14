#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Call the super class with id, x, y, width and height 
        this super call will use the logic of the __init__ of the
            Rectangle class.
        The width and height must be assigned to the value of size
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        You must not create new attributes for this class,
        use all attributes of Rectangle - As reminder:
            a Square is a Rectangle with the same width and height
        All width, height, x and y validation must inherit from Rectangle
            - same behavior in case of wrong data
        """
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        The overloading __str__ method should return
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,self.x,
                                                self.y, self.width)
