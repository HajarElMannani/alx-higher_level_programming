#!/usr/bin/python3
import hidden_4
__name__ == "__main__"
for name in dir(hidden_4):
    if name[:2] != "__":
        print("{}".format(name))
