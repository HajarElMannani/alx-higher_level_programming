#!/usr/bin/python3
import sys
__name__ == "__main__"
i, c = 1, 0
while i < len(sys.argv):
    c = c + int(sys.argv[i])
    i = i + 1
print("{}".format(c))
