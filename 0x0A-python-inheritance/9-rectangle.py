#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class inherits from BaseGeometry and represents a rectangle with width and height.

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

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(width, height): Initialize a rectangle with specified width and height.
        area(): Calculate the area of the rectangle.
        __str__(): Return the rectangle description as a string.

    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the rectangle description as a string.

        Returns:
            str: The rectangle description.

        """
        return f"[Rectangle] {self.__width}/{self.__height}"
