#!/usr/bin/python3
"""Find a peak"""


def find_peak(ints):
    """Finds a peak in a list of unsorted integers."""
    if not ints:
        return None
    left = 0
    right = len(ints) - 1
    while left < right:
        mid = left + (right - left) // 2
        if ints[mid] > ints[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return ints[left]
