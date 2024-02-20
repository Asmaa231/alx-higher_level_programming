#!/usr/bin/python3
"""define load_from_json function"""


import json


def load_from_json_file(filename):
    """creates an Object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
