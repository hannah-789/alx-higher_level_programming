#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from the built-in list class.

The MyList class provides an additional public instance method to print the list in sorted order.

"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Attributes:
        Inherits all attributes and methods from the list class.

    """

    def print_sorted(self):
        """
        Print the list in sorted (ascending) order.

        Returns:
            None

        """
        sorted_list = sorted(self)
        print(sorted_list)

