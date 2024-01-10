#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

The inherits_from function returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise, it returns False.

"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj (object): The input object.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class, False otherwise.

    """
    return isinstance(obj, type) and issubclass(type(obj), a_class)

