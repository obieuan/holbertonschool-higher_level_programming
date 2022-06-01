#!/usr/bin/python3
"""
from_json_string function module.
Define from_json_string function.
"""


import json


def from_json_string(my_str):
    """Returns an object made from JSON string.
    my_str: the string to load from JSON.
    """
    return json.loads(my_str)
