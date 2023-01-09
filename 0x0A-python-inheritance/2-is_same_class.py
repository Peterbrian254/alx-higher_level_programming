#!/usr/bin/python3

""" Module "1-my_list" defines a function is_same_class
that returns True if the passed object is an exact instance
of the specified class else returns False
"""


def is_same_class(obj, a_class):
    """Returns true if obj is instance of a_class"""
    if type(obj) == a_class:
        return True
    else:
        return False
