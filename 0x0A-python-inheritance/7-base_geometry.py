#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

The BaseGeometry class has public instance methods 'area()' that raises an Exception with the message 'area() is not implemented' and 'integer_validator()' that validates an integer value.

"""

class BaseGeometry:
    """
    A class representing BaseGeometry.

    Attributes:
        None.

    Methods:
        area(): Raises an Exception with the message 'area() is not implemented'.
        integer_validator(name, value): Validates an integer value.

    """
    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: Always raises an Exception with the message 'area() is not implemented'.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
