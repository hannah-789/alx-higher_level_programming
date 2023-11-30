#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    arg_plural = "s" if num_args != 1 else ""
    print("Number of argument{}: {}".format(arg_plural, num_args), end="")
    if num_args == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
