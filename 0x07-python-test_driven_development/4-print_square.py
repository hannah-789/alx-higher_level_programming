#!/usr/bin/python3
"""
This module provides a function to print a square with the character #.

The print_square function takes the size length of the square and prints a square with # characters.

"""

def print_square(size):
    """
    Print a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size.is_integer() and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
