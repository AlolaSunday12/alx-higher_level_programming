#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += '\n\n'

            print(result.rstrip())
