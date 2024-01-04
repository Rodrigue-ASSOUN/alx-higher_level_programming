"""
Real definition of a rectangle
"""
class Rectangle:
    """
    Instantiation with optional width and height
    Constructor
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    """
    #property getter  WIDTH
    Private instance attribute: width

    #property setter
    property def width(self): to retrieve it
    property setter def width(self, value): to set it
    width must be an integer, otherwise raise a TypeError exception
        with the message width must be an integer
    if width is less than 0, raise a ValueError exception
        with the message width must be >= 0

    #property getter HEIGHT
    property def height(self): to retrieve it

    #property setter
    property setter def height(self, value): to set it:
    height must be an integer, otherwise raise a TypeError exception
        with the message height must be an integer
    if height is less than 0, raise a ValueError exception
        with the message height must be >= 0
    """

    @property
    def width(self):
        self.__width = width
    
    @width.setter
    def width(self, value):
        if width is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        self.__height = height

    @height.setter
    def height(self, value):
        if height is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
