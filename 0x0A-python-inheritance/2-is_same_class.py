#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly an instance of a specified class.

The is_same_class function returns True if the object is exactly an instance of the specified class, otherwise False.

"""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj (object): The input object.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.

    """
    return type(obj) == a_class

