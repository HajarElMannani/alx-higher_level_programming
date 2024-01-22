#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        c = fct(*args)
        return c
    except Exception as erro:
        print("Exception: {}".format(erro), file=sys.stderr)
        return None
