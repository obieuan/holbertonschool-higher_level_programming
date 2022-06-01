#!/usr/bin/python3
"""
load_from_json_file function module.
Define load_from_json_file function.
"""


import json


def load_from_json_file(filename):
    """Returns an object from a text file JSON string.
    filename (str): the file to load from.
    """
    with open(filename, 'r', encoding="UTF-8") as myfile:
        return json.loads(myfile.read())
