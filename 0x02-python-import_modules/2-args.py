#!/usr/bin/python3
import sys
__name__ == "__main__"
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:\n1: {}".format(sys.argv[1]))
else:
    i = 1
    print("{} arguments:".format(len(sys.argv) - 1))
    while i < len(sys.argv):
        print("{}: {}".format(i, sys.argv[i]))
        i = i + 1
