#!/usr/bin/python3
"""
This module provides a function to add two integers.

The add_integer function takes two arguments, a and b, and returns their addition after ensuring they are integers.

"""

def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first operand.
        b (int or float): The second operand. Default is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Casting to integers if inputs are floats
    a = int(a)
    b = int(b)

    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
