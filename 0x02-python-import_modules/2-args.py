#!/usr/bin/python3
def print_arg(argv):
    x = len(argv) - 1
    if x == 0:
        print("{:d} argument.".format(x))
        return
    else:
        if x == 1:
            print("{:d} argument:".format(x))
        else:
            print("{:d} arguments:".format(x))
        i = 1
        while i <= x:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
