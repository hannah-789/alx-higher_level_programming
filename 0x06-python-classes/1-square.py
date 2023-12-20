#!/usr/bin/python3

class Square:
    """
    This class defines a square.

    Attributes:
        size (int): Private instance attribute representing the size of the square.

    Methods:
        No methods are defined in this version.
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square.

        Note:
            No type or value verification is performed for the size parameter.
        """
        self.__size = size

