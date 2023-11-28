#!/usr/bin/python3
def uppercase(s):
    for char in s:
        print("{:c}".format(ord(char) - 32) if ord('a') <= ord(char) <= ord('z') else char, end="")
    print()
