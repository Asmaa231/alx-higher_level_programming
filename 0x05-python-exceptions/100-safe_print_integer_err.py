#!/usr/bin/python3
def safe_print_integer_err(value):
import sys

def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        is_int = False
    return is_int