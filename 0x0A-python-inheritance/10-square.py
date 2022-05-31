#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module BaseGeometry
"""


class Square(Rectangle):
    """ Square """

    def __init__(self, size):
        """ Constructor method """
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area """
        return super().area()
