#!/usr/bin/python3
"""My Int"""


class MyInt(int):
    """Defines my int"""

    def __eq__(self, other):
        """== comparison operator for my int"""
        return int(str(self)) != other

    def __ne__(self, other):
        """!= comparison operator for my int"""
        return int(str(self)) == other
