#!/usr/bin/python3
"""
square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherited from Rectangle"""

    def __init__(self, size):
        """attributes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
