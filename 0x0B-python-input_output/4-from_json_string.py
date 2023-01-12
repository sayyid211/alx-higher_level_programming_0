#!/usr/bin/python3
"""read json str module"""
import json


def from_json_string(my_str):
    """return string from a json representation"""
    return json.loads(my_str)
