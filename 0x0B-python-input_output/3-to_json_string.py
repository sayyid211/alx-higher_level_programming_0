#!/usr/bin/python3
"""module foe json write"""
import json


def to_json_string(my_obj):
    """computes and return a stringg's json representation"""
    return json.dumps(my_obj)
