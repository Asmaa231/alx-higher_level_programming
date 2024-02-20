#!/usr/bin/python3
"""define write_file with 2 args"""


def write_file(filename="", text=""):
    """read filename with utf-8"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
