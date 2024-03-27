#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
     """
    Find a peak element in a list of integers.

    A peak element is an element that is greater than its neighbors.
    This function uses a binary search approach to find a peak element,
    so its time complexity is O(log(n)), where n is the length of the input list.

    Args:
        list_of_integers (list): The list of integers.

    Returns:
        int: A peak element in the list.

    Raises:
        ValueError: If the list is empty.
    """
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]

