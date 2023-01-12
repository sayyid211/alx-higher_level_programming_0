#!/usr/bin/python3
"""module save to json"""
import json


def save_to_json(my_obj, filename):
    """saves myobj to file"""
    with open(filename, 'w') as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
