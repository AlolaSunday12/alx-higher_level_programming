#!/usr/bin/python3
def magic_string():
    """
    Returns a string 'BestSchool' repeated n times, where n
    is the number of the iteration.

    Returns:
        str: The repeated string.
    """
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(['BestSchool'] * magic_string.count)
