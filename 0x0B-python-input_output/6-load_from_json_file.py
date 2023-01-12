#!/usr/bin/python3
"""module for loading json"""
import json


def load_from_json_file(filename):
    """Fetch object from json file"""
    with open(filename) as f:
        file_d = f.read()
        return json.loads(file_d)
