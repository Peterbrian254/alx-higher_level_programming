#!/usr/bin/python3

""" Module "1-my_list" defines a class MyList that inherits from
list and has one public instance method print_sorted
"""


class MyList(list):
    """class that inherits from list class"""
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        print(sorted(self))
