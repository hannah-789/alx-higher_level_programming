#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for i in range(x):
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
                printed_integers += 1

    except (IndexError, ValueError, TypeError):
        pass

    finally:
        print()

    return printed_integers
