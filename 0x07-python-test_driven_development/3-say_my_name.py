#!/usr/bin/python3
"""
This module provides a function to print a person's name.

The say_my_name function takes a first name and an optional last name, and prints a message saying "My name is <first name> <last name>".

"""

def say_my_name(first_name, last_name=""):
    """
    Print a person's name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}"
    print(full_name)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
