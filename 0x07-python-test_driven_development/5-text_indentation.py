#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines after each of these characters: ., ? and :

The text_indentation function takes a text and prints it with 2 new lines after each occurrence of the characters '.', '?', and ':'.

"""

def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char

        if char in punctuation_chars:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
