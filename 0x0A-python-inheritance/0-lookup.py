#!/usr/bin/python3
"""
This module provides a function to return the list of available attributes and methods of an object.

The lookup function takes an object and returns a list of attributes and methods.

"""

def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj (object): The input object.

    Returns:
        list: A list containing the names of attributes and methods of the object.

    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or not attr.startswith("__")]
