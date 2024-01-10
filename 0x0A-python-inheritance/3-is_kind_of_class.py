#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

The is_kind_of_class function returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise, it returns False.

"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

    Args:
        obj (object): The input object.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a_class or its subclasses, False otherwise.

    """
    return isinstance(obj, a_class)

