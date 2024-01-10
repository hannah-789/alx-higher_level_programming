#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

The BaseGeometry class is an empty class with a public instance method 'area()' that raises an Exception with the message 'area() is not implemented'.

"""

class BaseGeometry:
    """
    A class representing BaseGeometry.

    Attributes:
        None.

    Methods:
        area(): Raises an Exception with the message 'area() is not implemented'.

    """
    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: Always raises an Exception with the message 'area() is not implemented'.

        """
        raise Exception("area() is not implemented")
