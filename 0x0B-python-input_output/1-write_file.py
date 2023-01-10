#!/usr/bin/python3

"""2-append_write module defines a function append_write that
appends to a text file and returns the number of characters
written
"""


def append_write(filename="", text=""):
    """returns the number of characters appended to filename passed"""
    with open(filename, "a") as f:
        return (f.write(text))
