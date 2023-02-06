#!/usr/bin/python3
"""MyList"""


class MyList(list):
    """Defines a custom list"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
