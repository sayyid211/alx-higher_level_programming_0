#!/usr/bin/python3
"""Module for test_indentation"""


def text_indentation(text):
    """Indents a text string"""
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError('text must be a string')

    new_str = "".join([i if i not in ".?:" else i + "\n\n" for i in text])
    print("\n".join([i.strip() for i in new_str.split("\n")]), end="")
